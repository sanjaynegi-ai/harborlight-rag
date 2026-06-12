# Support Policy

Effective date: 2026-01-01.

HarborLight offers three support tiers.

| Tier | Coverage | First response target | Included review |
|---|---|---:|---|
| Standard | Business hours local region | 1 business day | Quarterly |
| Priority | 24x5 | 4 hours | Monthly |
| Mission Critical | 24x7 | 1 hour | Monthly plus incident review |

Customers with Mission Critical support receive a written incident review after Severity 1 events. Priority customers receive review notes for Severity 1 and Severity 2 events.

Support escalation for APAC customers starts in Singapore. DockFlow port workshops are usually coordinated through Rotterdam.

## Severity Levels

Severity 1 means a production service is unavailable or a critical workflow is blocked for a Mission Critical customer. Severity 2 means a major function is degraded with a workaround. Severity 3 means a non-critical issue or information request.

Written incident reviews are required for Mission Critical customers after Severity 1 events. Priority customers receive review notes for Severity 1 and Severity 2 events. Standard customers receive normal ticket summaries unless the contract states otherwise.

## Escalation Path

Support starts with the regional support queue. APAC support starts in Singapore. Port operations escalations usually include Rotterdam specialists. Platform outages include Seattle platform operations. Evaluation-related defects are routed to Austin evaluation engineering.

## Evaluation Notes

Support questions often combine customer files with this policy. The assistant should cite the customer file for the customer's tier and cite this policy for response targets, coverage, and review obligations.

## Customer Handoff Checklist

Before a customer success manager uses an assistant answer in customer communication, they should verify the cited files, confirm the support tier, check whether an incident review is required, and avoid adding commitments that are not present in the approved documents.

For Severity 1 incidents, the customer handoff note should include affected product, impact, start and end time if known, root cause, follow-up action, and whether the customer receives a written incident review.

## Support Workflow Detail

Every support case starts with customer identification, product identification, support tier confirmation, and source citation. The support tier determines response target and review obligation, but the product file determines expected product behavior.

Support managers should avoid promising service credits unless the customer contract and policy explicitly support that claim. The knowledge base contains SLA targets and review obligations, but it does not contain a general service-credit formula.

## Incident Review Contents

A written incident review for Mission Critical customers should include incident date, affected product, customer impact, duration if known, root cause, follow-up action, and prevention plan. If exact start and end timestamps are not in the incident file, the assistant should say they are not available.

Priority customers receive review notes for Severity 1 and Severity 2 events. Standard customers receive normal ticket summaries unless a customer contract says otherwise.

## Regional Escalation Examples

An APAC carrier integration outage starts with Singapore support triage. A DockFlow berth-planning concern usually includes Rotterdam specialists. A ChromaDB or model configuration failure includes Seattle platform operations. A regression in the evaluator or golden dataset is routed to Austin evaluation engineering.

## Answer Boundaries

The assistant may describe response targets and included reviews. It should not promise refunds, legal penalties, customer credits, or public statements unless those commitments appear in approved customer or policy documents.

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
