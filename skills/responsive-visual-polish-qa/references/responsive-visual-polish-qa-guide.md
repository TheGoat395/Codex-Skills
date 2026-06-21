# Responsive Visual Polish QA Guide

## Purpose

Make the browser-rendered result the final quality gate.

## Use When

- After any frontend build or meaningful visual edit.
- Before final delivery of a website/app.
- When the user wants polished modern output rather than functional code only.

## Do Not Use When

- The task is purely advisory and no code was changed.
- No local/browser tooling exists; in that case explain the limitation and perform static checks.

## Discovery Questions

- How can the site be run locally?
- Which commands are available for lint/build/test?
- Which viewports matter most for this audience?
- Are there media/canvas/forms/interactions that need targeted checks?

## Decision Tree

- If a dev server is required, start it or use existing one.
- If browser inspection is available, check desktop and mobile.
- If visible issues exist, patch them before final answer.
- If checks fail, determine whether failure is environment/setup or regression.

## Implementation Rules

- Check around 1440, 1280, 900, and 390 widths when feasible.
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

## Shared Website Requirements

- Inspect before coding: project structure, framework, homepage/main entry, styling system, interaction/motion system, assets, and available commands.
- Before major changes, explain planned files and wait unless the user clearly says proceed, build, create, implement, fix, continue, or similar.
- Use existing project conventions first; explain major dependencies before adding them.
- Default to premium modern quality without generic SaaS/agency/template patterns.
- Prefer real, generated, or art-directed visuals when the subject benefits from images, video, product UI, or spatial media.
- Build version 1, inspect the rendered result, improve visual quality, then run available checks again.
- Check desktop and mobile. Keep text readable, avoid overlaps, respect focus states and reduced motion.
- Report files changed, commands run, visual checks completed, and anything not tested.
