# Culture

HarborLight's culture emphasizes evidence, calm operations, and practical sustainability.

Core values:

- Source the claim.
- Reduce operational waste.
- Improve customer trust.
- Learn in public inside the company.
- Treat incidents as system learning.

Internal documentation standards require product, policy, customer, and incident documents to include an owner, an effective date or report date, and cross-references when a fact depends on another document.

HarborLight's Friday demo ritual is called Lighthouse Review. Teams show experiments, evaluation results, and lessons learned.

## Documentation Culture

HarborLight teams are expected to write documents that are easy to quote, easy to cite, and easy to retire. A document should state what it covers, what it does not cover, who owns it, and when it should be reviewed. Documents that contain customer-specific exceptions must cross-reference the governing policy.

Teams avoid "tribal knowledge" as a release dependency. If a support engineer needs a fact to answer customers, that fact belongs in an approved document. If the fact is sensitive, it belongs in an approved restricted document with access controls rather than in an informal chat thread.

## Evaluation Culture

During Lighthouse Review, AI Engineering presents category-level evaluation results before showing anecdotal demos. A model or prompt change is not considered better unless it improves or preserves retrieval and answer quality across the golden dataset.

HarborLight uses weak cases as learning artifacts. Teams discuss why a question failed, whether the source document was unclear, whether chunking separated related facts, whether retrieval missed the right file, or whether the prompt failed to enforce refusal behavior.

## Collaboration Norms

Domain experts are expected to review golden answers in plain language. QA engineers are expected to challenge ambiguous reference answers. Product owners are expected to decide whether a weak case is a release blocker or an accepted limitation. Security reviewers are expected to identify missing access-control assumptions before release.

## Continuous Improvement Ritual

After each evaluation run, the team writes a short experiment note with five fields: configuration changed, expected improvement, retrieval result, answer result, and decision. Experiment notes are kept with the evaluator output so future teams can understand why a chunking or prompt change was accepted.

If a weak case is caused by missing source content, the fix is not prompt tuning. The fix is to assign a document owner and update the approved knowledge base. If a weak case is caused by retrieval missing the correct file, AI Engineering investigates chunk size, overlap, metadata, and retrieval k.

## Learning Culture for RAG Work

HarborLight expects teams to make uncertainty visible. A weak answer is not hidden at the end of a demo; it is shown with the retrieved chunks, the missing evidence, and the next experiment. The team distinguishes between a retrieval problem, a source-content problem, a prompt problem, and an evaluation-data problem.

The phrase used in internal reviews is "source before style." A polished answer without source support is considered worse than a plain answer with correct citations. Teams are encouraged to improve tone only after retrieval and groundedness are acceptable.

## Golden Dataset Etiquette

Domain experts write reference answers in plain operational language. They avoid trick wording unless the category is explicitly testing insufficient context. QA engineers check that each test has expected sources or clear refusal criteria. AI engineers maintain JSONL formatting and ensure that each new category has enough examples.

Golden questions should not be rewritten only to make metrics look better. If a real employee would ask a messy question, the evaluation set should include at least a few messy but realistic phrasings.

## Demo Review Checklist

A Lighthouse Review demo note must include five items: the owner, the configuration used, the strongest category, the weakest category, and the next action. If a demo omits weak cases, the review is considered incomplete.

A tuning experiment should have one primary change. Changing chunk size, overlap, model, prompt, and k at the same time makes the result hard to interpret. The preferred experiment note names exactly one controlled variable unless the team is intentionally testing a bundled release candidate.

## Refusal Culture

HarborLight treats correct insufficient-context answers as evidence of maturity. The assistant should be comfortable saying that approved documents do not contain salary bands, private addresses, confidential negotiated margins, credentials, or exact event timestamps when those details are absent.

A refusal should be specific enough to be useful. "I do not know" is less helpful than "The approved documents describe the support tier and SLA, but they do not provide legal penalty language."

## Review Language Standards

HarborLight asks reviewers to use concrete labels when discussing RAG behavior. A "retrieval miss" means the correct source did not appear in top-k results. A "grounding miss" means the source appeared but the answer did not use it correctly. A "source gap" means no approved document contains the fact. A "policy boundary" means the assistant should refuse or narrow the answer even if the user asks confidently.

These labels help students avoid vague debugging. Saying "the model was bad" is not enough. The team must identify whether the source content, retriever, prompt, evaluation row, or user expectation needs to change.

The labels are recorded in experiment notes so later reviewers can compare fixes across releases.

## Teaching Deep Dive

This document is also used to teach students how enterprise RAG answers depend on document purpose. A company document usually provides organizational context, official boundaries, ownership, and operating norms. It should not be treated as a substitute for a customer contract, product specification, incident report, or policy.

When a learner asks an assistant question, this document can supply framing facts, but the answer may still require a second source. For example, a question about who owns a review may cite leadership, while a question about how that review affects a customer may also cite the customer file. A question about an office role may cite offices, while a support obligation still requires the support policy.

Students should notice that broad company documents are high-value retrieval targets but can also cause overgeneralization. A good RAG answer uses the broad document to orient the answer and then cites the specific source that proves the operational detail. This is one reason the project keeps metadata for source, category, filename, and document path.

## Retrieval Risk Notes

Company documents often contain terms that appear in many questions: assistant, support, customer, evaluation, owner, and release. Those terms can make retrieval noisy. The evaluation set therefore includes questions that require the assistant to select a narrower document even when company text is also relevant.

If company chunks dominate retrieval, students should inspect chunk size, overlap, and metadata filtering. They should not immediately rewrite the answer prompt. Retrieval quality should be diagnosed before answer style.

## Operational Examples

A customer success manager preparing for a call might ask for the correct escalation owner, the accepted release boundary, or the right demo talking point. The answer should cite the company document for those broad facts and avoid inventing undocumented details such as private employee schedules, unlisted locations, or customer-specific commitments.

An onboarding trainer might ask why the assistant refuses salary, credential, or private pricing questions. The answer should explain that source documents do not contain those facts and that safe refusal is an intended behavior.

## Maintenance Notes

Company documents should be reviewed after leadership changes, office changes, governance changes, or release-scope changes. If a company document changes, ingestion must be rerun because source text has changed. After reingestion, the team should run at least the direct_fact, multi_doc, and insufficient_context portions of the golden dataset.
