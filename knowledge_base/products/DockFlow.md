# DockFlow

DockFlow coordinates berth schedules, yard capacity, gate appointments, and container handoffs for port operators.

Key facts:

- Initial release date: 2021-08-03.
- Primary office support: Rotterdam.
- Standard SLA target: berth schedule refresh within 5 minutes.
- Common outcome: 12% to 18% reduction in gate queue time.
- Integrates with DelayCast for disruption forecasts.

DockFlow is referenced in the EastGate Ports, HarborNova Terminal, and SilverQuay Authority customer documents.

## Data Inputs

DockFlow uses vessel arrival notices, berth plans, yard capacity snapshots, gate appointment schedules, equipment availability, and terminal exception events. DelayCast can add disruption forecasts when customers subscribe to both products.

The product does not control physical terminal equipment. It coordinates planning signals and recommended schedule adjustments for operations teams.

## Configuration Notes

DockFlow implementations start with a berth schedule baseline, then add yard and gate constraints. Rotterdam specialists usually lead workshops because they maintain HarborLight's port operations playbooks.

EastGate Ports uses two simulation workshops per year. HarborNova Terminal can request one emergency yard-capacity model review per quarter. SilverQuay Authority requires plain-language incident summaries because it is a public port authority.

## Evaluation Notes

Good DockFlow answers should cite both product and customer files when a question combines product behavior with a customer obligation. The 5-minute berth refresh target comes from this file, while customer-specific workshop and incident-summary obligations come from customer documents.

## Known Edge Cases

DockFlow can miss its refresh SLA if berth schedule cache invalidation fails. The 2024 DockFlow berth refresh incident affected HarborNova Terminal and led to a synthetic berth refresh monitor.

## Implementation Runbook

DockFlow implementations begin with terminal map validation, berth naming normalization, yard capacity snapshot review, and gate appointment data checks. Rotterdam specialists lead the initial workshop because terminology differs across terminal operators.

The standard DockFlow implementation sequence is berth baseline import, yard constraint mapping, gate appointment integration, disruption simulation, operator review, and production handoff. A disruption simulation is required before peak-season use for Mission Critical port customers.

## Planning Signals

DockFlow separates planning signals into berth signals, yard signals, gate signals, and exception signals. Berth signals include vessel arrival changes and berth conflicts. Yard signals include capacity snapshots and reefer slot availability. Gate signals include appointment volume and truck queue patterns. Exception signals include equipment outages and schedule recovery events.

When a customer also uses DelayCast, DockFlow can show disruption forecasts beside berth and yard planning views. The forecast does not automatically change the schedule; operators review recommendations before operational action.

## Metrics and Monitoring

DockFlow monitoring tracks berth refresh latency, stale schedule count, gate queue estimate accuracy, yard capacity forecast error, and operator override notes. The teaching SLA fact is berth schedule refresh within 5 minutes.

If refresh latency exceeds the target, support teams check cache invalidation, source system freshness, and terminal integration status before declaring a platform outage.

## Answer Boundaries

DockFlow answers should not imply HarborLight controls cranes, trucks, labor assignments, or physical berth availability. DockFlow coordinates planning signals and recommended adjustments. Customer operators retain authority over terminal execution.

Questions about EastGate workshops, HarborNova emergency yard reviews, and SilverQuay public briefing language require customer-file citations in addition to this product file.

## Teaching Deep Dive

This product document is designed to teach the difference between product capability, customer deployment, support obligation, and policy rule. A product file describes what the product does, what its standard targets are, which integrations exist, and where the product should not be overclaimed. A customer file proves whether a specific customer adopted the product. A policy file proves retention, support, pricing, or security rules.

Students should practice answering product questions with precise scope. If a user asks what the product can do generally, this file may be sufficient. If a user asks whether a customer receives the feature, the answer must cite the customer file. If a user asks about price, retention, support tier, or incident review obligations, the answer must cite the relevant policy or incident file.

## Implementation Evidence

Production RAG projects need implementation details because real users ask operational questions, not only marketing questions. Implementation notes help the assistant answer how teams configure, monitor, and troubleshoot the product while still avoiding unsupported promises. The implementation notes are intentionally specific enough for retrieval tests but not so specific that they expose secrets or customer-private financial data.

Every implementation answer should preserve the boundary between recommendation and control. HarborLight products provide signals, forecasts, reports, or recommendations. Customers retain operational authority. The assistant should not imply that software directly controls weather, labor, vehicles, cranes, regulatory submissions, or customer business decisions.

## Evaluation Design Notes

Product documents support direct factual tests, comparison tests, temporal tests, and multi-document tests. Good golden questions ask for release dates, standard SLA targets, integrations, monitoring signals, and product boundaries. Weak questions are useful when they ask the assistant to overclaim a guarantee that the product document does not provide.

When students change chunk size, they should check whether product key facts stay together with the relevant boundary language. If chunks separate a product capability from its limitation, the answer can become overconfident.

## Maintenance Notes

Product documents should be updated after a release, integration change, standard SLA change, or approved product-positioning change. If a product document changes, rerun ingestion and then run retrieval evaluation before answer evaluation. Prompt tuning cannot compensate for missing or stale product facts.
