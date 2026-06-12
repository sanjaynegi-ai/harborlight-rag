from __future__ import annotations

from pathlib import Path
# import sys

# PROJECT_ROOT = Path(__file__).resolve().parents[1]
# if str(PROJECT_ROOT) not in sys.path:
#     sys.path.insert(0, str(PROJECT_ROOT))

from langchain_community.document_loaders import DirectoryLoader, TextLoader
from langchain_core.documents import Document

from config import settings


def _category_from_path(path: Path) -> str:
    try:
        return path.relative_to(settings.KNOWLEDGE_BASE_PATH).parts[0]
    except (ValueError, IndexError):
        return "unknown"


def load_markdown_documents() -> list[Document]:
    if not settings.KNOWLEDGE_BASE_PATH.exists():
        raise FileNotFoundError(f"Knowledge base directory is missing: {settings.KNOWLEDGE_BASE_PATH}")

    loader = DirectoryLoader(
        str(settings.KNOWLEDGE_BASE_PATH),
        glob="**/*.md",
        loader_cls=TextLoader,
        loader_kwargs={"encoding": "utf-8"},
        show_progress=False,
    )
    documents = loader.load()
    if not documents:
        raise RuntimeError(f"No Markdown files found in {settings.KNOWLEDGE_BASE_PATH}")

    enriched: list[Document] = []
    for document in documents:
        source_path = Path(document.metadata["source"]).resolve()
        relative_path = source_path.relative_to(settings.KNOWLEDGE_BASE_PATH)
        metadata = {
            **document.metadata,
            "source": relative_path.as_posix(),
            "category": _category_from_path(source_path),
            "filename": source_path.name,
            "document_path": relative_path.as_posix(),
        }
        enriched.append(Document(page_content=document.page_content, metadata=metadata))
    return enriched


# if __name__ == "__main__":
#     docs = load_markdown_documents()

#     print(f"Loaded {len(docs)} documents")

#     for doc in docs[:5]:
#         print("-" * 80)
#         print("Content preview:")
#         print(doc.page_content[:300])
#         print()
#         print("Metadata:")
#         print(doc.metadata)
