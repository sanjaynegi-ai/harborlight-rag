# HarborLight RAG Production Implementation Guide

This guide is the master chronological walkthrough. Follow it from Phase 0 through Phase 21. Supporting documents in `docs/` deepen each phase, but this file is the spine of the project.

## Phase 0: Orientation

Goal: understand what students will build: a production-style internal RAG assistant for HarborLight Analytics.

Why it matters in production: enterprise RAG is a lifecycle, not a single chatbot script. Teams must understand business goals, data ownership, evaluation, deployment, monitoring, and governance before release.

Inputs required: `README.md`, `docs/01_problem_statement.md`, and this repository.

Owner role: instructor and student project team.

Activities:
- Read `README.md`.
- Read `docs/01_problem_statement.md`.
- Identify three workflows: ingestion, retrieval, and evaluation.

Deliverables: shared understanding of the project and its learning goals.

Quality gate: students can explain why ingestion, retrieval, and evaluation are separate.

Common mistakes: starting with prompts before business requirements; rebuilding the vector DB from the app; tuning without a golden dataset.

Student demo talking points: "This project models a real RAG engagement, not only a chat UI."

## Phase 1: Business Problem Discovery

Goal: define the business problem, target users, pain points, expected benefits, and scope.

Why it matters in production: unclear scope causes unsafe answers and endless tuning.

Inputs required: stakeholder interviews and `docs/01_problem_statement.md`.

Owner role: product owner with business owner.

Activities:
- Define target users: HarborLight employees in sales, support, product, engineering, and leadership.
- Clarify in-scope documents: overview, leadership, culture, offices, products, customers, policies, incidents.
- Clarify out-of-scope behavior: legal advice, unapproved documents, personal data lookup, and speculation.

Deliverables: approved problem statement.

Quality gate: product owner agrees on what the assistant should and should not answer.

Common mistakes: saying "answer anything about the company" without source boundaries.

Student demo talking points: "The assistant only answers from approved internal documents and cites filenames."

## Phase 2: Requirements Documentation

Goal: document functional, non-functional, security, evaluation, operational requirements, constraints, assumptions, and open questions.

Why it matters in production: requirements become the basis for tests, acceptance thresholds, and governance review.

Inputs required: `docs/02_business_requirements.md`.

Owner role: product owner, AI engineer, QA, security owner.

Activities:
- Document answer behavior, citations, refusal behavior, latency target, and evaluation thresholds.
- Document assumptions such as Markdown source format and OpenAI API availability.

Deliverables: business requirements document.

Quality gate: requirements are testable or explicitly marked as open questions.

Commands: none.

Common mistakes: writing vague requirements such as "answers should be good."

Student demo talking points: "Evaluation requirements are written before tuning."

## Phase 3: Stakeholders and Ownership

Goal: assign ownership.

Why it matters in production: RAG failures often happen between teams, especially when nobody owns data freshness or golden answers.

Inputs required: `docs/03_stakeholders_and_ownership.md`.

Owner role: delivery lead.

Activities:
- Data Engineering owns raw knowledge source availability and refresh process.
- AI Engineering owns chunking, embeddings, retrieval, prompts, and evaluation implementation.
- Domain Experts own truth validation and golden answers.
- QA owns regression testing.
- MLOps owns containerization, deployment, secrets, and monitoring.

Deliverables: RACI-style ownership table.

Quality gate: every workflow has a named owner.

Common mistakes: asking AI engineers to certify business truth alone.

Student demo talking points: "Ownership is part of production readiness."

## Phase 4: Discovery Workshop

Goal: run realistic discovery Q&A before implementation.

Why it matters in production: discovery reveals document gaps, access limits, risks, and success criteria.

Inputs required: `docs/04_discovery_questions.md`.

Owner role: product owner and AI engineer.

Activities:
- Ask what documents exist, who owns them, whether they are approved, how often they change, whether access restrictions exist, what questions are expected, what the assistant should refuse, what a correct answer means, acceptable latency, and risks of wrong answers.

Deliverables: discovery notes and decisions.

Quality gate: unanswered questions are tracked.

Common mistakes: treating discovery as optional.

Student demo talking points: "The workshop protects the system from the wrong problem."

## Phase 5: Data Readiness and Knowledge Base Handoff

Goal: confirm the knowledge base is ready before ingestion.

Why it matters in production: weak source data creates weak RAG systems.

Inputs required: `docs/05_data_readiness_checklist.md`.

