# Incident Report: DelayCast Weather Feed Gap

Date: 2024-07-09.

Affected product: DelayCast.

Impact: forecast confidence scores were unavailable for EastGate Ports and SilverQuay Authority for 2 hours.

Root cause: third-party weather feed authentication token expired earlier than documented.

Follow-up action: add token-expiry monitoring and secondary feed failover.

Customer impact: Mission Critical incident reviews were required for EastGate Ports and SilverQuay Authority.

Policy link: Mission Critical review obligations are described in `policies/support.md`; security incident communication expectations are in `policies/security.md`.

## Detection and Timeline

The issue was detected when forecast confidence scores stopped updating while the DelayCast forecast API remained available. The customer-visible impact lasted 2 hours.

The root cause was an authentication token that expired earlier than the provider's written schedule. The issue did not expose customer data, but it triggered security communication review because authentication handling was involved.

## Preventive Actions

HarborLight added token-expiry monitoring, secondary feed failover, and a pre-expiry alert routed to Seattle platform operations. DelayCast evaluation cases were updated to distinguish API availability from forecast confidence availability.

## Evaluation Notes

This incident supports questions about affected customers, Mission Critical reviews, the difference between confidence scores and API uptime, and the role of security communication.

## Communication Detail

Customer communication stated that forecast confidence scores were unavailable, not that all DelayCast forecasts were unavailable. This distinction matters because the forecast API remained available while confidence scoring was degraded.

The security review concluded that no customer data was exposed. The follow-up still included authentication-token monitoring because the root cause involved provider credential lifecycle management.

## Detailed Timeline

The 2024 DelayCast weather feed gap lasted 2 hours. Forecast confidence scores were unavailable for EastGate Ports and SilverQuay Authority, but the approved incident summary does not include exact start and end timestamps.

The issue was detected when confidence-score availability dropped below the alert threshold. The root cause was an expired authentication token for a primary weather feed.

## Customer Communication

EastGate Ports and SilverQuay Authority both had Mission Critical support, so written incident reviews were required. SilverQuay's review also had to follow its plain-language public briefing clause.

The customer communication separated forecast confidence from underlying operational disruption. HarborLight did not say DelayCast caused weather or port congestion; it said the confidence scores were unavailable during the feed gap.

## Preventive Actions

HarborLight added token-expiry monitoring, secondary weather feed failover, and a pre-expiry alert routed to Seattle platform operations. DelayCast product documentation was updated to clarify forecast availability, confidence, and operational impact.

## Evaluation Notes

This incident is useful for insufficient-context tests about exact timestamps, multi-document tests involving Mission Critical obligations, and comparison tests about forecast confidence versus operational impact.

## Follow-Up Validation

After the incident, HarborLight validated that secondary feed failover could preserve confidence-score availability when the primary weather feed token was unavailable. The validation did not change the standard 72-hour forecast window or the 99.5% monthly forecast API uptime target.

The incident review reminded support teams that a feed gap can reduce confidence even when the API endpoint responds. That distinction became a required talking point for EastGate and SilverQuay handoff notes.

Support teams also added a checklist item to confirm whether a customer question is about API uptime, confidence-score availability, or real-world operational disruption before drafting a response.

## Teaching Deep Dive

This incident document teaches students how post-incident facts should be grounded. An incident file proves the affected product, impact, root cause, follow-up action, and customer impact if applicable. It should not be used to invent broader product defects, legal penalties, or customer compensation.

Incident answers should distinguish the symptom, cause, affected customers, duration, support obligation, and prevention plan. Users often blur those concepts, so the assistant should answer with clear labels when the question combines them.

## Cross-Document Use

Incident questions often require customer and policy citations. The incident file proves what happened. The customer file proves the affected customer's support tier or unusual clause. The support policy proves whether a written review or review notes are required.

If exact timestamps, compensation, or internal credentials are not in the incident file, the assistant should say so. A duration such as 2 hours or 31 minutes is not the same as exact start and end timestamps.

## Evaluation Design Notes

Incident files support temporal questions, numerical duration questions, multi-document support-obligation questions, and insufficient-context questions about missing timestamps or penalties. They are useful for testing whether the assistant avoids turning incident summaries into unsupported legal or commercial claims.

Students should add a golden question after any new incident file is added. The question should check the incident fact itself and at least one cross-document obligation if a customer was affected.

## Maintenance Notes

Incident reports are added after closure. If security policy is referenced, the security owner reviews the report before ingestion. If an incident changes a product runbook or policy, the product or policy document must also be updated; otherwise the knowledge base will contain an incident fact without the updated operating rule.
