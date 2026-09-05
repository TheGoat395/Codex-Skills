---
name: browser-inspection-workflow
description: "Coordinate rendered behavior and state evidence."
---

# Browser Inspection Workflow

Use this skill to make rendered-browser inspection a default part of shipping frontend work.

## Workflow

1. Inspect the affected surface, relevant project scripts, target URL and available inspection tooling; reuse existing context.
2. Read [Browser Inspection Workflow Guide](references/browser-inspection-workflow-guide.md) before claiming the site is ready.
3. Run the narrowest meaningful checks for the risk: visual, mobile, accessibility, performance, forms, media, SEO, analytics, deployment, or handoff.
4. Fix issues when they are in scope; otherwise record exact evidence and remaining risk.
5. After fixes, recheck affected rendered states; repeat broader polish only for an observed defect or unresolved quality risk.
6. Summarize commands, URLs, screenshots/checks, changed files, and what was not tested.

If a native `fullPage` screenshot is blank, sparse, missing lower content, frozen before reveal animation, or inconsistent with the working scroll experience, do not use it as visual proof. Route the capture through `$visual-regression-lab` and its stitched viewport workflow.

## Scoped execution

Apply the [shared web contract](../website-operating-rules/references/scoped-web-contract.md) once when execution crosses phases; reuse it if already read. Load only the specialist guidance relevant to the requested surface and deliverable.

## Scope and evidence

Coordinate one route/viewport/state evidence matrix shared by QA specialists. Reuse current evidence; recheck affected coverage after relevant changes. Captures require actual visual inspection before quality claims.
