# Test Strategy

## Evaluation-First Approach

Build a golden dataset and run baseline retrieval before tuning prompts, chunks, or models.

## Unit Test Strategy

Test document loading, metadata enrichment, chunking, schema validation, and mocked retrieval/answer behavior.

## Integration Test Strategy

Tests that require ChromaDB and OpenAI are labeled through skip conditions. They verify ingestion and RAG behavior against real services when available.

## Smoke Test Strategy

Check Dockerfiles, Compose services, scripts, and configuration loading.

## Regression Evaluation

Run retrieval and answer evaluations before and after experiments.

## Human Review

Domain experts review golden answers and weak cases.

## Release Criteria

Critical unit tests pass, integration tests pass in the target environment, baseline evaluation is documented, and known failures are accepted or fixed.
