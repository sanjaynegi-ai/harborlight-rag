# RouteWise

RouteWise optimizes delivery and drayage routes to reduce fuel usage and late arrivals. It combines route constraints, live traffic signals, yard availability, and fuel models.

Primary users are dispatch teams, carrier operations managers, and sustainability analysts.

Key facts:

- Initial release date: 2020-04-15.
- Standard SLA target: route recommendations available within 90 seconds.
- Typical measured fuel reduction range: 6% to 11%.
- Integrates with FleetPulse for live vehicle telemetry.
- Integrates with EmissionsLens for emissions reporting.

RouteWise is referenced in the NorthPier Logistics, UrbanHaul Express, BlueRiver Freight, and CedarLine Distribution customer documents.

## Data Inputs

RouteWise uses route constraints, delivery time windows, yard availability, traffic signals, vehicle class, driver shift limits, and fuel-consumption profiles. FleetPulse telemetry can provide live vehicle position and idle-time signals when a customer has both products.

RouteWise does not replace dispatcher judgment. It provides recommended routes, risk warnings, and fuel-impact estimates. Dispatchers remain responsible for final route approval.

## Configuration Notes

The default optimization objective balances arrival reliability and fuel reduction. Customers may request a reliability-heavy profile during peak season. NorthPier Logistics uses a balanced profile. BlueRiver Freight uses a fuel-weighted profile for quarterly sustainability reviews. CedarLine Distribution excludes Sunday route optimization from service credits under its customer clause.

## Evaluation Notes

Good RouteWise answers should distinguish between list price, SLA target, and measured fuel-reduction range. The list price is in `policies/pricing.md`, while the 90-second recommendation target and 6% to 11% fuel reduction range are in this product document.

## Known Edge Cases

RouteWise recommendations can be delayed when upstream traffic provider formats change. The 2025 RouteWise routing window incident documents one such case and references fallback parsing as the follow-up action.

## Implementation Runbook

RouteWise implementations begin with lane inventory, delivery-window validation, vehicle-class mapping, and dispatcher workflow review. The customer success team confirms which constraints are hard constraints and which are preferences. Hard constraints include legal driver hours, customer delivery windows, and vehicle eligibility. Preferences include lower fuel use, fewer tolls, and preferred yards.

The standard implementation milestone sequence is discovery workshop, baseline route import, optimization dry run, dispatcher review, pilot launch, and production handoff. A production handoff is not complete until the customer confirms that exception routes and no-go zones are represented correctly.

## Profiles and Configuration

RouteWise supports a balanced profile, a fuel-weighted profile, and a reliability-heavy profile called Peak Guard. The balanced profile is the default. The fuel-weighted profile is commonly used for sustainability review. Peak Guard is used during holiday surges, labor disruptions, or severe weather windows when late-arrival risk is more important than fuel savings.

Profile changes are configuration changes, not model retraining. Customer success should document profile changes in the customer file when the change affects SLA interpretation, quarterly reporting, or an unusual clause.

## Metrics and Monitoring

RouteWise monitoring tracks recommendation latency, route acceptance rate, avoided miles, late-arrival risk, and dispatcher override rate. A high override rate can indicate that constraints are stale or that the optimization objective no longer matches operations reality.

The teaching project uses the 90-second recommendation target as the primary SLA fact. Production monitoring would also track p95 and p99 recommendation latency by customer, region, and provider feed.

## Answer Boundaries

The assistant may say that RouteWise typically shows a 6% to 11% measured fuel reduction range. It must not promise a guaranteed fuel reduction for a new customer unless that guarantee appears in an approved customer contract. It also must not claim that RouteWise replaces dispatcher judgment.

Questions about list price should cite `policies/pricing.md`. Questions about NorthPier, UrbanHaul, BlueRiver, or CedarLine deployment details should cite the relevant customer file.

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
