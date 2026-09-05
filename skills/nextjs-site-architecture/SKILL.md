---
name: "nextjs-site-architecture"
description: "Coordinate the Next.js foundation and ownership."
---

# Next.js Site Architecture

For substantial web work, reuse the [scoped web contract](../website-operating-rules/references/scoped-web-contract.md) when available; it replaces duplicated policy here. Match the requested scope and existing decisions; a missing optional sibling does not block this local procedure.

## Overview

Set a clean, maintainable Next.js foundation. Architecture should let the design stay consistent while keeping pages easy to refine.

## Workflow

1. Identify the requested component or architecture outcome, affected files and existing decisions; reuse established content and visual direction.
2. Inspect the project before editing when code exists.
3. Apply this skill's specific rules from `references/nextjs-site-architecture-guide.md`.
4. Explain material implementation choices while continuing authorized work.
5. Implement when requested, inspect affected output, fix observed defects, and run the smallest decisive relevant checks.

## Reference

Read `references/nextjs-site-architecture-guide.md` when this skill triggers for a concrete website build, redesign, visual review, or implementation plan.

## Ownership

Own the Next.js foundation and integration map. Let `nextjs-app-router-routing` own detailed route-file/navigation behavior and `nextjs-server-client-boundaries` own import, serialization and rendering boundaries. Apply only the relevant specialist rather than repeating their full workflows.
