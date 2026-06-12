# Incident Report: DockFlow Berth Refresh Delay

Date: 2024-11-04.

Affected product: DockFlow.

Impact: berth schedules refreshed every 12 minutes instead of the 5-minute SLA for HarborNova Terminal.

Root cause: a cache invalidation bug in the berth schedule service.

Follow-up action: add cache health checks and a synthetic berth refresh monitor.

Customer impact: HarborNova received a Mission Critical incident review.

Policy link: DockFlow SLA details are described in `products/DockFlow.md`.

## Detection and Timeline

HarborNova reported stale berth schedules through its Mission Critical support path. Internal monitoring confirmed that refreshes were occurring every 12 minutes instead of within the 5-minute target.

The issue was isolated to berth schedule cache invalidation. No customer data was lost. The operational impact was delayed schedule adjustment during a high-density yard planning window.

## Preventive Actions

The team added cache health checks, a synthetic berth refresh monitor, and a regression test that verifies refresh events invalidate cached schedule views. Rotterdam specialists reviewed the incident with HarborNova operations.

## Evaluation Notes

This incident supports questions about SLA comparison, root cause, customer-specific support obligations, and DockFlow's operational edge cases.

## Detailed Timeline

The 2024 DockFlow berth refresh delay affected HarborNova Terminal. Berth schedules refreshed every 12 minutes instead of the 5-minute SLA. The issue was traced to failed cache invalidation after a terminal source-system update.

The incident was treated as a Severity 1 event for HarborNova because it blocked a critical workflow for a Mission Critical customer.

## Customer Communication

HarborNova received a written incident review. The review described the affected product, customer impact, root cause, follow-up action, and synthetic berth refresh monitor added after the incident.

The communication did not promise physical terminal capacity improvements. It focused on schedule refresh behavior and recovery monitoring.

## Preventive Actions

HarborLight added a synthetic berth refresh monitor, cache invalidation tests, and a post-update validation checklist for terminal integrations. Rotterdam specialists reviewed the operational language before customer delivery.

## Evaluation Notes

This incident supports questions about HarborNova, DockFlow SLA behavior, Mission Critical review obligations, and the difference between software refresh latency and physical yard capacity.

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
