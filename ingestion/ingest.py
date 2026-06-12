from __future__ import annotations

from rich.console import Console

from config import settings
from ingestion.build_vector_db import rebuild_chroma_collection
from ingestion.chunk_documents import split_documents
from ingestion.load_documents import load_markdown_documents
from ingestion.validate_documents import validate_documents

console = Console()


def main() -> None:
    console.rule("HarborLight Knowledge Ingestion")
    console.print(f"Knowledge base: {settings.KNOWLEDGE_BASE_PATH}")
    console.print(f"ChromaDB: {settings.CHROMA_HOST}:{settings.CHROMA_PORT}")
    console.print(f"Collection: {settings.CHROMA_COLLECTION}")
    console.print(f"Embedding model: {settings.EMBEDDING_MODEL}")

    settings.require_openai_api_key()
    documents = load_markdown_documents()
    validate_documents(documents)
    chunks = split_documents(documents)
    rebuild_chroma_collection(chunks)

    console.print("\nIngestion complete.")
    console.print(f"Documents indexed: {len(documents)}")
    console.print(f"Chunks indexed: {len(chunks)}")
    console.print(f"Chunk size/overlap: {settings.CHUNK_SIZE}/{settings.CHUNK_OVERLAP}")


if __name__ == "__main__":
    main()