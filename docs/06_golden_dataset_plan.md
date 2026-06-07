# Golden Dataset Plan

## Purpose

The golden dataset provides a stable benchmark for retrieval and answer quality. It must exist before serious tuning.

## Dataset Schema

Each JSONL row contains question, keywords, reference answer, category, and expected source filenames.

## Ownership

Domain experts validate truth, AI engineers format data, QA runs regression, and the product owner approves thresholds.

## Question Categories

- `direct_fact`
- `multi_doc`
- `temporal`
- `comparison`
- `numerical`
- `insufficient_context`

## Minimum Quantity

At least 40 tests, with at least five tests in each category.

## Review Process

Draft questions, validate source files, review reference answers, run baseline, then freeze version 1.

## Acceptance Thresholds

Initial teaching thresholds: retrieval hit rate above 0.75, average groundedness above 4 for supported questions, and correct refusal behavior for insufficient-context questions.

## Examples

Question: Which product did NorthPier Logistics adopt first?

Expected source: `customers/northpier_logistics.md`