Owner role: Data Engineering with domain experts.

Activities:
- Check format, metadata, versioning, duplicates, conflicts, deprecated documents, missing owners, refresh cadence, confidentiality labels, and quality.

Deliverables: approved knowledge base handoff.

Quality gate: documents have owners, status, and no unresolved conflicts.

Common mistakes: indexing draft or conflicting documents.

Student demo talking points: "Implementation starts only after data readiness."

## Phase 6: Golden Dataset Planning

Goal: define the golden dataset before serious tuning.

Why it matters in production: without a benchmark, tuning is guesswork.

Inputs required: `docs/06_golden_dataset_plan.md` and `evaluation/tests.jsonl`.

Owner role: domain experts validate truth, AI engineer formats tests, QA runs regression, product owner approves thresholds.

Activities:
- Define each test with question, keywords, reference answer, category, and expected sources.
- Include at least 40 tests.
- Include at least five tests per category: `direct_fact`, `multi_doc`, `temporal`, `comparison`, `numerical`, `insufficient_context`.

Deliverables: validated `evaluation/tests.jsonl`.

Quality gate: domain experts approve reference answers and expected sources.

Common mistakes: writing only easy direct questions.

Student demo talking points: "The golden dataset is built before optimization."

## Phase 7: Architecture and Design

Goal: design the RAG system.

Why it matters in production: architecture choices define ownership, failure modes, and release cycles.

Inputs required: `docs/07_solution_design.md`, `docs/08_architecture_decisions.md`, `docs/diagrams/architecture.md`.

Owner role: AI engineer and MLOps engineer.

Architecture:

```text
Markdown company documents
        |
        v
Ingestion container
        |
        v
Document loader
        |
        v
Text splitter
        |
        v
Embedding model
        |
        v
ChromaDB container
        |
        v
RAG app container
        |
        v
Retriever + user question
        |
        v
LLM answer with cited sources
```

Activities:
- Separate ingestion and RAG app.
- Use ChromaDB as a separate service.
- Keep evaluation separate.
- Define metadata: `source`, `category`, `filename`, `document_path`, `chunk_index`.
- Select chunk size, overlap, embedding model, retrieval k, prompting, citations, and refusal behavior.

Deliverables: solution design and ADRs.

Quality gate: the RAG app cannot rebuild vectors automatically.

Common mistakes: coupling ingestion to user traffic.

Student demo talking points: "Batch indexing and online retrieval have different owners and release cycles."

## Phase 8: Test Strategy Before Coding

Goal: design tests and evaluation before implementation.

Why it matters in production: RAG quality needs regression evaluation, not only unit tests.

Inputs required: `docs/09_test_strategy.md`.

Owner role: QA and AI engineer.

Activities:
- Use evaluation-first development.
- Add unit tests for loading, chunking, metadata.
- Add integration tests for ingestion and RAG.
- Evaluate retrieval before answer generation.
- Add smoke tests for Docker service files and settings.

Deliverables: test strategy and acceptance criteria.

Quality gate: tests cover code behavior and quality metrics.

Commands: `uv run pytest`

Common mistakes: relying only on manual chat examples.

Student demo talking points: "Pure TDD is hard for RAG quality, but evaluation-first is mandatory."

## Phase 9: Project Setup

Goal: prepare local configuration.

Why it matters in production: repeatable setup reduces environment drift.

Inputs required: Docker Desktop, uv, OpenAI API key.

Owner role: student developer.

Activities and commands:

macOS/Linux:

```bash
cp .env.example .env
docker compose build
```

Windows PowerShell:

```powershell
Copy-Item .env.example .env
docker compose build
```

Deliverables: `.env` file and built Docker images.

Quality gate: Docker Desktop is running and images build.

Common mistakes: leaving `OPENAI_API_KEY=replace-with-your-key`; using `CHROMA_HOST=chromadb` for local non-Docker scripts.

Student demo talking points: "uv is the only Python package manager used."

## Phase 10: Knowledge Base Creation

Goal: create original Markdown knowledge base documents.

Why it matters in production: source documents are the truth boundary.

Inputs required: `knowledge_base/`.

Owner role: Data Engineering and domain experts.

Activities:
- Create company, product, customer, policy, and incident documents.
- Include direct, multi-document, temporal, comparison, numerical, and insufficient-context support.
- Avoid any previous tutorial names.

Deliverables: approved synthetic HarborLight knowledge base.

