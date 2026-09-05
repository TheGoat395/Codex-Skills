---
name: modern-site-engineering
description: "Integrate systems after frontend direction."
---

# Modern Site Engineering

## Operating Mode

Inspect relevant structure, framework, entry files, styling and interaction systems, and available build commands. Proceed within existing authorization and explain material choices.

## Selected stack

Retain the selected framework and existing package manager. For a new project with an unresolved choice, use `route-enterprise-web-stack`; then select only dependencies required by the actual components. The roles below are optional capabilities, not an installation list.

## Dependency Roles

- Next.js: routing, metadata, optimized images/fonts, production build.
- TypeScript: stable component contracts.
- Tailwind: fast design-system implementation with custom tokens.
- CSS variables: brand colors, spacing, shadows, easing, radii, typography.
- Motion: React-native UI motion, enter/exit, hover/tap, layout transitions.
- GSAP: timeline-driven cinematic sequences, ScrollTrigger, pinned scenes, split text, advanced scroll choreography.
- Lenis: smooth scrolling when the design calls for cinematic scroll.
- Three.js/R3F/Drei: immersive product, material, shader, or spatial scenes.
- lucide-react: icons for controls and clear commands.
- shadcn/ui: accessible component source to customize, not a default visual identity.
- Playwright: visual and interaction verification.

## Build Workflow

1. Inspect project and commands.
2. Reuse the approved visual system; establish type, color, spacing, media and motion only when those decisions are in scope.
3. Build version 1 with real content structure.
4. Run the app locally when possible.
5. Inspect changed visual output in the browser at the requested supported sizes.
6. Correct observed spacing, type, hierarchy, interaction, motion or responsive defects on affected surfaces. Repeat checks after edits or unresolved findings, not by fixed cycle.
7. Run available lint/build/test commands.
8. Report files changed, commands run, and any errors honestly.

## Component Defaults

- Prefer section components with clear names: `Hero`, `FeaturedWork`, `Experience`, `Gallery`, `Offer`, `Journal`, `Contact`.
- Keep layout primitives minimal and reusable.
- Use responsive constraints: `clamp()`, `minmax()`, `aspect-ratio`, stable grid tracks.
- Avoid text overflow by designing for the longest realistic labels.
- Make buttons feel designed: icon placement, focus state, hover state, disabled state.
- Use semantic HTML and accessible labels.
- Respect `prefers-reduced-motion`.

## Motion Defaults

Use CSS transitions for tiny state changes. Use Motion for component/state animation. Use GSAP only when timeline control or scroll choreography is actually needed. Use Three/R3F only when visual concept benefits from spatial or material interaction.

Read `references/stack-recipes.md` when starting a new project or adding dependencies.

## Ownership

Coordinate integration once framework and direction are chosen. Use `route-enterprise-web-stack` only for an unresolved architecture decision. A localized task goes directly to its implementation owner; this skill does not require a new site blueprint or full tool stack.
