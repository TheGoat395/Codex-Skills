# Stack Recipes

## New Luxury/Cinematic Site

Use this when there is no existing repo and the target is a polished marketing, portfolio, brand, or product site.

```bash
npx create-next-app@latest site --typescript --tailwind --eslint --app --src-dir
cd site
npm install motion gsap lenis lucide-react clsx tailwind-merge
npm install three @react-three/fiber @react-three/drei
npm install -D @playwright/test
```

Add only what the concept needs. Skip Three/R3F for editorial sites that are better served by photography/video. Skip GSAP when Motion and CSS cover the interaction.

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

- `npm run lint`
- `npm run build`
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
