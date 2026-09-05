---
name: "react-component-craft"
description: "Build component behavior and presentation."
---

# React Component Craft

For substantial web work, reuse the [scoped web contract](../website-operating-rules/references/scoped-web-contract.md) when available; it replaces duplicated policy here. Match the requested scope and existing decisions; a missing optional sibling does not block this local procedure.

## Overview

Build components that are reusable without becoming abstract sludge. Good components express local design patterns and keep the page easy to revise.

## Workflow

1. Identify the requested component or architecture outcome, affected files and existing decisions; reuse established content and visual direction.
2. Inspect the project before editing when code exists.
3. Apply this skill's specific rules from `references/react-component-craft-guide.md`.
4. Explain material implementation choices while continuing authorized work.
5. Implement when requested, inspect affected output, fix observed defects, and run the smallest decisive relevant checks.

## Reference

Read `references/react-component-craft-guide.md` when this skill triggers for a concrete website build, redesign, visual review, or implementation plan.

## Ownership

Coordinate a component spanning several concerns. Use `react-component-composition` for boundaries/slots, `react-state-and-effects-discipline` for state, `react-form-patterns` for inputs, `react-accessible-components` for semantics and `react-responsive-components` for responsive interaction. Invoke only the owner needed by the actual work.
