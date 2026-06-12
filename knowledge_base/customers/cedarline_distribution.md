# CedarLine Distribution Contract Summary

Customer name: CedarLine Distribution.

Industry: warehouse-to-store distribution.

Product adopted: FleetPulse and RouteWise.

Start date: 2023-06-01.

Renewal terms: annual renewal with 5% uplift cap.

SLA: FleetPulse telemetry freshness target of 2 minutes; RouteWise recommendations within 90 seconds.

Support tier: Standard.

Unusual clause: CedarLine excludes Sunday route optimization from service credits.

Cross-reference: Standard support coverage is in `policies/support.md`; FleetPulse raw telemetry retention is in `policies/data_retention.md`.

## Operating Context

CedarLine Distribution runs warehouse-to-store routes with predictable weekday schedules and limited Sunday operations. It uses FleetPulse for telemetry monitoring and RouteWise for route recommendations.

The Sunday route optimization exclusion means Sunday route issues are not eligible for service credits. The exclusion does not disable Sunday use of the product; it only affects service-credit calculations.

## Incident History

CedarLine was affected by the 2023 FleetPulse telemetry lag. Because CedarLine has Standard support, it received a Standard support summary rather than Priority notes or a Mission Critical review.

## Evaluation Notes

CedarLine supports questions about service-credit exclusions, Standard support, FleetPulse retention, and customer impact from the 2023 FleetPulse incident.

## Account Runbook

CedarLine account preparation starts with weekday route coverage, FleetPulse telemetry freshness, RouteWise recommendation latency, and the Sunday route optimization service-credit exclusion. Customer success should confirm whether a reported Sunday issue is a product issue, a support issue, or a service-credit question.

CedarLine uses RouteWise and FleetPulse together. FleetPulse supplies telemetry and idle-time signals, while RouteWise creates route recommendations. The customer file does not approve EmissionsLens reporting for CedarLine.

## Data and Reporting Details

CedarLine's operational review includes telemetry freshness, route recommendation latency, dispatcher override notes, and repeated warehouse departure delays. The review does not include audited emissions reporting or public-sector briefing language.

The Sunday exclusion applies only to service credits for Sunday route optimization. It does not remove Sunday access to the software and does not change weekday SLA expectations.

## Renewal Review Notes

CedarLine follows the default annual renewal with a 5% uplift cap. There is no documented pilot credit, no public-sector no-uplift term, and no Mission Critical support uplift in the approved customer summary.

If CedarLine upgrades from Standard to Priority support, the customer file and pricing review must be updated before the assistant can answer that Priority terms apply.

## Evaluation Scenarios

CedarLine is useful for testing comparisons between Standard and Priority support, questions about exclusions, and refusal behavior around products that are not adopted.

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
