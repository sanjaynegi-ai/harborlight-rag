# MetroDray Services Case Study

Customer name: MetroDray Services.

Industry: port drayage fleet.

Product adopted: FleetPulse.

Start date: 2024-06-15.

Renewal terms: annual renewal each June with pilot credit applied in the first year.

SLA: FleetPulse telemetry freshness target of 2 minutes.

Support tier: Priority.

Unusual clause: MetroDray requires a weekly exception report during the first 120 days.

Cross-reference: pilot credit rules are in `policies/pricing.md`; FleetPulse telemetry rules are in `products/FleetPulse.md`.

## Operating Context

MetroDray Services operates port drayage vehicles and adopted FleetPulse during a first-year pilot. The main pilot goal is to identify recurring exception events before expanding to route optimization.

The weekly exception report during the first 120 days includes telemetry freshness exceptions, idle-time outliers, depot geofence anomalies, and maintenance-signal trends.

## Commercial Notes

MetroDray's first-year pilot credit must be documented because pilot credits are pricing exceptions under the Pricing Policy. The customer has not adopted RouteWise, DockFlow, EmissionsLens, or DelayCast in the approved customer file.

## Evaluation Notes

MetroDray supports questions about pilot credits, weekly exception reports, FleetPulse-only adoption, and the distinction between pilot terms and standard annual renewal.

## Pilot Exit Criteria

MetroDray's pilot exit review checks three items: whether weekly exception reports were delivered during the first 120 days, whether telemetry freshness met the 2-minute target, and whether depot geofence anomalies decreased after operations coaching.

If MetroDray expands after the pilot, RouteWise is the likely next product under discussion, but it is not listed as adopted in the approved customer summary.

## Account Runbook

MetroDray account preparation starts with pilot status, weekly exception report delivery, telemetry freshness, depot geofence anomaly trends, and the first-year pilot credit. Customer success should not describe RouteWise as adopted unless a future amendment adds it.

The first 120 days are treated as a learning period. Weekly exception reports are intended to help MetroDray identify repeated operational patterns before expanding the deployment.

## Data and Reporting Details

The weekly exception report has four sections: telemetry freshness exceptions, idle-time outliers, depot geofence anomalies, and maintenance-signal trends. A fifth optional note may describe coaching actions, but the four sections are the required ones.

Depot geofence anomalies are reviewed alongside driver feedback because port drayage yards often have shared entrances and staging lanes. A geofence anomaly does not automatically indicate driver error.

## Renewal Review Notes

MetroDray renews each June. The first renewal review should check whether the pilot credit was applied correctly, whether weekly reports were delivered, and whether the customer wants to discuss RouteWise as a possible expansion.

## Evaluation Scenarios

MetroDray is useful for testing pilot-credit language, exact report-section recall, numerical questions about the three pilot exit criteria, and refusal behavior for confidential negotiated margin.

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
