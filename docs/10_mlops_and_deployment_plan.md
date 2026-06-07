# MLOps and Deployment Plan

- Build separate Docker images for ingestion, RAG app, and evaluator.
- Run ChromaDB as a separate service with the `chroma_data` volume.
- Treat ingestion as a batch job that exits after indexing.
- Treat the RAG app and evaluator as long-running services.
- Store secrets in `.env` locally and a secret manager in production.
- Version knowledge base, collection name, embedding model, prompt, and evaluation dataset.
- Reindex when documents, chunking, overlap, or embedding model changes.
- Roll back by restoring a previous collection version and prompt version.
- Keep separate release cycles for ingestion and retrieval.
