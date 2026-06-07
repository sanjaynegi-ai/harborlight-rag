# Business Requirements

## Functional Requirements

- Answer employee questions using only approved documents.
- Cite source filenames in every answer.
- Show retrieved context in the teaching UI.
- Refuse when context is insufficient.
- Allow retrieval k to be changed.

## Non-Functional Requirements

- Local Docker Desktop deployment.
- Clear separation of ingestion, retrieval, and evaluation.
- Beginner-readable code.
- Repeatable reset and reindex process.

## Data Requirements

- Markdown files under `knowledge_base/`.
- Required metadata: source, category, filename, document path.
- Documents must be synthetic, approved, current, and non-conflicting.

## Evaluation Requirements

- At least 40 golden tests.
- Category-level retrieval and answer metrics.
- Weak case reporting.

## Security Requirements

- No committed secrets.
- Source citations.
- Refusal behavior for unsupported questions.
- Clear plan for access control before production.

## Operational Requirements

- Docker Compose services for ChromaDB, ingestion, RAG app, and evaluator.
- Persistent ChromaDB volume.
- Reindexing and rollback documented.

## Assumptions

- Learners have Docker Desktop, uv, and an OpenAI API key.
- The fictional knowledge base is the only approved source.

## Constraints

- Use uv only.
- Use Python 3.13.1.
- Keep ChromaDB separate from the app.

## Open Questions

- What production identity provider would enforce document-level access?
- What telemetry stack would HarborLight use?
- What approval workflow would publish new knowledge files?