Quality gate: each file is original, internally consistent, and suitable for evaluation.

Common mistakes: documents too thin to support multi-hop questions.

Student demo talking points: "The KB is synthetic but shaped like an enterprise handoff."

## Phase 11: Implement Ingestion Workflow

Goal: build modular batch ingestion.

Why it matters in production: indexing is a controlled data operation, not a side effect of chat.

Inputs required: `ingestion/`, `config/settings.py`, `.env`, `knowledge_base/`.

Owner role: Data Engineering and AI Engineering.

Activities:
- Load `.env`.
- Recursively load Markdown files using `DirectoryLoader` with `glob="**/*.md"` and `TextLoader`.
- Attach metadata.
- Validate required metadata.
- Split with `RecursiveCharacterTextSplitter`.
- Embed with `OpenAIEmbeddings`.
- Connect to ChromaDB.
- Clear and rebuild the configured collection.
- Print document count, chunk count, model, collection, host, and port.

Commands:

```bash
uv run python -m ingestion.ingest
docker compose run --rm ingestion
```

Deliverables: indexed ChromaDB collection.

Quality gate: ingestion fails clearly for missing KB, no Markdown, missing API key, unreachable ChromaDB, or metadata errors.

Common mistakes: using stale vectors after document changes.

Student demo talking points: "Reindexing is explicit and repeatable."

## Phase 12: Implement RAG Retrieval Workflow

Goal: build the chat app.

Why it matters in production: online retrieval must be fast, grounded, and separate from indexing.

Inputs required: `rag_app/`.

Owner role: AI Engineering and application team.

Activities:
- Connect to existing ChromaDB collection.
- Retrieve chunks for a question.
- Include filenames in context.
- Use a prompt that answers only from context, refuses insufficient context, and cites sources.
- Return answer text and retrieved documents.
- Provide Gradio chat UI with retrieval k and context visibility controls.

Commands:

```bash
uv run python -m rag_app.app
docker compose up rag-app
```

Deliverables: working RAG assistant.

Quality gate: the app never rebuilds the vector database.

Common mistakes: hiding retrieved context from learners.

Student demo talking points: "The UI shows how retrieval shapes the answer."

## Phase 13: Implement Evaluation Workflow

Goal: measure retrieval and answer quality.

Why it matters in production: evaluation turns RAG improvement into a controlled experiment.

Inputs required: `evaluation/`, `evaluation/tests.jsonl`.

Owner role: AI Engineering, QA, and domain experts.

Activities:
- Validate test schema.
- Compute MRR, nDCG, keyword coverage, hit rate, category metrics, and weak cases.
- Use LLM-as-judge for accuracy, completeness, groundedness, relevance, and feedback.
- Show configuration, retrieval evaluation, answer evaluation, category charts/tables, weak cases, notes, and suggested tuning changes.

Commands:

```bash
uv run python -m evaluation.evaluator_app
docker compose up evaluator
```

Deliverables: evaluation dashboard.

Quality gate: baseline evaluation is run before tuning.

Common mistakes: improving one example while hurting a category.

Student demo talking points: "We tune from metrics, not vibes."

## Phase 14: Dockerization

Goal: create separate Docker images and Compose services.

Why it matters in production: containerized workflows mirror deployable services and batch jobs.

Inputs required: `docker/`, `docker-compose.yml`.

Owner role: MLOps/platform engineer.

Activities:
- Use official Chroma image with persistent volume.
- Build ingestion, RAG app, and evaluator images with Python 3.13 and uv.
- Use service name `chromadb` inside Docker.

Commands:

```bash
docker compose build
```

Deliverables: Dockerized local stack.

Quality gate: images build and services start.

Common mistakes: using local `localhost` inside containers.

Student demo talking points: "ChromaDB is infrastructure; ingestion is a job; apps are services."

## Phase 15: Local Deployment on Docker Desktop

Goal: run the system locally.

Why it matters in production: deployment steps must be repeatable.

Commands:

```bash
docker compose build
docker compose up -d chromadb
docker compose run --rm ingestion
docker compose up rag-app
docker compose up evaluator
```

Stop:

```bash
docker compose down
```

Full reset:

```bash
docker compose down -v
docker compose build
docker compose up -d chromadb
docker compose run --rm ingestion
```

Quality gate: RAG app opens on `http://localhost:7860`, evaluator opens on `http://localhost:7861`.

Common mistakes: forgetting to run ingestion after volume reset.

