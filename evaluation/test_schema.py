from __future__ import annotations

from pydantic import BaseModel, Field


class TestQuestion(BaseModel):
    __test__ = False

    question: str
    keywords: list[str]
    reference_answer: str
    category: str
    expected_sources: list[str] = Field(default_factory=list)
