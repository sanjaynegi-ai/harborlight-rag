# Architecture Decisions

## ADR 1: Use RAG Instead of Fine-Tuning

Context: answers must reflect changing internal documents.

Decision: use retrieval over approved documents.

Alternatives considered: fine-tuning, manual FAQ.

Consequences: source freshness depends on ingestion; answers can cite files.

## ADR 2: Use LangChain

Context: students need readable building blocks.

Decision: use LangChain loaders, splitters, vector store integration, and OpenAI wrappers.

Alternatives considered: direct SDK calls.

Consequences: less boilerplate, useful abstractions, dependency awareness required.

## ADR 3: Use ChromaDB

Context: local vector search is needed.

Decision: run ChromaDB as a Docker service.

Alternatives considered: FAISS, managed vector DB.

Consequences: simple local persistence and service separation.

## ADR 4: Separate Ingestion Workflow

Context: indexing is a batch data operation.

Decision: ingestion runs as its own job.

Alternatives considered: app rebuilds on startup.

Consequences: safer release cycle and explicit reindexing.

## ADR 5: Separate RAG App Workflow

Context: chat traffic should not mutate the vector store.

Decision: RAG app only retrieves and answers.

Alternatives considered: combined ingestion/chat service.

Consequences: clearer ownership and fewer runtime surprises.

## ADR 6: Use Docker Compose

Context: students need repeatable local deployment.

Decision: Compose defines ChromaDB, ingestion, RAG app, evaluator.

Alternatives considered: manual local processes.

Consequences: more production-like operations.

## ADR 7: Use Gradio

Context: learners need quick visual feedback.

Decision: use Gradio for chat and evaluation dashboards.

Alternatives considered: FastAPI plus custom frontend.

Consequences: faster teaching UI, less frontend complexity.

## ADR 8: Use uv

Context: environment setup should be modern and reproducible.

Decision: use uv only.

Alternatives considered: pip, Poetry, Conda.

Consequences: faster installs and one package workflow.

## ADR 9: Use Golden Dataset Before Tuning

Context: RAG tuning without metrics is unreliable.

Decision: create at least 40 tests before optimization.

Alternatives considered: manual chat spot checks.

Consequences: measurable iteration and regression safety.
