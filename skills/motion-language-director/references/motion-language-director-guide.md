# Motion Language Director Guide

## Purpose

Make animation feel choreographed, purposeful, and appropriate to the brand.

## Use When

- The user asks for animation, motion, cinematic, Framer-like, Viktor-style, scroll effects, GSAP, Lenis, or interactive polish.
- A site needs hover, reveal, page, or scroll motion direction.
- Before choosing GSAP/Motion/Lenis/R3F for a build.

## Do Not Use When

- The UI is a dense utility surface where motion should be minimal.
- The user asks for no animation or strict reduced-motion behavior only.

## Discovery Questions

- What should motion communicate: sequence, depth, focus, state, tactility, speed, drama?
- What motion mood fits: calm, cinematic, crisp, mechanical, liquid, editorial, playful?
- Which library is actually needed: CSS, Motion, GSAP, Lenis, R3F?
- What is the reduced-motion fallback?

## Decision Tree

- If simple hover/state, use CSS first.
- If React component lifecycle/layout transitions, use Motion.
- If scroll choreography/timelines/pinning/masks, use GSAP and official GSAP skills.
- If smooth scroll supports cinematic flow, consider Lenis with accessibility caution.
- If depth/material/space is core, consider R3F/WebGL.

## Implementation Rules

- Define timing, easing, stagger, distance, and purpose before coding.
- Use fewer stronger sequences instead of identical fade-ups everywhere.
- Animate transform, opacity, clip/mask, and shader uniforms before layout properties.
- Never gate content visibility solely on JS-triggered reveal.
- Respect prefers-reduced-motion.

## Useful Patterns

- Luxury: slow clip/fade, subtle parallax, low frequency, quiet easing.
- Productivity/devtool: snappy state changes, crisp hovers, command-like speed.
- Cinematic: pinned scenes, layered depth, text reveals, scroll camera feeling.
- Portfolio: gallery hover, page transitions, project reveal rhythm.

## Anti-Patterns

- Bounce/elastic defaults for serious premium sites.
- Same scroll reveal on every section.
- Scroll hijacking that traps the user.
- Animations that produce jank or content invisibility.

## QA Checklist

- Check reduced-motion behavior.
- Check performance and console errors.
- Check mobile scroll/gesture experience.
- Confirm motion supports hierarchy and does not obscure content.

## Acceptance Criteria

- Every motion choice has a purpose and fallback.
- The animation system feels consistent with the site category.

## Shared Website Requirements

- Inspect before coding: project structure, framework, homepage/main entry, styling system, interaction/motion system, assets, and available commands.
- Before major changes, explain planned files and wait unless the user clearly says proceed, build, create, implement, fix, continue, or similar.
- Use existing project conventions first; explain major dependencies before adding them.
- Default to premium modern quality without generic SaaS/agency/template patterns.
- Prefer real, generated, or art-directed visuals when the subject benefits from images, video, product UI, or spatial media.
- Build version 1, inspect the rendered result, improve visual quality, then run available checks again.
- Check desktop and mobile. Keep text readable, avoid overlaps, respect focus states and reduced motion.
- Report files changed, commands run, visual checks completed, and anything not tested.
