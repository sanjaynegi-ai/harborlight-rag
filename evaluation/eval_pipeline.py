from __future__ import annotations

from evaluation.eval_answers import evaluate_answers
from evaluation.eval_retrieval import evaluate_retrieval


def run_full_evaluation(answer_limit: int | None = None, k: int | None = None) -> dict:
    retrieval_detail, retrieval_by_category, weak_cases = evaluate_retrieval(k=k)
    answer_detail, answer_by_category = evaluate_answers(limit=answer_limit, k=k)
    return {
        "retrieval_detail": retrieval_detail,
        "retrieval_by_category": retrieval_by_category,
        "weak_cases": weak_cases,
        "answer_detail": answer_detail,
        "answer_by_category": answer_by_category,
    }
