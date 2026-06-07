# Docker Deployment

```text
docker compose
  |
  +-- chromadb:8000
  |     volume: chroma_data
  |
  +-- ingestion
  |     command: uv run python -m ingestion.ingest
  |
  +-- rag-app:7860
  |     command: uv run python -m rag_app.app
  |
  +-- evaluator:7861
        command: uv run python -m evaluation.evaluator_app
```
