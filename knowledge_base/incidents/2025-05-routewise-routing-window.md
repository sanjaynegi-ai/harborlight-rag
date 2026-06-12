# Incident Report: RouteWise Routing Window Error

Date: 2025-05-21.

Affected product: RouteWise.

Impact: NorthPier Logistics and BlueRiver Freight saw route recommendations delayed beyond 90 seconds for 31 minutes.

Root cause: a traffic provider response format changed without prior notice.

Follow-up action: add provider contract tests and fallback parsing.

Customer impact: Priority support summaries were sent to both customers.

Policy link: RouteWise SLA expectations are described in `products/RouteWise.md`.

## Detection and Timeline

The issue was detected when recommendation latency exceeded the 90-second target. NorthPier Logistics and BlueRiver Freight experienced delayed recommendations for 31 minutes.

The upstream traffic provider changed a response field name without prior notice. RouteWise continued to operate, but fallback parsing did not recognize the new format until the incident response team patched the parser.

## Preventive Actions

HarborLight added provider contract tests, fallback parsing, and monitoring for schema drift in upstream traffic responses. BlueRiver's quarterly review included a note explaining that delayed recommendations did not change the customer's 4% uplift cap.

## Evaluation Notes

This incident supports questions about affected customers, duration, RouteWise SLA expectations, and why provider schema changes matter to route recommendation latency.

## Detailed Timeline

The 2025 RouteWise routing window error delayed route recommendations for 31 minutes. The affected symptom was recommendation latency, not incorrect route distance or deleted route plans.

The root cause was an upstream traffic provider schema change that broke a parser used during recommendation preparation. RouteWise fallback parsing was not strict enough to catch the change before latency increased.

## Customer Communication

BlueRiver was included in follow-up review because it uses RouteWise for fuel-weighted routing outcomes. The quarterly review noted that delayed recommendations did not change BlueRiver's documented 4% uplift cap.

The customer communication explained provider schema drift, fallback parsing, and monitoring improvements without exposing provider credentials or internal secrets.

## Preventive Actions

HarborLight added provider contract tests, schema drift alerts, and fallback parsing validation. Austin evaluation engineering added questions that distinguish recommendation latency from route correctness.

## Evaluation Notes

This incident supports numerical questions about 31 minutes, product-boundary questions about RouteWise latency, and multi-document questions involving BlueRiver's pricing exception.

## Teaching Deep Dive

This incident document teaches students how post-incident facts should be grounded. An incident file proves the affected product, impact, root cause, follow-up action, and customer impact if applicable. It should not be used to invent broader product defects, legal penalties, or customer compensation.

Incident answers should distinguish the symptom, cause, affected customers, duration, support obligation, and prevention plan. Users often blur those concepts, so the assistant should answer with clear labels when the question combines them.

## Cross-Document Use

Incident questions often require customer and policy citations. The incident file proves what happened. The customer file proves the affected customer's support tier or unusual clause. The support policy proves whether a written review or review notes are required.

If exact timestamps, compensation, or internal credentials are not in the incident file, the assistant should say so. A duration such as 2 hours or 31 minutes is not the same as exact start and end timestamps.

## Evaluation Design Notes

Incident files support temporal questions, numerical duration questions, multi-document support-obligation questions, and insufficient-context questions about missing timestamps or penalties. They are useful for testing whether the assistant avoids turning incident summaries into unsupported legal or commercial claims.

Students should add a golden question after any new incident file is added. The question should check the incident fact itself and at least one cross-document obligation if a customer was affected.

## Maintenance Notes

Incident reports are added after closure. If security policy is referenced, the security owner reviews the report before ingestion. If an incident changes a product runbook or policy, the product or policy document must also be updated; otherwise the knowledge base will contain an incident fact without the updated operating rule.
