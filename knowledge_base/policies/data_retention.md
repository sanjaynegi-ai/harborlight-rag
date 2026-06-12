# Data Retention Policy

Effective date: 2026-01-01.

HarborLight retains customer operational data according to product category and contract terms.

Default retention periods:

- RouteWise route plans: 365 days.
- DockFlow berth and yard schedules: 540 days.
- EmissionsLens generated reports: 7 years.
- FleetPulse raw telemetry: 180 days.
- DelayCast forecast events: 400 days.
- Support tickets: 3 years.
- Security audit logs: 2 years.

Customer-specific retention overrides must be documented in the customer contract file and approved by the Chief Security Officer.

## Retention Review Process

Retention periods are reviewed annually by the Chief Security Officer, Data Engineering, and the relevant product owner. Changes require a documented migration plan because older indexed knowledge chunks may still describe the previous policy.

If a customer contract contains a retention override, the customer file must name the product, the retention period, and the approval owner. The default policy applies when no override is documented.

## Deletion and Reindexing

When a document is removed or replaced, Data Engineering must trigger a vector reindex. A deleted source document should not remain retrievable from ChromaDB after the next approved ingestion run.

In this teaching project, `docker compose down -v` removes the local ChromaDB volume. Production deletion would require controlled collection replacement, audit logging, and verification that removed documents are no longer returned.

## Evaluation Notes

Retention questions often require numerical answers. The assistant should cite this file for default periods and cite customer files only when a customer-specific override exists.

## Retention Ownership

The Chief Security Officer owns the policy, but Data Engineering owns execution of retention workflows. Product owners must confirm that retention changes do not break customer reporting or support obligations. Customer success owns notification language when a customer-specific override changes.

Retention changes are treated as data migrations. The migration note must identify affected products, affected customer documents, collection versions that contain old text, and the date when the new policy becomes effective.

## Retrieval Implications

The RAG assistant can retrieve old policy text if an old source document remains in the vector collection. For that reason, document replacement must be followed by controlled reindexing. Deleting a Markdown file without rebuilding ChromaDB is not sufficient.

The evaluator should include at least one retention question after any policy change. Retention questions are good regression tests because they combine product names, numbers, and policy filenames.

## Exception Handling

Customer-specific overrides must name the customer, product, retention period, approval owner, and effective date. If any of those fields is missing, the override is not ready for ingestion.

The assistant should not infer a retention override from a customer's industry. For example, refrigerated logistics does not automatically change EmissionsLens retention; the TerraPort file must state the customer-specific requirement if one exists.

## Audit Notes

A production audit should sample answers about report retention, telemetry retention, support ticket retention, and security audit logs. The reviewer checks that answers cite this policy and do not confuse generated reports with raw telemetry or support tickets.

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
