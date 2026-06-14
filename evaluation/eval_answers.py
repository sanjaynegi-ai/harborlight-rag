from __future__ import annotations

import json
from typing import Any

import pandas as pd
from langchain_openai import ChatOpenAI

from config import settings
from evaluation.eval_retrieval import load_tests
from rag_app.answer import answer_question, format_context
from rag_app.prompts import EVALUATION_JUDGE_PROMPT


def _fallback_judgment(feedback: str) -> dict[str, Any]:
    return {
        "accuracy": 0,
        "completeness": 0,
        "groundedness": 0,
        "relevance": 0,
        "feedback": feedback,
    }


def judge_answer(question: str, answer: str, reference_answer: str, context: str) -> dict[str, Any]:
    settings.require_openai_api_key()
    model = ChatOpenAI(model=settings.CHAT_MODEL, temperature=0)
    response = model.invoke(
        [
            {"role": "system", "content": EVALUATION_JUDGE_PROMPT},
            {
                "role": "user",
                "content": (
                    f"Question: {question}\n\nGenerated answer: {answer}\n\n"
                    f"Reference answer: {reference_answer}\n\nRetrieved context: {context}"
                ),
            },
        ]
    )
    try:
        data = json.loads(str(response.content))
    except json.JSONDecodeError:
        return _fallback_judgment(f"Judge returned non-JSON: {response.content}")
    return data


def evaluate_answers(limit: int | None = None, k: int | None = None) -> tuple[pd.DataFrame, pd.DataFrame]:
    rows = []
    tests = load_tests()
    if limit:
        tests = tests[:limit]
    for test in tests:
        answer, documents = answer_question(test.question, k=k or settings.RETRIEVAL_K)
        judgment = judge_answer(test.question, answer, test.reference_answer, format_context(documents))
        rows.append(
            {
                "question": test.question,
                "category": test.category,
                "answer": answer,
                "reference_answer": test.reference_answer,
                **judgment,
            }
        )
    detail = pd.DataFrame(rows)
    score_columns = ["accuracy", "completeness", "groundedness", "relevance"]
    by_category = detail.groupby("category", as_index=False)[score_columns].mean()
    return detail, by_category
