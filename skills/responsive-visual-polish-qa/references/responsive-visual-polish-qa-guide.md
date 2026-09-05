# Responsive Visual Polish QA Guide

## Purpose

Make the browser-rendered result the final quality gate.

## Use When

- When the affected surface requires this specialist's visual dimension.
- Before final delivery of a website/app.
- When the user wants polished modern output rather than functional code only.

## Do Not Use When

- No relevant visual review or implementation is requested. Advisory/source-only review is valid with explicit visual limits.
- No local/browser tooling exists; in that case explain the limitation and perform static checks.

## Discovery Questions

- How can the site be run locally?
- Which commands are available for lint/build/test?
- Which viewports matter most for this audience?
- Are there media/canvas/forms/interactions that need targeted checks?

## Decision Tree

- If a dev server is required, start it or use existing one.
- If browser inspection is available, check desktop and mobile.
- If visible issues exist, fix them when authorized; otherwise report precise findings.
- If checks fail, determine whether failure is environment/setup or regression.

## Implementation Rules

- Select relevant viewports from the shared evidence matrix; 1440, 1280, 900 and 390 are broad-review starting points.
- Inspect hero, nav, major sections, CTAs, forms, media, footer.
- Look for horizontal scroll, overlaps, clipped text, weak crops, default states, poor focus.
- For canvas/WebGL, verify nonblank pixels and framing.
- Run checks again after polish when feasible.

## Useful Patterns

- Desktop pass: composition, whitespace, hero, section rhythm.
- Mobile pass: navigation, text wrap, crop, CTA reachability.
- Interaction pass: hover/focus/active/loading/error.
- Media pass: images/video/canvas load and frame correctly.

## Anti-Patterns

- Only reading code and assuming it looks right.
- Ignoring mobile because desktop looks okay.
- Leaving text overflow in buttons/cards/nav.
- Claiming tests ran when they did not.

## QA Checklist

- Record commands run and URLs inspected.
- Capture screenshots or browser metrics when useful.
- Fix visible defects and note residual risks.

## Acceptance Criteria

- The final answer states what was inspected.
- The site has had a visible polish pass across at least desktop/mobile when possible.

## Scoped execution

Apply the [shared web contract](../../website-operating-rules/references/scoped-web-contract.md) once when execution crosses phases; reuse it if already read. Load only the specialist guidance relevant to the requested surface and deliverable.
