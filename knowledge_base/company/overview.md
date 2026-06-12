# HarborLight Analytics Overview

HarborLight Analytics builds AI tools for sustainable logistics companies. Its customers include ports, shipping companies, warehouses, and delivery fleets that want to reduce fuel usage, optimize routing, forecast delays, and report emissions.

The company was founded in 2019 in Seattle. Its internal mission statement is: "Make freight decisions cleaner, faster, and easier to trust."

HarborLight has five production products:

- RouteWise for routing optimization and fuel reduction.
- DockFlow for port berth and yard coordination.
- EmissionsLens for emissions reporting.
- FleetPulse for telematics monitoring.
- DelayCast for disruption and delay forecasting.

As of the 2026 internal planning cycle, HarborLight has 184 employees. The company serves 42 enterprise customers and 18 pilot customers.

All employee assistant answers must come from approved documents in this knowledge base and cite source filenames.

## Business Units

HarborLight organizes delivery work into four business units:

- Port Intelligence, which owns DockFlow adoption playbooks and terminal operating workflows.
- Fleet Optimization, which owns RouteWise and FleetPulse go-to-market enablement.
- Climate Reporting, which owns EmissionsLens methodology packaging and audit support.
- Predictive Operations, which owns DelayCast disruption forecasting and cross-product risk signals.

The business units share a single customer success operating model. Each enterprise customer has a customer success lead, a technical account lead, and a named escalation path for Severity 1 incidents.

## Assistant Scope Notes

The internal assistant is intended for employee enablement, onboarding, support preparation, and product-policy lookup. It is not an external customer-facing system. It must not answer questions about confidential roadmap items, employee compensation, private customer financials, or credentials unless those facts appear in approved source documents.

The assistant should prefer concise answers with filenames over long narrative summaries. When a question asks for a comparison, it should identify the source of each compared fact. When a question asks for a count or total, it should explain the arithmetic briefly.

## Knowledge Base Refresh Model

HarborLight treats the Markdown knowledge base as a controlled internal publishing channel. Product documents are reviewed quarterly. Customer contract summaries are reviewed at renewal or after a material amendment. Incident reports are added after closure and reviewed by the security owner when security policy is referenced.

The initial teaching collection version is `harborlight_docs_v1`. A production system would record collection version, embedding model, chunk configuration, prompt version, and golden dataset version for every evaluation run.

## Internal Success Measures

The pilot success target is not "the assistant sounds helpful." HarborLight measures success with retrieval hit rate, groundedness, refusal correctness, user feedback, latency, and the number of support interruptions avoided during onboarding.

For the teaching project, a successful demo shows one supported direct answer, one multi-document answer, one numerical answer with arithmetic, one temporal answer, one comparison answer, and one insufficient-context refusal. Each answer should show source filenames.

## Release Boundaries

The assistant may be used by internal employees during the pilot after the production readiness checklist is accepted. It may not be embedded in external customer portals without a separate access-control design, customer communication review, and security sign-off.

## Enterprise Engagement Lifecycle

HarborLight treats the employee assistant as an enterprise enablement program rather than a chatbot experiment. The standard lifecycle starts with business discovery, moves through data readiness, then golden dataset approval, architecture review, implementation, evaluation, Dockerized deployment, monitoring, and continuous improvement. Product leadership requires those phases to be presented in that order during student demos.

The assistant pilot has three approved user groups: customer success managers, product support specialists, and onboarding trainers. Customer success managers use the assistant to prepare for customer calls. Product support specialists use it to verify support tiers, incident obligations, and product behavior. Onboarding trainers use it to teach new employees how HarborLight documents product and policy facts.

The assistant is not approved for customer self-service, regulatory filings, legal advice, financial forecasting, or employee HR decisions. If a question asks for one of those topics and the knowledge base does not contain approved language, the assistant should give an insufficient-context answer and cite the boundary when possible.

## Knowledge Base Governance

The approved knowledge base contains four source families: company documents, product documents, customer summaries, and incident or policy documents. Each family has a different owner and review cadence. Company documents are reviewed by product operations twice per year. Product documents are reviewed quarterly. Customer documents are reviewed at renewal or after material amendments. Policies are reviewed annually unless an incident requires an earlier update.

A knowledge base refresh must include a change note with the changed filenames, the reason for the change, the document owner, and whether ingestion must be rerun. If source content, chunk size, chunk overlap, embedding model, or metadata schema changes, ingestion must be rerun. If only the answer prompt changes, ingestion is not required.

The pilot collection naming pattern is `harborlight_docs_v1`, then `harborlight_docs_v2` for the next controlled rebuild. The collection version should be recorded beside the embedding model, chunk size, chunk overlap, retrieval k, prompt version, and golden dataset version.

## Assistant Operating Principles

The assistant should keep answers short enough for support handoff while still showing the evidence path. A good answer names the fact, cites the source filename, and avoids unsupported interpretation. When two documents disagree, the assistant should not choose silently; it should say the approved sources appear inconsistent and recommend escalation to the document owner.

For numerical questions, the assistant should show simple arithmetic when the arithmetic is part of the answer. For example, if a question asks for total employees, it should show 96 + 38 + 31 + 19 = 184. For temporal questions, it should include exact dates when the source documents include exact dates.

## Pilot Success Measures

The pilot target is at least 85% retrieval hit rate on the golden dataset, average groundedness of 4 or higher in LLM judge review, and no Severity 1 hallucination in the final demo. The product owner may approve release with known weak cases only if each weak case has an owner, a documented cause, and a planned fix.

HarborLight tracks insufficient-context responses as a positive control, not just as failures. A correct refusal is counted as successful when the question asks for private, unsupported, or out-of-scope information and the answer avoids inventing facts.

## Example Employee Use Cases

An onboarding trainer may ask the assistant to explain the difference between RouteWise and DelayCast before a new-hire workshop. A support specialist may ask which customers were affected by an incident before drafting a handoff note. A customer success manager may ask which policy governs a renewal clause before preparing a meeting agenda.

The approved answer pattern is evidence first. The assistant should identify the relevant fact, name the source filename, and keep the answer compact. If the answer requires multiple documents, it should make the document roles clear: one source for the customer-specific fact, one source for the product or policy rule, and one source for incident details if applicable.

## Non-Goals for the Pilot

The pilot does not implement role-aware retrieval, customer portal embedding, automated ticket creation, contract redlining, billing changes, or production incident paging. Those items are documented as future production concerns. The teaching project focuses on the lifecycle mechanics needed before those features would be safe.

The pilot also does not evaluate every possible employee question. It evaluates representative categories so students can reason about quality trends and weak cases rather than chasing anecdotal success.

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
