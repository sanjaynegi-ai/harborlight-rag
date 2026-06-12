from __future__ import annotations

from langchain_core.documents import Document

REQUIRED_METADATA = {"source", "category", "filename", "document_path"}


def validate_documents(documents: list[Document]) -> None:
    if not documents:
        raise RuntimeError("Document validation failed: no documents were provided.")

    failures: list[str] = []
    for index, document in enumerate(documents):
        missing = REQUIRED_METADATA - set(document.metadata)
        if missing:
            failures.append(f"document[{index}] missing metadata: {sorted(missing)}")
        if not document.page_content.strip():
            failures.append(f"document[{index}] has empty content: {document.metadata.get('source', 'unknown')}")

    if failures:
        joined = "\n".join(failures)
        raise RuntimeError(f"Document validation failed:\n{joined}")