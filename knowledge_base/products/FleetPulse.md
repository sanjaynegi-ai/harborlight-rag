# FleetPulse

FleetPulse monitors vehicle telemetry, idle time, maintenance signals, and exception events.

Key facts:

- Initial release date: 2023-05-22.
- Standard telemetry freshness target: 2 minutes.
- Stores raw telemetry for 180 days under `policies/data_retention.md`.
- Integrates with RouteWise for live routing.
- Integrates with EmissionsLens for idle-time emissions calculations.

FleetPulse is referenced in the UrbanHaul Express, CedarLine Distribution, and MetroDray Services customer documents.

## Data Inputs

FleetPulse uses GPS pings, engine status, idle-time events, odometer readings, maintenance signals, driver exception codes, and customer-defined depot geofences. Raw telemetry retention is 180 days under the Data Retention Policy.

FleetPulse does not make final maintenance decisions. It surfaces exception signals and trend summaries for fleet managers.

## Configuration Notes

UrbanHaul Express uses FleetPulse with RouteWise and receives a monthly idle-time emissions appendix. CedarLine Distribution uses FleetPulse with RouteWise but has Standard support. MetroDray Services uses FleetPulse only and receives a weekly exception report during its first 120 days.

## Evaluation Notes

Good FleetPulse answers should separate telemetry freshness, raw telemetry retention, customer support tier, and reporting clauses. The 2-minute freshness target is in this product document. Support tiers appear in customer files and `policies/support.md`.

## Known Edge Cases

Telemetry lag can occur if queue worker concurrency is misconfigured. The 2023 FleetPulse telemetry lag incident affected UrbanHaul Express and CedarLine Distribution for 47 minutes.

## Implementation Runbook

FleetPulse implementations begin with vehicle inventory, device mapping, depot geofence setup, telemetry freshness testing, and exception-code review. The customer success team confirms which vehicles are production vehicles, test vehicles, and excluded assets.

The first operational milestone is a telemetry confidence review. During that review, HarborLight checks whether GPS pings, engine status, odometer readings, and idle-time events are arriving within the 2-minute freshness target.

## Configuration Notes for Geofences

Depot geofences require a two-week calibration period when a customer has complex yards or shared depot entrances. During calibration, exception counts may be higher than normal because boundaries are still being adjusted.

MetroDray's depot geofence anomaly tracking is a pilot example. UrbanHaul's dense city routes are a different pattern because the main signal is idle-time clustering rather than depot boundary behavior.

## Metrics and Monitoring

FleetPulse monitoring tracks telemetry freshness, missing device count, idle-time trend, maintenance signal volume, depot geofence exceptions, and queue-worker latency. The teaching project uses raw telemetry retention of 180 days and telemetry freshness of 2 minutes as core facts.

If telemetry freshness degrades, support teams check device connectivity, ingestion queue health, and provider API status before escalating to platform operations.

## Answer Boundaries

FleetPulse can surface maintenance signals, but it does not make final maintenance decisions. It can calculate idle-time trends, but audited emissions reporting requires EmissionsLens unless the customer file states otherwise.

Questions about UrbanHaul's idle-time appendix should not imply UrbanHaul has adopted EmissionsLens. Questions about MetroDray should distinguish its approved FleetPulse pilot from a possible future RouteWise expansion.

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
