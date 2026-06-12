# Incident Report: FleetPulse Telemetry Lag

Date: 2023-10-18.

Affected product: FleetPulse.

Impact: telemetry freshness exceeded the 2-minute target for UrbanHaul Express and CedarLine Distribution for 47 minutes.

Root cause: a queue worker configuration limited parallel processing after a routine deployment.

Follow-up action: increase worker concurrency, add lag alerting, and update deployment checklist.

Customer impact: Priority support notes were sent to UrbanHaul Express; CedarLine received Standard support summary.

Policy link: support response expectations are described in `policies/support.md`.

## Detection and Timeline

The lag was detected by an internal telemetry freshness monitor. The first alert fired 6 minutes after the queue began falling behind. The incident lasted 47 minutes from first customer impact to restored freshness.

UrbanHaul Express had Priority support and received Priority support notes. CedarLine Distribution had Standard support and received a Standard support summary.

## Preventive Actions

The follow-up actions added worker-concurrency checks, deployment rollback guidance, and lag alert thresholds. Austin evaluation engineering added a golden dataset case to verify that FleetPulse lag answers cite both the incident and the support policy when support obligations are asked.

## Evaluation Notes

This incident supports numerical questions about duration, comparison questions about support handling, and multi-document questions involving FleetPulse telemetry freshness.

## Detailed Timeline

The 2023 FleetPulse telemetry lag was detected by queue freshness monitoring before most users reported it. The lag lasted 47 minutes. The affected customer-facing symptom was delayed telemetry visibility, not lost vehicle data.

Support compared telemetry arrival time with event creation time to confirm that the issue was ingestion latency. The incident did not change FleetPulse raw telemetry retention, which remains governed by the Data Retention Policy.

## Customer Communication

UrbanHaul received Priority support notes because it has Priority support. CedarLine received a Standard support summary because it has Standard support. Neither customer received a Mission Critical written incident review for this event.

The approved customer communication explained that telemetry appeared late, queue worker concurrency was corrected, and monitoring thresholds were adjusted.

## Preventive Actions

HarborLight added queue concurrency monitoring, freshness alerts, and a replay check to confirm that delayed telemetry events were processed after recovery. Austin evaluation engineering added weak-case questions to ensure the assistant separates delayed telemetry from deleted telemetry.

## Evaluation Notes

This incident is useful for comparison questions about support tier outcomes, numerical questions about 47 minutes, and questions that require citing both incident and customer files.

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
