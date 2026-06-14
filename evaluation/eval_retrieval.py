from __future__ import annotations

import json
import math
#from collections import defaultdict
from pathlib import Path
from typing import Any

import pandas as pd

from config import settings
from evaluation.test_schema import TestQuestion
from rag_app.retriever import fetch_context


def load_tests(path: Path | None = None) -> list[TestQuestion]:
    test_path = path or settings.EVALUATION_TESTS_PATH
    tests: list[TestQuestion] = []
    with test_path.open("r", encoding="utf-8") as file:
        for line in file:
            if line.strip():
                tests.append(TestQuestion.model_validate(json.loads(line)))
    return tests


def _matches(document_text: str, source: str, test: TestQuestion) -> bool:
    text = f"{source}\n{document_text}".lower()
    source_match = any(expected.lower() in source.lower() for expected in test.expected_sources)
    keyword_match = any(keyword.lower() in text for keyword in test.keywords)
    return source_match or keyword_match


def _ndcg(relevances: list[int]) -> float:
    dcg = sum(rel / math.log2(index + 2) for index, rel in enumerate(relevances))
    ideal = sorted(relevances, reverse=True)
    idcg = sum(rel / math.log2(index + 2) for index, rel in enumerate(ideal))
    return dcg / idcg if idcg else 0.0


def evaluate_retrieval(k: int | None = None) -> tuple[pd.DataFrame, pd.DataFrame, list[dict[str, Any]]]:
    rows: list[dict[str, Any]] = []
    weak_cases: list[dict[str, Any]] = []
    for test in load_tests():
        documents = fetch_context(test.question, k=k or settings.RETRIEVAL_K)
        relevances = []
        reciprocal_rank = 0.0
        retrieved_sources = []
        retrieved_text = "\n".join(document.page_content for document in documents).lower()
        keyword_hits = sum(1 for keyword in test.keywords if keyword.lower() in retrieved_text)

        for rank, document in enumerate(documents, start=1):
            source = document.metadata.get("source", "")
            retrieved_sources.append(source)
            relevant = int(_matches(document.page_content, source, test))
            relevances.append(relevant)
            if relevant and reciprocal_rank == 0:
                reciprocal_rank = 1 / rank

        source_or_keyword_hit = any(relevances) or keyword_hits > 0
        row = {
            "question": test.question,
            "category": test.category,
            "mrr": reciprocal_rank,
            "ndcg": _ndcg(relevances),
            "keyword_coverage": keyword_hits / max(len(test.keywords), 1),
            "hit": source_or_keyword_hit,
            "retrieved_sources": ", ".join(retrieved_sources),
        }
        rows.append(row)
        if not source_or_keyword_hit or row["keyword_coverage"] < 0.5:
            weak_cases.append(row)

    detail = pd.DataFrame(rows)
    by_category = detail.groupby("category", as_index=False).agg(
        mrr=("mrr", "mean"),
        ndcg=("ndcg", "mean"),
        keyword_coverage=("keyword_coverage", "mean"),
        hit_rate=("hit", "mean"),
    )
    return detail, by_category, weak_cases
