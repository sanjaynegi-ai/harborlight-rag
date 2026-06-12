# BlueRiver Freight Contract Summary

Customer name: BlueRiver Freight.

Industry: long-haul freight brokerage.

Product adopted: RouteWise and EmissionsLens.

Start date: 2022-07-11.

Renewal terms: two-year renewal with a 4% uplift cap.

SLA: RouteWise recommendations within 90 seconds; quarterly EmissionsLens report package.

Support tier: Priority.

Unusual clause: BlueRiver requires a named sustainability analyst for quarterly review meetings.

Cross-reference: pricing uplift rules are in `policies/pricing.md`; EmissionsLens templates are described in `products/EmissionsLens.md`.

## Operating Context

BlueRiver Freight brokers long-haul freight and uses RouteWise to prioritize fuel-efficient route planning. EmissionsLens packages quarterly sustainability summaries for executive and customer reporting.

BlueRiver's named sustainability analyst attends quarterly review meetings. The review covers route distance trends, avoided emissions estimates, fuel-weighted routing outcomes, and source-data exceptions.

## Commercial Notes

BlueRiver's 4% uplift cap is lower than the default 5% renewal uplift cap in the pricing policy. The customer file is the source for that exception.

BlueRiver does not use DockFlow, FleetPulse, or DelayCast in the approved customer file.

## Evaluation Notes

BlueRiver is useful for questions about pricing exceptions, named analyst obligations, and product combinations involving RouteWise and EmissionsLens.

## Account Runbook

BlueRiver account preparation starts with RouteWise fuel-weighted routing outcomes, EmissionsLens quarterly package status, and the named sustainability analyst schedule. Customer success should verify whether the quarterly review meeting is focused on route trends, avoided emissions estimates, or source-data exceptions before drafting notes.

The named sustainability analyst is an account obligation, not a general EmissionsLens feature. If another customer asks for the same role, the assistant should cite that BlueRiver has the clause and avoid implying that all EmissionsLens customers receive it.

## Data and Reporting Details

BlueRiver's quarterly review package includes four recurring sections: route distance trend, avoided emissions estimate, fuel-weighted routing outcome, and source-data exception log. The source-data exception log identifies missing lane data, late broker updates, and unusual fuel records.

BlueRiver does not receive a monthly idle-time appendix. That clause belongs to UrbanHaul. BlueRiver does not receive public briefing incident summaries. That clause belongs to SilverQuay.

## Renewal Review Notes

The 4% uplift cap should be checked before renewal quoting because it differs from the default 5% uplift cap. Finance approval is still required for any additional exception beyond the documented 4% cap.

If BlueRiver adds FleetPulse in a future amendment, the customer file must be updated before the assistant can say FleetPulse is adopted. Until then, FleetPulse answers for BlueRiver should be treated as insufficient context.

## Evaluation Scenarios

BlueRiver is useful for testing whether the assistant separates list price from customer-specific uplift cap, and whether it cites customer files for unusual clauses. It also tests whether the assistant avoids transferring UrbanHaul's idle-time appendix to another customer.

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
