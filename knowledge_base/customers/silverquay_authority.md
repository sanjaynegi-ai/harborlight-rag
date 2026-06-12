# SilverQuay Authority Case Study

Customer name: SilverQuay Authority.

Industry: public port authority.

Product adopted: DockFlow and DelayCast.

Start date: 2024-02-05.

Renewal terms: annual public-sector renewal with no automatic uplift in the first renewal year.

SLA: DockFlow refresh within 5 minutes; DelayCast 72-hour forecast window.

Support tier: Mission Critical.

Unusual clause: all incident summaries must be written in plain-language public briefing format.

Cross-reference: incident `incidents/2024-07-delaycast-weather-feed.md` affected SilverQuay; support review rules are in `policies/support.md`.

## Operating Context

SilverQuay Authority is a public port authority. It uses DockFlow for berth planning and DelayCast for disruption forecasts. Public accountability shapes its communication requirements.

The plain-language public briefing clause applies to incident summaries. It requires customer-facing summaries to avoid internal jargon and to explain impact, root cause, and follow-up action in terms suitable for public officials.

## Incident History

SilverQuay was affected by the 2024 DelayCast weather feed gap. Forecast confidence scores were unavailable for 2 hours. Because SilverQuay has Mission Critical support, a Mission Critical incident review was required.

## Evaluation Notes

SilverQuay supports questions about public-sector renewal terms, plain-language incident summaries, DelayCast forecast behavior, and Mission Critical support obligations.

## Account Runbook

SilverQuay account preparation starts with DockFlow refresh performance, DelayCast forecast availability, plain-language incident summary requirements, and Mission Critical support obligations. Public-sector communication should avoid internal jargon.

The plain-language public briefing format requires a short explanation of what happened, who was affected, why it happened, what HarborLight changed, and what the customer can expect next.

## Data and Reporting Details

SilverQuay uses DockFlow and DelayCast together for port disruption planning. It does not use RouteWise, FleetPulse, or EmissionsLens in the approved customer file.

Because SilverQuay is a public port authority, incident summaries should be suitable for public officials. Technical root cause details can be included, but they should be explained in ordinary operational language.

## Renewal Review Notes

SilverQuay has an annual public-sector renewal with no automatic uplift in the first renewal year. Renewal review should include public briefing obligations, Mission Critical incident review history, and whether DockFlow and DelayCast usage remains in scope.

## Evaluation Scenarios

SilverQuay is useful for testing public-sector renewal exceptions, plain-language communication requirements, and Mission Critical incident obligations after the 2024 DelayCast weather feed gap.

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
