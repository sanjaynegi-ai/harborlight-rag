# Discovery Questions

## Client and Business Owner

- What employee groups need the assistant?
- Which decisions will answers support?
- What is in scope and out of scope?
- What risks come from wrong answers?

Example answer: support and sales need faster policy, product, and contract lookup; unsupported questions must be refused.

## Data Engineering

- What documents exist?
- Who owns them?
- Are they approved?
- How often do they change?
- Are deprecated versions clearly marked?

Example answer: approved Markdown files are refreshed monthly, while incident reports are added within two business days after closure.

## Domain Experts

- What questions should the assistant answer?
- What is a correct answer?
- Which source filenames should support each answer?
- Which cases require insufficient-context responses?

Example answer: pricing questions must cite `policies/pricing.md` and relevant customer files.

## Security and Governance

- Are there access restrictions?
- Is PII present?
- What audit logs are required?
- How are secrets managed?

Example answer: the teaching project has no real PII, but production would need role-aware retrieval.
