# Pricing Policy

Effective date: 2026-01-01.

HarborLight uses annual subscription pricing with product add-ons.

Base annual list prices:

- RouteWise: 180,000 USD.
- DockFlow: 240,000 USD.
- EmissionsLens: 150,000 USD.
- FleetPulse: 165,000 USD.
- DelayCast: 120,000 USD.

Discount rules:

- Multi-product bundle discount: 8% for two products, 12% for three or more products.
- Pilot customers may receive a 90-day pilot credit.
- Renewal uplift cap is 5% unless the customer contract states otherwise.
- Mission Critical support adds 15% of subscription value.

Pricing exceptions require product owner and finance approval.

## Pricing Examples

A customer buying RouteWise and DelayCast qualifies for the two-product bundle discount of 8%. Based on list prices, RouteWise plus DelayCast totals 300,000 USD before discount and 276,000 USD after the 8% bundle discount.

A customer buying DockFlow, DelayCast, and EmissionsLens qualifies for the three-product bundle discount of 12%. Based on list prices, those three products total 510,000 USD before discount and 448,800 USD after the 12% bundle discount.

Mission Critical support is calculated after subscription value is established. If the subscription value is 300,000 USD, Mission Critical support adds 45,000 USD.

## Approval Notes

Pilot credits must be documented in the customer file. MetroDray Services has a first-year pilot credit. Public-sector no-uplift terms must also be documented; SilverQuay Authority has no automatic uplift in the first renewal year.

## Evaluation Notes

Pricing questions should distinguish list price, discount, renewal uplift cap, pilot credit, and support uplift. Actual paid contract price is not available in the approved documents unless a customer file states it.

## Pricing Governance

Pricing exceptions are reviewed monthly by finance operations. The review checks whether exceptions have an owner, an expiration date, and a documented business reason. Exceptions without documentation are not eligible for renewal automation.

The assistant may summarize published list prices and documented customer clauses. It must not estimate confidential negotiated pricing, margin, or discount history beyond the approved policy and customer summaries.

## Pricing Interpretation Rules

List price, discounted subscription value, support uplift, renewal uplift, and pilot credit are different concepts. The assistant should name which concept it is answering about. If a user asks for actual paid price and the customer file does not state it, the correct answer is insufficient context.

Bundle discounts apply to subscription product list prices before Mission Critical support is added. Mission Critical support is calculated as 15% of subscription value after the subscription value is established.

## Approval Workflow

Pricing exceptions require product owner approval and finance approval. The approval record should include the customer, exception type, expiration date, business reason, and whether the exception affects renewal automation.

A pricing exception in a customer file is more specific than the default policy. BlueRiver's 4% uplift cap and SilverQuay's no automatic uplift in the first renewal year are approved customer-specific exceptions.

## Teaching Examples

RouteWise plus DelayCast totals 300,000 USD before discount. With the two-product 8% bundle discount, the subscription value is 276,000 USD. If Mission Critical support were added to that discounted value, the support uplift would be 41,400 USD.

FleetPulse plus RouteWise totals 345,000 USD before discount. With the two-product 8% bundle discount, the subscription value is 317,400 USD. The policy does not state any actual customer paid price for CedarLine or UrbanHaul.

## Answer Boundaries

The assistant may calculate policy examples from published list prices and discount rules. It must not estimate confidential negotiated margin, sales commission, procurement concessions, or customer payment history.

## Teaching Deep Dive

This policy document teaches students how enterprise RAG systems answer rule-based questions. A policy file defines defaults, controls, approval paths, and boundaries. A customer file may override a default, but the override must be explicit. The assistant should never infer an exception from customer size, industry, region, or similarity to another customer.

Policy answers should be careful with verbs. The assistant may say a policy requires, allows, or prohibits something only when this file says so. If the policy only describes a review process or target, the assistant should not turn that into a penalty, refund, legal obligation, or guarantee.

## Cross-Document Use

Many correct answers require both this policy and another source. A support answer needs the customer support tier plus the policy response target. A retention answer may need the product retention default plus the customer override. A pricing answer may need list price, discount rule, and the customer-specific renewal clause.

Students should check whether the answer cites the source of each rule. A single citation is often not enough when the question combines customer-specific and policy-level facts.

## Evaluation Design Notes

Policy files support numerical questions, comparison questions, insufficient-context questions, and multi-document questions. They are ideal for testing whether the assistant refuses to invent legal penalties, actual paid prices, passwords, private addresses, or unsupported access-control details.

If policy chunks are too large, retrieval may include many unrelated rules. If chunks are too small, the rule and its exception-handling note may separate. Students should inspect retrieved chunks before changing prompts.

## Maintenance Notes

Policies should be reviewed after incidents, leadership decisions, regulatory changes, or operational changes. Any policy change requires reingestion, baseline evaluation, and a check for stale source text in ChromaDB. A policy deletion or replacement is not complete until old chunks are no longer retrievable.
