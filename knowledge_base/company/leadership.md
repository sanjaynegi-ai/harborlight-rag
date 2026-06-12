# Leadership

HarborLight Analytics is led by a cross-functional executive team.

- Mara Chen is Chief Executive Officer and co-founder.
- Dev Patel is Chief Technology Officer and owns AI platform strategy.
- Lena Ortiz is Chief Product Officer and owns product roadmap governance.
- Priya Raman is Chief Customer Officer and owns customer success escalation.
- Tomasz Zielinski is Chief Security Officer and owns security review and incident communication.
- Ellen Brooks is VP of Sustainable Logistics Research and owns methodology reviews for emissions calculations.

The executive sponsor for the internal RAG assistant is Lena Ortiz. The technical sponsor is Dev Patel.

Leadership requires that the assistant cite source filenames and refuse unsupported questions.

## Decision Rights

Mara Chen approves company-wide assistant rollout messaging. Dev Patel approves model and platform choices. Lena Ortiz approves product scope and acceptance thresholds. Priya Raman approves customer-success workflows and escalation language. Tomasz Zielinski approves security controls, audit requirements, and incident communication wording. Ellen Brooks approves sustainability methodology language for EmissionsLens answers.

The RAG assistant steering group meets on the first Tuesday of each month during the pilot. The group reviews evaluation metrics, weak cases, missing documents, and user feedback. A release decision requires approval from Lena Ortiz, Dev Patel, and Tomasz Zielinski.

## Named Operational Owners

For the teaching project, the simulated ownership roster is:

- Product owner: Lena Ortiz.
- AI engineering owner: Dev Patel.
- Evaluation owner: Austin evaluation engineering team.
- Knowledge base owner: Priya Raman for customer files and Lena Ortiz for product files.
- Security reviewer: Tomasz Zielinski.
- Emissions methodology reviewer: Ellen Brooks.

If a generated answer conflicts with an approved source document, the incident is assigned first to AI Engineering for diagnosis and then to the relevant document owner for source correction if the document is wrong.

## Escalation Expectations

Severity 1 customer-facing answer failures are reviewed within one business day. A Severity 1 answer failure is any assistant answer that invents a contractual obligation, exposes confidential data, or contradicts an approved policy in a way that could affect customer communication.

Leadership requires a written remediation note for Severity 1 answer failures. The note must include the question, retrieved sources, model, collection version, prompt version, root cause, and corrective action.

## Steering Group Operating Model

The RAG assistant steering group includes Lena Ortiz, Dev Patel, Tomasz Zielinski, Priya Raman, Ellen Brooks, the Austin evaluation lead, and a rotating customer success representative. The group uses a fixed agenda: review new source documents, review golden dataset changes, inspect weak cases, approve or reject tuning experiments, and assign owners for unresolved risks.

A release vote requires three approvals: product scope from Lena Ortiz, platform readiness from Dev Patel, and security readiness from Tomasz Zielinski. Ellen Brooks has veto authority over EmissionsLens methodology language when an answer could be reused in sustainability reporting preparation.

## Decision Escalation Examples

If retrieval misses the right customer file, the issue is assigned to AI Engineering. If the retrieved customer file contains stale contract language, the issue is assigned to the customer success document owner. If the answer exposes or invents confidential information, Tomasz Zielinski opens a Severity 1 generated-answer review.

If a product answer sounds plausible but cannot be traced to a product document, Lena Ortiz treats it as a scope problem rather than a writing problem. Product scope must be documented before prompts are tuned around it.

## Approval Artifacts

Leadership expects every release packet to contain the problem statement, requirements summary, stakeholder ownership map, data readiness checklist, golden dataset summary, architecture decision log, baseline evaluation report, Docker deployment proof, monitoring plan, governance review, and production readiness checklist.

The minimum release packet must name the collection version, embedding model, chat model, chunk size, chunk overlap, retrieval k, prompt version, and evaluator dataset file. Missing version information blocks release because future teams would not be able to reproduce the result.

## Communication Rules

Leadership communication about the assistant should avoid saying the system knows HarborLight policy. The approved wording is that the assistant retrieves approved documents and drafts grounded answers with source citations. Employees remain responsible for checking cited files before using answers in customer communication.

## Release Accountability

Lena Ortiz owns the final release recommendation, but she cannot approve release alone. Dev Patel must confirm that ingestion, retrieval, and model configuration are reproducible. Tomasz Zielinski must confirm that secrets, audit expectations, and refusal boundaries are acceptable for the pilot.

Priya Raman confirms that customer success workflows are realistic. Ellen Brooks confirms that emissions methodology wording does not overstate what EmissionsLens can certify. The Austin evaluation lead confirms that baseline metrics and weak cases are documented.

## Teaching Deep Dive

This document is also used to teach students how enterprise RAG answers depend on document purpose. A company document usually provides organizational context, official boundaries, ownership, and operating norms. It should not be treated as a substitute for a customer contract, product specification, incident report, or policy.

When a learner asks an assistant question, this document can supply framing facts, but the answer may still require a second source. For example, a question about who owns a review may cite leadership, while a question about how that review affects a customer may also cite the customer file. A question about an office role may cite offices, while a support obligation still requires the support policy.

Students should notice that broad company documents are high-value retrieval targets but can also cause overgeneralization. A good RAG answer uses the broad document to orient the answer and then cites the specific source that proves the operational detail. This is one reason the project keeps metadata for source, category, filename, and document path.

## Retrieval Risk Notes

Company documents often contain terms that appear in many questions: assistant, support, customer, evaluation, owner, and release. Those terms can make retrieval noisy. The evaluation set therefore includes questions that require the assistant to select a narrower document even when company text is also relevant.

If company chunks dominate retrieval, students should inspect chunk size, overlap, and metadata filtering. They should not immediately rewrite the answer prompt. Retrieval quality should be diagnosed before answer style.

## Operational Examples

A customer success manager preparing for a call might ask for the correct escalation owner, the accepted release boundary, or the right demo talking point. The answer should cite the company document for those broad facts and avoid inventing undocumented details such as private employee schedules, unlisted locations, or customer-specific commitments.

An onboarding trainer might ask why the assistant refuses salary, credential, or private pricing questions. The answer should explain that source documents do not contain those facts and that safe refusal is an intended behavior.

## Maintenance Notes

Company documents should be reviewed after leadership changes, office changes, governance changes, or release-scope changes. If a company document changes, ingestion must be rerun because source text has changed. After reingestion, the team should run at least the direct_fact, multi_doc, and insufficient_context portions of the golden dataset.
