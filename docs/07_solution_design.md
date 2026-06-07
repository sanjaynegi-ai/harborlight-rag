# Solution Design

## Logical Architecture

Markdown documents are loaded by a batch ingestion container, split into chunks, embedded with OpenAI embeddings, and indexed in ChromaDB. The RAG app retrieves from ChromaDB and prompts an OpenAI chat model. The evaluator runs golden tests against the same retrieval and answer code.

## Component Responsibilities

- Ingestion: loading, validation, chunking, embedding, indexing.
- ChromaDB: vector storage and similarity search.
- RAG app: user interface, retrieval, answer generation, citations.
- Evaluator: retrieval metrics, answer judging, experiment notes.

## Data Flow

Documents move one way from `knowledge_base/` into ChromaDB through ingestion. User questions never trigger indexing.

## Runtime Flow

User question -> retriever -> chunks with metadata -> prompt -> answer with sources.

## Error Handling

The system fails clearly for missing API key, missing files, empty chunks, missing metadata, and unreachable ChromaDB.

## Source Citation Behavior

Context includes source filenames, and the prompt requires a short `Sources:` line.

## Refusal Behavior

If context is insufficient, the assistant says approved documents do not contain enough information.

## Tradeoffs

ChromaDB and Gradio are simple for teaching. Production might use managed vector search, role-aware retrieval, and enterprise observability.
