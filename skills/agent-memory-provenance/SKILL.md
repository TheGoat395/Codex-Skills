---
name: agent-memory-provenance
description: Design attributable, privacy-aware memory for AI agents. Use when an agent needs session context, durable memory, retrieval, summaries, source citations, client isolation, compaction, retention rules, or an append-only decision and evidence record.
---

# Agent Memory & Provenance

## Separate memory types

Keep these distinct:

- run state: transient tool and workflow state;
- session history: bounded conversational continuity;
- evidence store: source documents, extracts, timestamps, and access status;
- decisions: approved choices, assumptions, owner, and reconsideration condition;
- retrieval index: derived search aid, never the sole record of truth.

Do not treat an LLM summary as evidence or a vector result as permission to act.

## Design the record

For each retained item, define tenant/owner, source URI or file, capture time, fact-versus-inference label, allowed readers, retention period, deletion path, and sensitivity. Preserve originals when possible; make derived summaries reversible by linking them to their source records.

Use append-only event records for auditability. Compact only with an explicit summary of what was retained, omitted, and still retrievable. Never place passwords, tokens, private keys, cookies, recovery codes, or unrelated client data in agent memory.

## Retrieval and isolation

- Retrieve only records relevant to the active task and permitted tenant.
- Filter by source authority, freshness, locale, and client before semantic similarity.
- Treat stale or conflicting retrieval as a question to resolve, not silent context.
- Keep client credentials, documents, logs, and decisions isolated by default.

## Verify and deliver

Test cross-session recall, source citation, a conflicting-source case, a sensitive-record exclusion, retention behavior, and tenant isolation. Deliver a memory map, data dictionary, retention matrix, and example evidence receipt. Use `$agent-orchestration-architecture` for runtime ownership. For durable research capture, preserve source records and evidence receipts with the same provenance fields.