Student demo talking points: "Windows and macOS both use Docker Desktop and the same Compose commands."

## Phase 16: Validation and Testing

Goal: run automated tests.

Why it matters in production: tests catch regressions in code paths and configuration.

Commands:

```bash
uv run pytest
docker compose run --rm rag-app uv run pytest
```

Testing requirements:
- Document loader unit test.
- Metadata unit test.
- Chunking unit test.
- Retriever unit test.
- Ingestion integration test.
- RAG pipeline integration test.
- Docker service smoke test.

Quality gate: local tests pass; external tests either pass or skip with clear reason.

Common mistakes: running integration tests without ChromaDB or API key.

Student demo talking points: "Unit tests protect code; evaluation protects RAG quality."

## Phase 17: Evaluation and Iteration

Goal: run baseline evaluation and controlled experiments.

Why it matters in production: every tuning change must be measured.

Activities:
1. Change config.
2. Rerun ingestion if chunking, embedding model, or documents changed.
3. Run retrieval evaluation.
4. Run answer evaluation.
5. Compare category-level results.
6. Document findings.

Experiments:
- Chunk size 300 vs 700 vs 1000.
- Overlap 50 vs 120 vs 200.
- Retrieval k 3 vs 6 vs 10.
- Strict citations vs relaxed prompt.
- Embedding model change.
- Insufficient-context prompt improvement.

Quality gate: no change is accepted without before/after results.

Common mistakes: rerunning ingestion for prompt-only changes; not rerunning ingestion after chunking changes.

Student demo talking points: "If source documents, chunking, overlap, or embedding model changes, reindex."

## Phase 18: Monitoring and Observability

Goal: define production monitoring.

Why it matters in production: released RAG systems need quality, cost, latency, and freshness visibility.

Inputs required: `docs/11_monitoring_observability_plan.md`.

Owner role: MLOps and AI Engineering.

Log:
- User question.
- Retrieved source filenames.
- Retrieval k.
- Similarity scores when available.
- Answer latency.
- LLM model.
- Token usage and cost estimate when available.
- Insufficient-context responses.
- User feedback.

Track:
- Retrieval quality.
- Answer groundedness.
- Hallucination reports.
- No-answer rate.
- Latency.
- Cost.
- Document freshness.
- Collection version.

Quality gate: monitoring fields are defined before release.

Common mistakes: treating logs as an afterthought.

Student demo talking points: "Production RAG has a feedback loop."

## Phase 19: Governance, Security, and Risk

Goal: prepare responsible release controls.

Why it matters in production: internal assistants can expose stale, confidential, or wrong information.

Inputs required: `docs/12_governance_and_risk_plan.md`.

Owner role: security/governance owner.

Activities:
- Define citations, refusal behavior, access control, PII handling, secrets management, audit logs, human review, model/version traceability, KB versioning, data retention, and incident response.

Deliverables: governance and risk plan.

Quality gate: security review is complete.

Common mistakes: relying on prompts as the only safety control.

Student demo talking points: "Grounded answers and citations reduce risk but do not replace governance."

## Phase 20: Production Readiness Review

Goal: decide go/no-go.

Why it matters in production: release requires evidence.

Inputs required: `docs/13_production_readiness_checklist.md`.

Owner role: product owner, AI Engineering, QA, MLOps, security.

Verify:
- Requirements satisfied.
- Knowledge base approved.
- Golden dataset approved.
- Baseline evaluation complete.
- Known weak cases documented.
- Docker deployment works.
- Logs and monitoring defined.
- Security review complete.
- Rollback/reindex process documented.
- Owners assigned.

Deliverables: go/no-go decision.

Quality gate: all critical checklist items pass.

Common mistakes: releasing with undocumented weak cases.

Student demo talking points: "A demo is not production readiness."

## Phase 21: Final Student Demo

Goal: present the complete lifecycle and working system.

Why it matters in production: stakeholders need both technical evidence and business context.

Students should present:
1. Business problem.
2. Requirements.
3. Data readiness.
4. Golden dataset.
5. Architecture.
6. Ingestion workflow.
7. RAG workflow.
8. Evaluation dashboard.
9. Docker deployment.
10. Monitoring/governance plan.
11. Lessons learned and improvements.

Quality gate: the demo shows both software and operating model.

Common mistakes: demoing only the chat app.

Student demo talking points: "The final artifact is an end-to-end production-style RAG engagement."
