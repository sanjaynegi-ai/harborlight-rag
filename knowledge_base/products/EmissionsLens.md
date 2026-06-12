# EmissionsLens

EmissionsLens produces emissions reports for logistics operations. It maps activity data to reporting categories and creates auditable summaries for sustainability teams.

Key facts:

- Initial release date: 2022-02-10.
- Supports monthly and quarterly reporting cycles.
- Standard retention for generated emissions reports follows `policies/data_retention.md`.
- Integrates with RouteWise and FleetPulse.
- Reporting templates include fuel, route distance, idle time, and avoided emissions estimates.

EmissionsLens is referenced in the GreenCurrent Shipping, BlueRiver Freight, and TerraPort Cold Chain customer documents.

## Data Inputs

EmissionsLens uses route distance, fuel consumption, idle time, refrigerated storage energy, vehicle class, vessel activity records, and customer-approved emissions factors. Ellen Brooks owns methodology reviews for emissions calculations.

The product produces auditable summaries, but it does not certify regulatory filings by itself. Customers remain responsible for final submission to regulators or auditors.

## Reporting Packages

Standard reporting packages include an executive summary, methodology notes, category-level activity data, avoided emissions estimates, and source-data exception notes. GreenCurrent Shipping receives monthly reports. TerraPort Cold Chain receives quarterly reports that separate refrigerated storage energy from transport fuel. BlueRiver Freight receives quarterly review packages with a named sustainability analyst.

## Evaluation Notes

Questions about retention should cite `policies/data_retention.md`. Questions about methodology ownership should cite `company/leadership.md`. Questions about customer-specific report timing should cite the relevant customer file.

## Known Edge Cases

Template validation can delay reports when a new category is introduced. The 2025 EmissionsLens report delay involved a refrigerated-storage category and led to schema tests for category-specific templates.

## Implementation Runbook

EmissionsLens implementations begin with activity-data mapping, reporting boundary confirmation, emissions factor approval, and template selection. The implementation team confirms whether the customer reports by shipment, route, facility, product line, or corporate reporting period.

A reporting package is not considered ready until source-data exceptions are listed separately from methodology assumptions. Source-data exceptions describe missing or late customer data. Methodology assumptions describe approved calculations or factors.

## Methodology Controls

Ellen Brooks owns methodology review standards, but customer success owns schedule coordination. Methodology changes require a reviewer, an effective date, and a note explaining whether prior reports are restated or left unchanged.

EmissionsLens can prepare auditable summaries, but the customer remains responsible for final regulatory submission. The assistant should not describe EmissionsLens output as legal certification.

## Metrics and Monitoring

EmissionsLens monitoring tracks report generation latency, template validation failures, source-data exception count, methodology version, and report delivery status. Report timing is measured after data lock, not after raw activity collection begins.

The teaching project uses two common timing facts: GreenCurrent receives monthly reports within two business days after data lock, and TerraPort receives quarterly reports within three business days after data lock.

## Answer Boundaries

Questions about report retention should cite the Data Retention Policy. Questions about report content for refrigerated storage should cite TerraPort. Questions about named sustainability analysts should cite BlueRiver. Questions about methodology ownership should cite the leadership file.

The assistant should not calculate official customer emissions totals unless the approved documents provide the exact input values and methodology.

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
