# Stack Recipes

## Conditional recipe selection

Use the existing framework and package manager. For a genuinely new Next.js project, verify the current official scaffolder and required options after Next.js is selected; do not run a whole-stack install recipe. Add Motion only for earned React animation, GSAP only for timeline/scroll choreography, Lenis only for a selected smooth-scroll requirement, Three/R3F/Drei only for actual graphics, and browser tooling only when existing tooling cannot verify the result. A localized Vite/React task remains Vite/React.

The directory example below applies only to a Next.js App Router project and is not a required migration for another framework or an existing sound structure.

## Suggested Structure

```txt
src/
  app/
    layout.tsx
    page.tsx
    globals.css
  components/
    layout/
    sections/
    motion/
    ui/
  lib/
    cn.ts
    animation.ts
    content.ts
public/
  images/
  video/
```

## Core Files

- `src/app/globals.css`: tokens, base type, selection, scrollbar, reduced-motion handling.
- `src/app/layout.tsx`: metadata, fonts, body classes.
- `src/app/page.tsx`: page composition only; keep sections separate once the page grows.
- `src/components/sections/*`: art-directed sections.
- `src/components/motion/*`: reusable reveal, parallax, or transition wrappers.
- `src/lib/content.ts`: structured content for easy copy refinement.

## Quality Gates

- Discover available package scripts and use the repository package manager.
- Run relevant lint/type/test/build scripts that actually exist.
- local browser inspection
- mobile viewport inspection
- check reduced motion
- check image/video loading
- check keyboard focus on interactive elements

## Common Libraries

- `motion`: install with `npm install motion`; import React features from `motion/react`.
- `gsap`: use with client components and clean up contexts/timelines.
- `lenis`: initialize in a client component; disable if it harms accessibility.
- `@react-three/fiber`: render `Canvas` only in client components.
- `@react-three/drei`: useful helpers for cameras, environments, loaders, text, and controls.
- `lucide-react`: use for icons in buttons, navigation controls, and tool-like UI.
- `clsx` + `tailwind-merge`: implement a `cn()` helper for class composition.
