# Problem Statement

## Executive Summary

HarborLight Analytics needs an internal assistant that answers employee questions from approved company documents and cites source filenames.

## Business Pain

Employees search across scattered product notes, customer contracts, policies, and incident reports. Answers are slow, inconsistent, and sometimes based on outdated memory.

## Target Users

Sales, customer support, product managers, engineering leads, finance operations, and executives.

## Current Process

Employees ask in chat channels, search shared folders, or interrupt document owners.

## Proposed RAG Assistant

The assistant retrieves approved Markdown documents from a ChromaDB-backed knowledge base and uses an OpenAI chat model to produce grounded answers with source citations.

## Expected Benefits

Faster internal answers, fewer interruptions, better source traceability, improved onboarding, and safer policy lookup.

## In Scope

Company overview, leadership, culture, offices, products, customer contracts and case studies, support policies, pricing policies, data retention policies, security policies, and incident reports.

## Out of Scope

Legal advice, HR case details, unreleased financials, personal employee data, customer secrets not in approved files, and answers without source support.
