# NorthPier Logistics Contract Summary

Customer name: NorthPier Logistics.

Industry: regional freight forwarding and drayage.

Product adopted: RouteWise first, followed by DelayCast.

Start date: 2021-06-01 for RouteWise; 2024-03-01 for DelayCast.

Renewal terms: annual renewal with a 5% uplift cap.

SLA: RouteWise recommendations within 90 seconds and DelayCast API availability of 99.5% monthly uptime.

Support tier: Priority.

Unusual clause: NorthPier receives a quarterly routing emissions summary because its board reports avoided fuel usage.

Cross-reference: RouteWise fuel reduction expectations are described in `products/RouteWise.md`; DelayCast forecast window is described in `products/DelayCast.md`.

## Operating Context

NorthPier runs short-haul drayage routes between inland rail yards and coastal distribution centers. Its dispatch team cares about fuel reduction, predictable pickup windows, and early warning for weather-driven route risk.

NorthPier uses RouteWise as the primary planning tool and DelayCast as a risk overlay. RouteWise creates the route recommendation. DelayCast adds disruption warnings when the forecast indicates weather, port congestion, or carrier status risk within the 72-hour window.

## Reporting and Review

The quarterly routing emissions summary is reviewed by NorthPier's operations director and HarborLight's customer success lead. The summary must include avoided fuel estimates, late-arrival trend notes, and the top three recurring route-risk causes.

NorthPier does not currently use FleetPulse or EmissionsLens. Questions about NorthPier raw vehicle telemetry or audited emissions reports should not imply those products are deployed.

## Evaluation Notes

NorthPier is useful for multi-document questions because its contract references both RouteWise and DelayCast. A good answer should cite this file for adoption dates and customer clauses, `products/RouteWise.md` for route recommendation behavior, and `products/DelayCast.md` for forecast window details.

## Account Runbook

NorthPier account preparation starts with RouteWise recommendation performance, DelayCast risk-warning coverage, quarterly routing emissions summary status, and recurring route-risk causes. Customer success should confirm whether the question asks about adopted products or a reporting clause.

NorthPier adopted RouteWise first and DelayCast later. The product sequence matters because RouteWise remains the primary planning tool and DelayCast acts as a risk overlay.

## Data and Reporting Details

NorthPier's quarterly routing emissions summary includes avoided fuel estimates, late-arrival trend notes, and the top three recurring route-risk causes. The summary is not an EmissionsLens audited report because NorthPier has not adopted EmissionsLens.

Route risk causes are grouped into weather exposure, port congestion, carrier status uncertainty, and pickup-window compression. DelayCast contributes warnings for the first three categories when relevant source feeds are available.

## Renewal Review Notes

NorthPier follows annual renewal with a 5% uplift cap. The renewal review should include RouteWise SLA performance, DelayCast uptime, quarterly summary delivery, and whether the 72-hour forecast window meets dispatch planning needs.

## Evaluation Scenarios

NorthPier is useful for temporal questions, product-sequence questions, and tests that require the assistant to avoid claiming FleetPulse telemetry or EmissionsLens audited reporting.

## Dispatch Workflow Detail

NorthPier dispatchers review RouteWise recommendations first and then inspect DelayCast risk warnings for the next 72 hours. If a high-risk warning appears, the dispatcher may choose a safer pickup window or a different route, but the approved documents do not require a specific operational action.

The quarterly routing emissions summary is board-facing, so customer success should keep language concise and avoid unsupported claims about regulatory certification. The approved summary supports avoided fuel estimates and late-arrival trends, not audited emissions reporting.

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
