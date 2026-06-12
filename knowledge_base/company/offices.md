# Offices

HarborLight Analytics has four offices.

| Office | Opened | Primary function | Employees |
|---|---:|---|---:|
| Seattle | 2019 | Headquarters, AI platform, executive staff | 96 |
| Rotterdam | 2021 | Port operations research and European customer success | 38 |
| Singapore | 2022 | Asia-Pacific support and carrier integrations | 31 |
| Austin | 2024 | Fleet analytics and evaluation engineering | 19 |

The Seattle office owns company-wide platform operations. Rotterdam is the primary office for DockFlow customer workshops. Singapore is the first-line office for APAC support coverage.

## Office Responsibilities

Seattle hosts the AI platform team, model operations review, and executive steering group. It owns final approval for production model configuration and collection version naming.

Rotterdam hosts port operations specialists. It leads DockFlow implementation workshops, terminal simulation exercises, and port customer discovery sessions. EastGate Ports, HarborNova Terminal, and SilverQuay Authority usually receive Rotterdam-led workshops.

Singapore hosts APAC support and carrier integration specialists. Singapore owns first-line support triage for APAC customers and maintains regional carrier integration notes. If an APAC issue becomes Severity 1, Singapore coordinates with Seattle platform operations.

Austin hosts evaluation engineering and fleet analytics specialists. Austin owns golden dataset maintenance for RouteWise, FleetPulse, and cross-product retrieval tests. Austin also maintains the evaluation dashboard used in this teaching project.

## Coverage Notes

Support handoff windows are designed to avoid unsupported customer escalations. Seattle covers North American business hours. Rotterdam covers European port operations hours. Singapore covers APAC first response. Austin focuses on evaluation and analytics rather than first-line customer support.

The office table is the source of truth for employee counts in this project. If a question asks for total office employees, add the four office counts: 96, 38, 31, and 19.

## Cross-Office Workflow

Seattle owns platform operations, deployment readiness, and collection version naming. If ChromaDB availability, Docker Compose configuration, or model configuration fails during a demo, Seattle platform operations is the simulated owner.

Rotterdam owns port-domain validation. DockFlow workshops, berth simulation exercises, yard capacity reviews, and public port incident language usually require Rotterdam review before being treated as final customer-facing material.

Singapore owns APAC support triage and carrier integration notes. APAC customer issues start in Singapore even when the underlying defect belongs to Seattle platform operations or Rotterdam port operations.

Austin owns evaluation engineering. Austin maintains the golden dataset, category-level dashboards, weak case table, and experiment notes. Austin also reviews whether new questions should be categorized as direct_fact, multi_doc, temporal, comparison, numerical, or insufficient_context.

## Handoff Windows

The standard weekday handoff sequence is Singapore to Rotterdam, Rotterdam to Seattle, and Seattle to Austin for evaluation defects. Austin does not provide first-line customer support; it receives evaluation defects, retrieval misses, and answer-quality regressions.

If an APAC Severity 1 issue involves DockFlow, Singapore opens the support case, Rotterdam validates port operations impact, and Seattle reviews platform logs. If the same issue becomes an evaluation defect, Austin adds or updates a golden question after the incident is closed.

## Demo Notes

For student demos, the offices document is the approved source for employee arithmetic, office opening chronology, regional responsibility, and cross-office escalation. It should not be used to infer private employee names, compensation, personal schedules, or unlisted office addresses.

The most recent office opening is Austin in 2024. The earliest office is Seattle in 2019. The European port operations center is Rotterdam. The APAC first response center is Singapore.

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
