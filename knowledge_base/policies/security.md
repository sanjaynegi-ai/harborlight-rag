# Security Policy

Effective date: 2026-01-01.

HarborLight uses least-privilege access, encrypted transport, encrypted storage for customer data, and quarterly access reviews.

Security requirements:

- Production secrets must be stored in an approved secret manager.
- Support staff may access customer environments only through named support roles.
- Security incidents must be reported to the Chief Security Officer within one business day.
- Customer-facing incident summaries must cite affected product, impact, root cause, and follow-up action.
- The internal RAG assistant must not expose secrets or answer from unapproved documents.

Security audit logs are retained for 2 years according to `policies/data_retention.md`.

## RAG Security Controls

The internal RAG assistant must load secrets only from environment variables or an approved secret manager. API keys must never be written into Markdown source documents, evaluation datasets, logs, screenshots, or Docker images.

Production retrieval must support role-aware filtering before the assistant is made available beyond the teaching pilot. A user should retrieve only documents they are allowed to read outside the assistant.

## Incident Classification

A security incident is Severity 1 if it exposes secrets, customer confidential data, or unauthorized personal data. It is Severity 2 if it exposes internal-only but non-secret operational data to the wrong employee group. It is Severity 3 if it creates a near miss with no confirmed exposure.

Security incidents involving generated answers require preservation of the question, retrieved sources, answer, model name, prompt version, collection version, and user feedback.

## Evaluation Notes

Questions about passwords, credentials, home addresses, or private compensation should receive insufficient-context or refusal-style answers unless an approved policy explicitly covers the safe high-level process.

## Audit Review Cadence

During the pilot, audit samples are reviewed every two weeks. The sample includes at least ten supported answers, five insufficient-context responses, and any user-flagged answer. The reviewer checks that sources were cited, retrieved files were appropriate, and unsupported facts were not invented.

Production audit review would also verify that user identity and document permissions were applied before retrieval. This teaching project documents that requirement but does not implement role-aware filtering.

## Access Control Expectations

The teaching project documents role-aware retrieval as a production requirement but does not implement it. A production assistant would filter documents before retrieval based on user identity, group membership, document confidentiality, and customer account assignment.

Access control must happen before chunks are sent to the LLM. Hiding a source citation after retrieval is not sufficient because the model may already have seen restricted text.

## Secret Handling

OpenAI API keys, Chroma credentials, database passwords, and service tokens must never appear in Markdown source files, JSONL evaluation rows, screenshots, logs, Docker images, or demo transcripts. Secrets are loaded from environment variables in the teaching project and from an approved secret manager in production.

If a secret is accidentally committed to the knowledge base, the response is not only to delete the Markdown line. The secret must be rotated, the vector collection rebuilt, logs reviewed, and incident handling documented.

## Generated Answer Incidents

A generated-answer incident is opened when the assistant invents a contractual obligation, exposes restricted information, or cites a source that does not support the claim. The incident record includes the question, retrieved chunks, answer, model, prompt version, collection version, user identity if available, and reviewer decision.

Security review distinguishes missing context from unsafe disclosure. A correct refusal for unsupported salary, address, credential, or private pricing questions is counted as safe behavior.

## Audit Sampling

Pilot audits include supported answers, insufficient-context answers, user-flagged answers, and answers involving customer obligations. Reviewers check citation correctness, source authorization assumptions, and whether the answer uses approved wording for sensitive topics.

## Teaching Deep Dive

This policy document teaches students how enterprise RAG systems answer rule-based questions. A policy file defines defaults, controls, approval paths, and boundaries. A customer file may override a default, but the override must be explicit. The assistant should never infer an exception from customer size, industry, region, or similarity to another customer.

Policy answers should be careful with verbs. The assistant may say a policy requires, allows, or prohibits something only when this file says so. If the policy only describes a review process or target, the assistant should not turn that into a penalty, refund, legal obligation, or guarantee.

## Cross-Document Use

Many correct answers require both this policy and another source. A support answer needs the customer support tier plus the policy response target. A retention answer may need the product retention default plus the customer override. A pricing answer may need list price, discount rule, and the customer-specific renewal clause.

Students should check whether the answer cites the source of each rule. A single citation is often not enough when the question combines customer-specific and policy-level facts.

## Evaluation Design Notes

Policy files support numerical questions, comparison questions, insufficient-context questions, and multi-document questions. They are ideal for testing whether the assistant refuses to invent legal penalties, actual paid prices, passwords, private addresses, or unsupported access-control details.

If policy chunks are too large, retrieval may include many unrelated rules. If chunks are too small, the rule and its exception-handling note may separate. Students should inspect retrieved chunks before changing prompts.

## Maintenance Notes

Policies should be reviewed after incidents, leadership decisions, regulatory changes, or operational changes. Any policy change requires reingestion, baseline evaluation, and a check for stale source text in ChromaDB. A policy deletion or replacement is not complete until old chunks are no longer retrievable.
