# UrbanHaul Express Case Study

Customer name: UrbanHaul Express.

Industry: last-mile delivery fleet.

Product adopted: FleetPulse and RouteWise.

Start date: 2023-09-15 for FleetPulse; 2023-11-01 for RouteWise.

Renewal terms: annual renewal each September.

SLA: FleetPulse telemetry freshness target of 2 minutes and RouteWise recommendations within 90 seconds.

Support tier: Priority.

Unusual clause: UrbanHaul receives an idle-time emissions appendix each month.

Cross-reference: FleetPulse telemetry retention is described in `policies/data_retention.md`; RouteWise integration is described in `products/RouteWise.md`.

## Operating Context

UrbanHaul Express runs dense city delivery routes with frequent idle-time events. FleetPulse was adopted first to expose telemetry and idle-time patterns. RouteWise was added later to improve routing decisions using those signals.

UrbanHaul's monthly idle-time emissions appendix summarizes idle minutes, estimated avoidable fuel use, and route segments with repeated dwell time. The appendix is not the same as a full EmissionsLens audited report.

## Incident History

UrbanHaul was affected by the 2023 FleetPulse telemetry lag for 47 minutes. Because UrbanHaul has Priority support, it received Priority support notes rather than a Mission Critical incident review.

## Evaluation Notes

UrbanHaul supports questions about product sequence, telemetry freshness, and the difference between an appendix and audited EmissionsLens reporting. Good answers should avoid claiming that UrbanHaul uses EmissionsLens.

## Account Runbook

UrbanHaul account preparation starts with FleetPulse telemetry freshness, RouteWise recommendation latency, idle-time emissions appendix delivery, and Priority support history. Customer success should verify whether a question is about telemetry, routing, or the monthly appendix.

UrbanHaul adopted FleetPulse before RouteWise. That sequence matters because FleetPulse exposed idle-time patterns before RouteWise used those signals for routing decisions.

## Data and Reporting Details

The monthly idle-time emissions appendix includes idle minutes, estimated avoidable fuel use, route segments with repeated dwell time, and operations notes for dense city delivery zones. It is an appendix, not a full audited EmissionsLens report.

UrbanHaul's route reviews often focus on curbside dwell time, failed delivery clustering, and repeated congestion around depot exits. These are operational patterns, not contractual penalties.

## Renewal Review Notes

UrbanHaul renews each September. Renewal review should include FleetPulse telemetry performance, RouteWise recommendation performance, idle-time appendix delivery, and whether Priority support notes were completed for relevant incidents.

## Evaluation Scenarios

UrbanHaul is useful for testing product adoption sequence, appendix-vs-report distinctions, incident support tier differences, and multi-document answers combining FleetPulse and RouteWise.

## Teaching Deep Dive

This customer document is designed to teach account-specific grounding. A customer file proves adoption, start date, renewal terms, SLA summary, support tier, unusual clauses, and approved cross-references for one customer. It should not be generalized to other customers unless another approved file states the same fact.

Customer documents are especially important because they often override default policy. A pricing uplift cap, public-sector renewal rule, pilot credit, unusual report, workshop commitment, or incident-summary format should be cited from the customer file before it is used in an answer. The policy document explains the default rule; the customer file proves the exception.

## Account Handoff Practice

A realistic account handoff answer should mention the adopted products, the support tier, the unusual clause, and any cross-document source that governs the answer. If a customer does not use a product, the assistant should avoid implying future roadmap, likely expansion, or similar-customer behavior as fact.

Students should practice distinguishing adopted products from possible future discussions. A phrase such as "likely next product under discussion" is not the same as "product adopted." The assistant should preserve that distinction because customer success teams may rely on it in call preparation.

## Evaluation Design Notes

Customer files support direct_fact questions about support tier and adopted product, temporal questions about start dates, comparison questions between customers, numerical questions about report counts or review limits, and multi_doc questions involving policy or product files. They also support insufficient_context questions about actual paid price, confidential margin, unapproved products, and private customer details.

If retrieval misses a customer file, students should inspect whether filenames, customer names, product names, and unusual clauses are preserved in chunk metadata and chunk text. Customer names are strong retrieval anchors; losing them during chunking usually hurts answer quality.

## Maintenance Notes

Customer summaries should be reviewed at renewal, after a material amendment, after an incident affecting the customer, or when a customer adds or removes a product. If a customer document changes, ingestion must be rerun and at least one golden question for that customer should be reviewed or added.
