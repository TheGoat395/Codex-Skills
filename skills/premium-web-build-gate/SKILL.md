---
name: premium-web-build-gate
description: "Check premium specs before implementation."
---

# Premium Web Build Gate

## Overview

Use this skill to prevent generic website output by locking strategy, reference direction, content boundaries, visual system, motion behavior, stack decisions, and QA criteria before implementation. It is a gate: do not start code until the brief below is concrete enough that another design engineer could build from it without guessing.

## Required Order

Follow this sequence for premium web work:

1. Inspect the current project, repo instructions, design docs, route structure, live/local render, assets, and existing copy.
2. Research or re-check current reference sources when the references, tools, product standards, or external sites may have changed.
3. Select Tier 1, Tier 2, or Tier 3 from [the shared quality tiers](../website-operating-rules/references/website-quality-tiers.md); higher tiers inherit lower-tier requirements.
4. Classify sources as `use`, `distill`, `inspiration only`, or `avoid`.
5. Produce the Build-Ready UI Spec.
6. Proceed within the existing task authorization after stating material assumptions; ask only for an actually blocking unresolved choice.
7. Build version 1 using the approved spec.
8. Inspect affected rendered desktop/mobile states; fix observed defects and recheck relevant coverage.
9. Report files changed, commands run, visual QA status, and anything blocked.

## Build-Ready UI Spec

Before coding, write a concise spec with these headings:

- `Current System`: framework, entry files, styling system, interaction/motion system, source vs generated assets, junk folders, and planned edit files.
- `Quality Tier`: selected tier, inherited gates, and why the requested commercial outcome maps to it.
- `Business Truth`: what the organization actually does, stated without invented specifics, fake proof, or copied claims.
- `Page Scope`: what belongs on this page, what belongs on later subpages, and what must be removed to avoid content crowding.
- `Reference Contract`: 3-5 concrete reference behaviors to borrow, 3-5 to avoid, and which references are verified vs user shorthand.
- `Visual Lane`: typography, color/material, layout rhythm, media/art direction, component vocabulary, and density rules.
- `Motion Storyboard`: section-by-section motion beats with purpose, scroll relationship, trigger, duration feel, easing feel, reduced-motion fallback, and performance risk.
- `Implementation Stack`: chosen framework/libraries, why each is needed, and whether it is project-local or global.
- `Acceptance Gates`: desktop/mobile visual checks, interaction checks, accessibility checks, performance risks, and anti-generic checks.

## Reference Rules

Use references as behavior contracts, not vibes:

- Raycast-like means speed, keyboard/product clarity, sharp interaction states, and concrete product proof.
- Linear-like means quiet precision, dense but readable product systems, low-noise hierarchy, and operational specificity.
- Vercel-like means technical credibility, strong infrastructure language, crisp capability segmentation, and clean developer-facing surfaces.
- Squarespace-polished means elegant business flow, strong first viewport, real category clarity, and polished templates without looking generic.
- Viktor Oddy references must be treated as a named designer/source, not vague shorthand. When accessible, verify `viktoroddy.com`, `x.com/viktoroddy`, `motionsites.ai`, `designrocket.io`, and current public articles/videos, then extract concrete traits such as compact studio positioning, AI-site-builder workflows, premium hero/prompt libraries, motion-heavy hero previews, tight CTAs, GIF/video demonstrations, and disciplined type systems. Only use "Viktor-style" shorthand after the actual source has been checked or the user has supplied the traits.

In original-work mode, extract structural rules and adapt them to the brand/content. In authorized exact-fidelity mode, preserve the requested source details and identify unavailable evidence.

## Content Discipline

Premium pages fail when they become content dumps. Enforce these rules:

- Choose homepage depth from user tasks, content and page architecture; a detailed single-page site can be correct.
- Move detailed services, project examples, process minutiae, and long proof lists to subpages unless the current page specifically needs them.
- Use real copy from the repo/site/docs when available. If copy must be clarified, preserve truth and remove fluff.
- No fake metrics, fake testimonials, fake client names, fake awards, or vague claims like "world-class" unless sourced.
- Give each section a clear content role; split or reorganize only when observed crowding or comprehension calls for it.

## Visual Rules

Prefer a few decisive moves over many decorative ones:

- Use at most two type families unless a brand system already requires more.
- Keep display type meaningful. Do not use huge words as filler or status noise.
- Avoid repeated card grids, repeated circles, random dots, blobs, generic glowing lines, and decorative effects that do not support the concept.
- Use visual assets, product UI, geometry, video, or spatial scenes when they clarify the business or motion idea.
- Maintain responsive composition: mobile must be intentionally designed, not merely stacked.
- Respect the current brand anchor when the user wants it preserved.

## Motion Rules

Motion should serve sequence, depth, focus, tactility, narrative, artistic expression or deliberate delight:

- Create fewer, stronger scroll scenes rather than many small ambient animations.
- Each motion beat needs a reason: reveal hierarchy, transform context, guide attention, compare states, or resolve a scene.
- Avoid motion that competes with reading, causes overlap, jitters, drags too long, or looks like a generic template effect.
- Use GSAP/ScrollTrigger/Lenis/Motion/R3F only when they serve the storyboard.
- Always provide `prefers-reduced-motion` behavior and preserve anchor navigation.
- Animate transform, opacity, clip/mask, shader uniforms, or canvas state where possible. Avoid layout-thrashing properties.

## Tool And Skill Trust Gate

Before installing or adopting a new tool/skill:

- Prefer official docs, official skills, reputable maintainers, active repos, clear licenses, and small focused tools.
- Treat community skill lists as lead sources, not install instructions.
- Do not install broad style packs that overlap existing skills unless they add a clear missing gate.
- Install frontend libraries per project, not globally, unless the tool is a CLI or Codex skill.
- Explain why the new dependency or skill materially improves the result.
- Only when Cables Standalone is actually selected, account for its unsandboxed Node integration and external operator code. Use only trusted patches, operators, and npm dependencies; keep client assets separated and export audited web bundles for delivery.

## Final QA

Before final delivery after implementation:

- Run the site locally when possible.
- Inspect rendered desktop and mobile views when possible.
- Check text overflow, visual overlap, awkward wraps, content density, hover/focus states, reduced motion, console errors, and performance risks.
- Perform an anti-generic pass: remove anything that could belong to any random SaaS/agency template.
- Be honest about anything not tested, especially browser/screenshot QA if tooling or credits blocked it.

## Scope and evidence

Check the applicable gaps in the shared direction/build spec. `$route-sellable-web-tier` owns requested-tier interpretation; preserve that capability floor without rerunning full release governance for a small edit. Do not add a new spec, media generation or deployment solely because this gate is selected.

## Optional specialists

route-sellable-web-tier is optional. Without it, select the requested quality depth using the shared quality-tier reference, preserve project requirements, and avoid imposing enterprise governance on a localized edit.
