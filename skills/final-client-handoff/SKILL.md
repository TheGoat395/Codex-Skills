---
name: final-client-handoff
description: "Prepare verified ownership and delivery notes."
---

# Final Client Handoff

Use this skill to give the user a calm, accurate closeout they can trust and act on.

## Closeout modes

For a small change, report changed files, actual checks and remaining limits; no release manifest is required. For a client release, aggregate existing applicable ownership, tested/untested, recovery and release evidence using the full procedure below.

## Workflow

1. Inspect the affected surface, relevant project scripts, target URL and available inspection tooling; reuse existing context.
2. Read [Final Client Handoff Guide](references/final-client-handoff-guide.md) before claiming the site is ready.
3. Run the narrowest meaningful checks for the risk: visual, mobile, accessibility, performance, forms, media, SEO, analytics, deployment, or handoff.
4. Fix issues when they are in scope; otherwise record exact evidence and remaining risk.
5. Summarize commands, URLs, screenshots/checks, changed files, and what was not tested.

For a full client release, use [references/release-handoff-template.md](references/release-handoff-template.md) for the release, monitoring, recovery, and ownership record. Validate it with `python3 "<skill-root>/scripts/verify-handoff.py" <handoff.json>`.

## Scoped execution

Apply the [shared web contract](../website-operating-rules/references/scoped-web-contract.md) once when execution crosses phases; reuse it if already read. Load only the specialist guidance relevant to the requested surface and deliverable.

For helper-driven evidence, use the [typed record schema](references/evidence-record-schema.md). The helper validates structure only; use actual inspection/test results for claims.

Resolve `<skill-root>` to this skill folder's actual absolute location; preserve project-local module resolution for Node capture tools.
