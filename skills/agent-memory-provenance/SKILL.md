---
name: agent-memory-provenance
description: "Design memory provenance and tenant isolation."
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

Use append-only non-sensitive event references for auditability; sensitive payloads need their own authorized deletion and retention path. Existing authorization governs storage; a memory design task does not authorize adding personal durable memories. Compact only with an explicit summary of what was retained, omitted, and still retrievable. Never place passwords, tokens, private keys, cookies, recovery codes, or unrelated client data in agent memory.

## Retrieval and isolation

- Retrieve only records relevant to the active task and permitted tenant.
- Filter by source authority, freshness, locale, and client before semantic similarity.
- Treat stale or conflicting retrieval as a question to resolve, not silent context.
- Keep client credentials, documents, logs, and decisions isolated by default.

## Verify and deliver

Test the changed behavior and material failure boundaries, selecting from cross-session recall, source citation, conflicting sources, sensitive-record exclusion, retention and tenant isolation. Deliver the requested result; select a memory map, data dictionary, retention matrix or evidence receipt only when needed for that result. Use `$agent-orchestration-architecture` for runtime ownership and `$research-provenance-archive` for durable research capture.

## Optional specialists

For durable research archives, research-provenance-archive is optional. Without it, preserve attributable source identifiers, capture dates, claim/evidence links, access boundaries and corrections in the existing project store.
