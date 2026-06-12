# TerraPort Cold Chain Contract Summary

Customer name: TerraPort Cold Chain.

Industry: refrigerated logistics and warehousing.

Product adopted: EmissionsLens.

Start date: 2023-12-01.

Renewal terms: annual renewal with a 90-day expansion option.

SLA: quarterly emissions reports delivered within three business days after data lock.

Support tier: Priority.

Unusual clause: emissions reports must separate refrigerated storage energy from transport fuel.

Cross-reference: EmissionsLens reporting templates are described in `products/EmissionsLens.md`; generated reports are retained for 7 years under `policies/data_retention.md`.

## Operating Context

TerraPort Cold Chain operates refrigerated warehouses and temperature-controlled transport lanes. It uses EmissionsLens to separate refrigerated storage energy from transport fuel in quarterly reports.

The 90-day expansion option allows TerraPort to add additional warehouse sites after renewal without renegotiating the full agreement. The option does not add RouteWise, FleetPulse, DockFlow, or DelayCast automatically.

## Incident History

TerraPort was included in the 2025 EmissionsLens report delay, but the delay did not breach TerraPort's SLA because its quarterly reports were still delivered within three business days after data lock.

## Evaluation Notes

TerraPort supports questions about cold-chain-specific reporting, retention, expansion options, and why a delay affected a customer without breaching its SLA.

## Account Runbook

TerraPort account preparation starts with quarterly data lock status, refrigerated storage energy separation, transport fuel reporting, retention obligations, and the 90-day expansion option. Customer success should confirm whether an expansion question concerns additional warehouse sites or additional products.

The 90-day expansion option allows additional warehouse sites after renewal. It does not automatically add RouteWise, FleetPulse, DockFlow, or DelayCast.

## Data and Reporting Details

TerraPort reports separate refrigerated storage energy from transport fuel because cold-chain operations can shift energy usage between warehouses and vehicles. The report should not merge those categories unless the customer approves a methodology change.

The 2025 EmissionsLens report delay affected TerraPort operationally, but it did not breach TerraPort's SLA because quarterly reports were delivered within three business days after data lock.

## Renewal Review Notes

TerraPort follows annual renewal with a 90-day expansion option. Renewal review should include site count, report category validation, data lock timing, and whether any expansion sites require updated reporting boundaries.

## Evaluation Scenarios

TerraPort is useful for questions about category separation, customer impact without SLA breach, retention, and the difference between site expansion and product expansion.

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
