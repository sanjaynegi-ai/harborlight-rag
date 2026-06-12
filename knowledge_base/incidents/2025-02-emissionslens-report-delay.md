# Incident Report: EmissionsLens Report Delay

Date: 2025-02-12.

Affected product: EmissionsLens.

Impact: February draft emissions reports for GreenCurrent Shipping and TerraPort Cold Chain were delayed by one business day.

Root cause: report template validation rejected a new refrigerated-storage category.

Follow-up action: add schema tests for category-specific report templates.

Customer impact: no SLA breach for TerraPort; GreenCurrent received a Standard support notice.

Policy link: report retention is described in `policies/data_retention.md`.

## Detection and Timeline

The delay was detected during report template validation. The new refrigerated-storage category was valid for TerraPort Cold Chain but had not been included in the validation schema.

GreenCurrent Shipping received a Standard support notice because its monthly draft report was delayed by one business day. TerraPort Cold Chain had no SLA breach because its quarterly report still met the three-business-day delivery window.

## Preventive Actions

EmissionsLens added schema tests for customer-specific reporting categories and a checklist item requiring methodology review when a new emissions category appears.

## Evaluation Notes

This incident supports questions that require distinguishing customer impact from SLA breach. It also supports multi-document questions involving TerraPort's refrigerated storage clause and EmissionsLens reporting templates.

## Detailed Timeline

The 2025 EmissionsLens report delay involved a refrigerated-storage reporting category. Template validation delayed report packaging while the team checked whether refrigerated storage energy and transport fuel were separated correctly.

TerraPort was included in the affected group, but its SLA was not breached because quarterly reports were still delivered within three business days after data lock.

## Customer Communication

The approved communication said the delay came from template validation, not from a change in emissions methodology. If methodology had changed, Ellen Brooks's methodology review standards would have applied.

Customer success reminded teams that report delay questions should cite the customer file for SLA timing and the product file for template behavior.

## Preventive Actions

HarborLight added schema tests for category-specific templates, a refrigerated-storage validation example, and a checklist that separates source-data exceptions from methodology assumptions.

## Evaluation Notes

This incident supports questions about customer impact without SLA breach, cold-chain reporting categories, and why product template issues should not be confused with methodology approval.

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
