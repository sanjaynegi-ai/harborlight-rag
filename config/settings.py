"""Central settings for ingestion, retrieval, evaluation, and apps."""

from __future__ import annotations

import os
from pathlib import Path

from dotenv import load_dotenv

load_dotenv()

PROJECT_ROOT = Path(__file__).resolve().parents[1]
KNOWLEDGE_BASE_PATH = PROJECT_ROOT / "knowledge_base"
EVALUATION_TESTS_PATH = PROJECT_ROOT / "evaluation" / "tests.jsonl"

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY", "")

CHROMA_HOST = os.getenv("CHROMA_HOST", "localhost")
CHROMA_PORT = int(os.getenv("CHROMA_PORT", "8000"))
CHROMA_COLLECTION = os.getenv("CHROMA_COLLECTION", "harborlight_docs")

CHAT_MODEL = os.getenv("CHAT_MODEL", "gpt-4.1-nano")
EMBEDDING_MODEL = os.getenv("EMBEDDING_MODEL", "text-embedding-3-large")

CHUNK_SIZE = int(os.getenv("CHUNK_SIZE", "700"))
CHUNK_OVERLAP = int(os.getenv("CHUNK_OVERLAP", "120"))
RETRIEVAL_K = int(os.getenv("RETRIEVAL_K", "6"))

APP_HOST = os.getenv("APP_HOST", "127.0.0.1")
RAG_APP_PORT = int(os.getenv("RAG_APP_PORT", "7860"))
EVALUATOR_PORT = int(os.getenv("EVALUATOR_PORT", "7861"))


def chroma_url() -> str:
    return f"http://{CHROMA_HOST}:{CHROMA_PORT}"


def require_openai_api_key() -> None:
    if not OPENAI_API_KEY or OPENAI_API_KEY == "replace-with-your-key":
        raise RuntimeError("OPENAI_API_KEY is missing. Copy .env.example to .env and set a real key.")
