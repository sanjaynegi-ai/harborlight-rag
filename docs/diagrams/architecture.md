# Architecture Diagram

```text
knowledge_base/*.md
        |
        v
ingestion container
  - load
  - validate
  - chunk
  - embed
        |
        v
ChromaDB service with chroma_data volume
        |
        +------------------+
        |                  |
        v                  v
RAG app service       evaluator service
  - retrieve            - retrieval metrics
  - prompt              - answer judge
  - cite sources        - weak cases
```
