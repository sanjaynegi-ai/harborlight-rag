# DelayCast

DelayCast forecasts logistics disruptions using weather, port congestion, labor notices, traffic patterns, and carrier status signals.

Key facts:

- Initial release date: 2024-01-18.
- Standard forecast window: 72 hours.
- Standard SLA target: forecast API availability of 99.5% monthly uptime.
- Integrates with DockFlow for port disruption planning.
- Integrates with RouteWise for route risk warnings.

DelayCast is referenced in the EastGate Ports, SilverQuay Authority, and NorthPier Logistics customer documents.

## Data Inputs

DelayCast uses weather feeds, port congestion signals, labor notices, traffic patterns, vessel arrival changes, carrier status messages, and historical disruption outcomes. Forecast confidence depends on source availability and freshness.

DelayCast provides risk forecasts, not guaranteed predictions. Customer teams use forecasts to plan contingency actions.

## Configuration Notes

The standard forecast window is 72 hours. NorthPier Logistics uses DelayCast to warn dispatch teams about route risk. EastGate Ports and SilverQuay Authority use DelayCast with DockFlow for port disruption planning.

## Evaluation Notes

Good DelayCast answers should distinguish between forecast window, API uptime SLA, and customer incident obligations. The forecast window and 99.5% uptime target are in this file. Mission Critical review obligations are in `policies/support.md`.

## Known Edge Cases

Forecast confidence can be unavailable if a weather feed authentication token expires. The 2024 DelayCast weather feed gap affected EastGate Ports and SilverQuay Authority for 2 hours and led to token-expiry monitoring plus secondary feed failover.

## Customer Communication Notes

DelayCast answers should avoid promising that forecasts are always correct. The approved language is that DelayCast provides disruption risk forecasts that help teams plan contingency actions. For Mission Critical customers, customer-facing incident language must separate forecast availability, forecast confidence, and the underlying operational event.

If a customer asks whether DelayCast caused a delay, support teams should check whether DelayCast provided a warning, whether the customer received the warning, and whether operational teams acted on it. The product forecasts risk; it does not control weather, port labor notices, or carrier behavior.

## Implementation Runbook

DelayCast implementations begin with region selection, feed availability review, customer alert threshold design, and downstream workflow mapping. The team confirms whether forecasts are used for dispatch, port planning, customer communication, or executive reporting.

A customer should not receive operational alerts until thresholds are validated against historical disruption examples. Thresholds that are too sensitive create alert fatigue; thresholds that are too conservative miss useful warnings.

## Forecast Interpretation

DelayCast separates forecast availability, forecast confidence, and operational impact. Forecast availability means the API responds. Forecast confidence means source data is fresh enough to support the risk estimate. Operational impact means the disruption actually affects the customer's lanes, terminals, or carrier commitments.

This distinction matters for incident communication. A weather feed gap can lower forecast confidence even when the API remains available. A weather event can disrupt operations even when DelayCast correctly warned the customer.

## Metrics and Monitoring

DelayCast monitoring tracks API uptime, feed freshness, confidence-score availability, forecast horizon coverage, alert volume, and customer acknowledgement rate. The standard forecast window is 72 hours, but useful confidence may vary by region and source availability.

Production monitoring would track separate freshness indicators for weather, traffic, labor notices, port congestion, and carrier status feeds.

## Answer Boundaries

DelayCast forecasts risk; it does not control weather, labor notices, carrier behavior, port congestion, or customer response. The assistant should avoid saying DelayCast caused or prevented a delay unless the approved documents explicitly say so.

Questions about EastGate, SilverQuay, and NorthPier require customer citations. Questions about the 2024 weather feed gap require the incident file in addition to this product file.

## Alert Design Examples

DelayCast alert thresholds are configured by workflow. A dispatch workflow may prefer earlier warnings with lower confidence so teams can plan alternate routes. A port operations workflow may prefer fewer alerts with higher confidence so planners are not distracted during berth recovery.

The assistant should describe these as configuration examples, not universal defaults. The approved universal facts are the 72-hour standard forecast window, the 99.5% monthly forecast API uptime target, and the distinction between availability, confidence, and operational impact.

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
