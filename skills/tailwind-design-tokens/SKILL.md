---
name: "tailwind-design-tokens"
description: "Map semantic tokens into Tailwind utilities."
---

# Tailwind Design Tokens

For substantial web work, reuse the [scoped web contract](../website-operating-rules/references/scoped-web-contract.md) when available; it replaces duplicated policy here. Match the requested scope and existing decisions; a missing optional sibling does not block this local procedure.

## Overview

Make Tailwind feel like a design system, not utility confetti. Tailwind is fast, but the taste comes from tokens, constraints, and repeated decisions.

## Workflow

1. Identify the requested component or architecture outcome, affected files and existing decisions; reuse established content and visual direction.
2. Inspect the project before editing when code exists.
3. Apply this skill's specific rules from `references/tailwind-design-tokens-guide.md`.
4. Explain material implementation choices while continuing authorized work.
5. Implement when requested, inspect affected output, fix observed defects, and run the smallest decisive relevant checks.

## Reference

Read `references/tailwind-design-tokens-guide.md` when this skill triggers for a concrete website build, redesign, visual review, or implementation plan.

## Ownership

Own token consumption by the installed Tailwind version and mapping to utilities/aliases. Use `design-token-production-pipeline` only when generation, validation or multiple output consumers require a compiler contract.
