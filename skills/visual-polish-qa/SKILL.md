---
name: visual-polish-qa
description: Inspect, test, and refine frontend visual quality before delivery. Use after building or editing websites, landing pages, portfolios, dashboards, games, interactive tools, cinematic sites, luxury sites, or any UI where Codex should run a second polish pass for responsive layout, typography, spacing, hierarchy, motion, accessibility, and browser-rendered correctness.
---

# Visual Polish QA

## Principle

Do not stop when the code compiles. Inspect the rendered result, identify visible weaknesses, improve it, then run checks again.

## Required Loop

1. Start or locate the dev server when the project needs one.
2. Open the site in a browser or capture screenshots when tooling is available.
3. Check desktop and mobile widths.
4. Inspect hero, navigation, major sections, interactive states, forms, media, and footer.
5. Fix obvious visual defects and weak polish.
6. Re-run build/lint/test commands available in the repo.
7. Report what was checked and what could not be checked.

## What To Look For

- Text overflow, awkward line breaks, cramped labels, clipped buttons.
- Elements overlapping or drifting outside their intended layout.
- Hero media that is too dark, blurry, cropped, generic, or disconnected from the subject.
- Repetitive card grids and generic spacing.
- Typography that lacks hierarchy or scale discipline.
- Weak button states, missing focus styles, inert hover states.
- Motion that is too fast, too busy, inaccessible, or unrelated to hierarchy.
- Mobile layouts that simply stack without composition.
- Desktop layouts that stretch content too wide.
- Forms that look unstyled or have poor error/empty/loading states.

## Fix Biases

- Prefer fewer, stronger visual moves.
- Tighten spacing before adding decoration.
- Improve copy specificity before adding sections.
- Use real media, generated bitmap imagery, or purposeful 3D when visuals matter.
- Make controls clear with icons and labels where appropriate.
- Preserve accessibility while polishing motion and visual style.

## Verification

Use Playwright, browser tools, screenshots, or the in-app browser when available. For canvas/WebGL/Three.js work, verify that the canvas is nonblank, framed correctly, and active across desktop and mobile.

Read `references/polish-checklist.md` for the detailed pass.
