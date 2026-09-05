---
name: cross-browser-qa
description: "Verify browser-engine compatibility."
---

# Cross Browser QA

Use this skill to catch browser-specific issues that one local Chromium pass will miss.

## Workflow

1. Inspect the affected surface, relevant project scripts, target URL and available inspection tooling; reuse existing context.
2. Read [Cross Browser QA Guide](references/cross-browser-qa-guide.md) before claiming the site is ready.
3. Run the narrowest meaningful checks for the risk: visual, mobile, accessibility, performance, forms, media, SEO, analytics, deployment, or handoff.
4. Fix issues when they are in scope; otherwise record exact evidence and remaining risk.
5. Summarize commands, URLs, screenshots/checks, changed files, and what was not tested.

## Scoped execution

Apply the [shared web contract](../website-operating-rules/references/scoped-web-contract.md) once when execution crosses phases; reuse it if already read. Load only the specialist guidance relevant to the requested surface and deliverable.

## Scope and evidence

Record browser engine, version, OS, viewport and tested core path. Playwright WebKit is WebKit evidence, not actual Safari or real-device certification. Mark unavailable browsers untested.
