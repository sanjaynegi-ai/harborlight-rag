from __future__ import annotations

import chromadb
from langchain_chroma import Chroma
from langchain_core.documents import Document
from langchain_openai import OpenAIEmbeddings

from config import settings


def rebuild_chroma_collection(chunks: list[Document]) -> None:
    settings.require_openai_api_key()
    if not chunks:
        raise RuntimeError("Cannot build vector database with zero chunks.")

    client = chromadb.HttpClient(host=settings.CHROMA_HOST, port=settings.CHROMA_PORT)
    try:
        client.delete_collection(settings.CHROMA_COLLECTION)
        print(f"Deleted existing collection: {settings.CHROMA_COLLECTION}")
    except Exception:
        print(f"No existing collection to delete: {settings.CHROMA_COLLECTION}")

    embeddings = OpenAIEmbeddings(model=settings.EMBEDDING_MODEL)
    vector_store = Chroma(
        client=client,
        collection_name=settings.CHROMA_COLLECTION,
        embedding_function=embeddings,
    )
    vector_store.add_documents(chunks)