---
name: modern-site-engineering
description: Implement beautiful modern websites and web apps with an opinionated premium frontend stack. Use for Next.js, React, Tailwind, Motion, GSAP, Lenis, Three.js/React Three Fiber, shadcn/ui customization, responsive layouts, landing pages, portfolios, cinematic sites, luxury brand sites, Squarespace-like sites, and any frontend build where Codex should produce polished modern UI by default.
---

# Modern Site Engineering

## Operating Mode

Inspect before coding. Identify structure, framework, entry files, styling system, interaction system, and build commands. If the user has not clearly said to proceed, explain planned files before major changes.

## Preferred Stack

For new projects, prefer:

```bash
npx create-next-app@latest <name> --typescript --tailwind --eslint --app --src-dir
npm install motion gsap lenis lucide-react clsx tailwind-merge
npm install three @react-three/fiber @react-three/drei
npm install -D @playwright/test
```

Use existing project tools when working inside an existing repo. Do not add major dependencies without explaining why.

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
2. Define visual system: type, color, spacing, media, motion.
3. Build version 1 with real content structure.
4. Run the app locally when possible.
5. Inspect in browser/screenshots across desktop and mobile.
6. Do a second polish pass for spacing, typography, hierarchy, hover states, motion, and responsiveness.
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
