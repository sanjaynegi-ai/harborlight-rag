# HarborNova Terminal Contract Summary

Customer name: HarborNova Terminal.

Industry: container terminal operations.

Product adopted: DockFlow.

Start date: 2021-10-01.

Renewal terms: annual renewal with a service review every October.

SLA: berth schedule refresh within 5 minutes.

Support tier: Mission Critical.

Unusual clause: HarborNova can request one emergency yard-capacity model review per quarter.

Cross-reference: DockFlow support is coordinated by the Rotterdam office in `company/offices.md`; incident review obligations are in `policies/support.md`.

## Operating Context

HarborNova Terminal operates a high-density container yard with frequent berth rescheduling. DockFlow is used for berth refresh planning, yard-capacity review, and schedule-recovery discussions.

The emergency yard-capacity model review clause exists because HarborNova has seasonal congestion spikes. The clause permits one emergency review per quarter, but it does not guarantee custom software development.

## Incident History

HarborNova was affected by the 2024 DockFlow berth refresh delay. Berth schedules refreshed every 12 minutes instead of the 5-minute SLA. Because HarborNova has Mission Critical support, it received a written incident review.

## Evaluation Notes

HarborNova supports questions about customer-specific clauses, DockFlow SLA behavior, Rotterdam coordination, and incident review obligations.

## Account Runbook

HarborNova account preparation starts with DockFlow berth refresh status, emergency yard-capacity model review usage, Rotterdam coordination, and Mission Critical incident review obligations. Customer success should check whether the quarterly emergency review has already been used before promising availability.

The emergency yard-capacity model review is limited to one per quarter. It is a planning review, not a guarantee of custom software work or physical yard expansion.

## Data and Reporting Details

HarborNova planning reviews include berth schedule stability, yard-density constraints, recovery options after vessel delays, and cache refresh health after the 2024 DockFlow incident.

HarborNova does not use DelayCast in the approved customer file. If a question asks about HarborNova weather forecasts or forecast API uptime, the assistant should not assume DelayCast is adopted.

## Renewal Review Notes

HarborNova renews annually with an October service review. The review should include DockFlow SLA performance, emergency yard-capacity review history, incident review completion, and Rotterdam workshop notes.

## Evaluation Scenarios

HarborNova is useful for questions about customer-specific clauses, exact support obligations, product boundaries, and the difference between planning review and software development.

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
