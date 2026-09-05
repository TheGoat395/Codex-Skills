---
name: visual-polish-qa
description: "Refine rendered finish at accepted viewports."
---

# Visual Polish QA

## Principle

Inspect affected rendered output after implementation. Fix observed weaknesses within authorization and recheck affected behavior; stop when acceptance is met. An analysis-only review reports findings without edits.

## Required Loop

1. Start or locate the dev server when the project needs one.
2. Open the site in a browser or capture screenshots when tooling is available.
3. Check the accepted target viewports; route a systematic breakpoint problem to `responsive-visual-polish-qa`.
4. Inspect hero, navigation, major sections, interactive states, forms, media, and footer.
5. Fix obvious visual defects and weak polish.
6. Run relevant required checks; repeat or broaden only after changes, failures or an unresolved risk.
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

## Scope and evidence

Inspect affected visual finish using relevant viewports and states from the shared evidence matrix. A four-viewport matrix is a useful broad-review starting point, not mandatory for every local edit. Route breakpoint defects to `$responsive-visual-polish-qa`.
