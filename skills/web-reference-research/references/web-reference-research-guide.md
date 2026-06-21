# Web Reference Research Guide

## Purpose

Convert taste references into concrete, verifiable design decisions.

## Use When

- The user asks for research, current references, X/GitHub inspiration, or named web design influences.
- The prompt includes brands or people such as Squarespace, Raycast, Linear, Vercel, Viktor Oddy, Codrops, Awwwards, Framer-style, or luxury/cinematic sites.
- A design feels vague and needs source-backed constraints before coding.

## Do Not Use When

- The user provides a complete approved design system and asks for implementation only.
- The task is offline and browsing is not needed or allowed.
- The request is a simple local bug fix unrelated to design references.

## Discovery Questions

- Which reference is primary and which are secondary?
- Is the reference about layout, motion, typography, copy, product realism, visual assets, or polish?
- What site category are we applying the reference to?
- What would be inappropriate to borrow from the reference?

## Decision Tree

- If the reference is current/public and precision matters, browse and cite sources.
- If a source is inaccessible, say so and label any interpretation as inference.
- Extract traits into build rules: type, layout, color, media, motion, copy, conversion, QA.
- Create steal/adapt/avoid notes before implementation.
- During QA, compare the result against the extracted traits rather than the reference name.

## Implementation Rules

- Do not pretend to have verified X content if it was not accessible.
- Use reference names as shorthand only after defining the concrete traits.
- Avoid copying proprietary assets, exact layouts, or brand identity.
- Translate references by site category: a hotel should not become a devtool homepage because Vercel was mentioned.
- Keep citations in final answers when web research materially shaped the recommendation.

## Useful Patterns

- Squarespace: clear business categories, elegant templates, practical conversion paths, image-first clarity.
- Raycast: command surface, fast ergonomic interactions, product UI details, controlled playfulness.
- Linear: dense product realism, restrained glow, workflow clarity, serious speed language.
- Vercel: monochrome precision, strong type, developer trust, minimal surfaces, system clarity.
- Viktor-style motion shorthand: smooth scroll choreography, layered reveals, precise timing, non-template composition.
- Codrops/Awwwards: sticky scenes, masks, WebGL galleries, scroll rhythm, experimental transitions.

## Anti-Patterns

- Copying the visual skin of a reference while ignoring its information structure.
- Combining too many references into an incoherent collage.
- Treating luxury, modern, or cinematic as self-explanatory.
- Using unverifiable creator details as fact.

## QA Checklist

- Check that the final brief has at least three concrete traits and three avoid rules.
- Confirm the chosen reference family matches the site category.
- Verify any current/public claims if the user asked for research.

## Acceptance Criteria

- Another builder could implement the direction without needing the original inspiration link.
- The design borrows principles, not copyrighted assets or exact brand identity.
- The final site can be judged against named traits, not vibes.

## Shared Website Requirements

- Inspect before coding: project structure, framework, homepage/main entry, styling system, interaction/motion system, assets, and available commands.
- Before major changes, explain planned files and wait unless the user clearly says proceed, build, create, implement, fix, continue, or similar.
- Use existing project conventions first; explain major dependencies before adding them.
- Default to premium modern quality without generic SaaS/agency/template patterns.
- Prefer real, generated, or art-directed visuals when the subject benefits from images, video, product UI, or spatial media.
- Build version 1, inspect the rendered result, improve visual quality, then run available checks again.
- Check desktop and mobile. Keep text readable, avoid overlaps, respect focus states and reduced motion.
- Report files changed, commands run, visual checks completed, and anything not tested.
