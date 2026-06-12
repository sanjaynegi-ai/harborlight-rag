from __future__ import annotations

import chromadb
from langchain_chroma import Chroma
from langchain_core.documents import Document
from langchain_openai import OpenAIEmbeddings

from config import settings


def get_vector_store() -> Chroma:
    settings.require_openai_api_key()
    client = chromadb.HttpClient(host=settings.CHROMA_HOST, port=settings.CHROMA_PORT)
    embeddings = OpenAIEmbeddings(model=settings.EMBEDDING_MODEL)
    return Chroma(
        client=client,
        collection_name=settings.CHROMA_COLLECTION,
        embedding_function=embeddings,
    )


def fetch_context(question: str, k: int | None = None) -> list[Document]:
    if not question.strip():
        return []
    vector_store = get_vector_store()
    return vector_store.similarity_search(question, k=k or settings.RETRIEVAL_K)


def fetch_context_with_scores(question: str, k: int | None = None) -> list[tuple[Document, float]]:
    if not question.strip():
        return []
    vector_store = get_vector_store()
    return vector_store.similarity_search_with_score(question, k=k or settings.RETRIEVAL_K)