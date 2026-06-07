# Monitoring and Observability Plan

## Logs

Log user question, retrieved source filenames, retrieval k, similarity scores when available, answer latency, model, insufficient-context responses, and user feedback.

## Metrics

Track retrieval hit rate, groundedness, hallucination reports, no-answer rate, latency, cost, document freshness, and collection version.

## Alerts

Alert on ChromaDB unavailability, high latency, cost spikes, low groundedness, elevated no-answer rate, and stale knowledge base versions.

## Tracing Concepts

Trace request ID across retrieval, prompt construction, LLM response, and UI return.

## Feedback

Collect thumbs up/down, correction notes, and requested missing documents.

## Cost Tracking

Estimate embedding cost per reindex and chat cost per answer using token usage when available.

## Drift and Freshness

Monitor document age, refresh cadence, and category-specific weak cases.
