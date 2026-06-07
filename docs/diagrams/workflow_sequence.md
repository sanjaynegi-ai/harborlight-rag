# Workflow Sequence

```text
Data Engineering -> Knowledge Base: publish approved Markdown
AI Engineering -> Ingestion Job: run reindex
Ingestion Job -> ChromaDB: rebuild collection
Employee -> RAG App: ask question
RAG App -> ChromaDB: retrieve top-k chunks
RAG App -> OpenAI: send grounded prompt
RAG App -> Employee: answer with Sources line
QA -> Evaluator: run golden dataset
Evaluator -> Product Owner: category metrics and weak cases
```
