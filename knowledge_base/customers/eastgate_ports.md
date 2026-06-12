# EastGate Ports Case Study

Customer name: EastGate Ports.

Industry: multi-terminal port authority.

Product adopted: DockFlow and DelayCast.

Start date: 2022-02-14 for DockFlow; 2024-05-20 for DelayCast.

Renewal terms: three-year agreement renewing every February.

SLA: DockFlow berth refresh within 5 minutes; DelayCast forecast API 99.5% monthly uptime.

Support tier: Mission Critical.

Unusual clause: HarborLight must run two Rotterdam-led berth simulation workshops each year.

Cross-reference: Mission Critical incident review rules are in `policies/support.md`; DockFlow Rotterdam support is described in `company/offices.md`.

## Operating Context

EastGate Ports manages two container terminals and one bulk cargo terminal. It adopted DockFlow to reduce berth planning conflicts and later added DelayCast to prepare for weather and congestion disruption risks.

The two required Rotterdam-led workshops focus on berth simulation. The first workshop reviews peak-season constraints. The second workshop reviews incident response and schedule recovery.

## Reporting and Review

Because EastGate has Mission Critical support, Severity 1 incidents require a written incident review. The 2024 DelayCast weather feed gap triggered this obligation because forecast confidence scores were unavailable for 2 hours.

EastGate does not use RouteWise, FleetPulse, or EmissionsLens in the approved customer file.

## Evaluation Notes

EastGate is useful for questions that combine customer obligations, support policy, office responsibility, and incidents. Answers should cite this file for the workshop clause and product adoption dates, `policies/support.md` for Mission Critical obligations, and the relevant incident file for impact details.

## Account Runbook

EastGate account preparation starts with DockFlow berth refresh performance, DelayCast forecast confidence, Rotterdam workshop scheduling, and Mission Critical review obligations. The account team should confirm whether a question concerns normal planning, a disruption forecast, or a Severity 1 incident review.

The two annual Rotterdam-led workshops are a contract obligation. One workshop focuses on peak-season berth constraints, and one focuses on incident response and schedule recovery.

## Data and Reporting Details

EastGate's planning review uses berth conflicts, yard capacity constraints, gate queue estimates, and DelayCast forecast warnings. The review does not include fleet telemetry, route recommendation latency, or EmissionsLens reporting because those products are not adopted.

When DelayCast confidence scores are unavailable, the customer communication should distinguish forecast confidence from the actual port disruption. EastGate may still have operational disruptions that were not caused by DelayCast.

## Renewal Review Notes

EastGate renews every February under a three-year agreement. The customer has Mission Critical support, so renewal review should include incident review history, workshop delivery status, and whether DockFlow and DelayCast SLAs were met.

## Evaluation Scenarios

EastGate is useful for multi-document questions that combine DockFlow, DelayCast, Rotterdam office ownership, support tier, and the 2024 weather feed incident.

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
