# Next.js Server Client Boundaries Guide

## Purpose

Protect performance, security, and maintainability by keeping interactivity narrow and intentional.

## Use When

- A Next.js App Router file needs `use client`, browser APIs, event handlers, state, refs, effects, Motion, GSAP, Lenis, or DOM measurement.
- A component fetches data, uses secrets, accesses server-only APIs, or could avoid shipping JavaScript.
- The page feels sluggish or bundle-heavy after adding interactive features.

## Do Not Use When

- The project is not Next.js App Router.
- The task is pure CSS or copy with no component boundary decisions.
- The app intentionally uses another architecture and no migration is requested.

## Discovery Questions

- Which exact elements need client-side state, events, browser APIs, or animation runtime?
- Which data can be fetched on the server close to its source?
- Are props passed into client components serializable?
- Can providers, modals, menus, or animation wrappers sit deeper in the tree?

## Decision Tree

- Start with Server Components for pages, layouts, content, data, and static sections.
- Add `use client` only at the smallest component boundary that needs it.
- Pass server data into Client Components as serializable props.
- Use `children` slots to nest server-rendered content inside client shells such as modals.
- Move providers as deep as possible instead of wrapping the whole document.

## Implementation Rules

- Never expose secrets, tokens, private endpoints, or server-only modules to client bundles.
- Keep animation and interaction components narrow; the whole page should not become a client component for one reveal.
- Prefer server-rendered content for SEO, perceived speed, and lower JavaScript cost.
- Check imports after adding `use client`; everything imported becomes part of the client graph.
- Use client-only effects with cleanup for listeners, observers, timers, and animation instances.

## Useful Patterns

- Server page fetches case-study data, passes title/images to a small animated gallery client component.
- Server layout renders static nav and logo, while a client search/menu island handles interaction.
- Client modal accepts server-rendered `children` content rather than fetching everything again.

## Anti-Patterns

- Adding `use client` to `app/layout.tsx` without a very strong reason.
- Passing functions, class instances, or non-serializable data into Client Components.
- Importing server-only helpers into client files.
- Using Effects to copy server props into redundant state.

## QA Checklist

- Search for `use client` and verify each boundary is justified.
- Inspect bundle or build output if bundle size is a concern.
- Run lint/build to catch server/client import mistakes.
- Manually test interactive islands without breaking route rendering.

## Acceptance Criteria

- Interactive code is narrow, explicit, and cleaned up.
- Server-rendered content stays server-rendered where possible.
- The component boundary improves performance and does not hide generic design shortcuts.

## Shared Website Requirements

- Inspect before coding: project structure, framework, router, homepage or main entry, styling system, JavaScript or motion system, assets, and available commands.
- Prefer the existing project stack and conventions before adding dependencies or moving architecture.
- For Next.js App Router projects, keep Server Components as the default and introduce Client Components only for interactivity, browser APIs, effects, or client-only libraries.
- For React work, keep components pure, derive render data during render, and use Effects only to synchronize with external systems.
- Default website output must still follow the premium visual baseline: strong type, real content, designed states, responsive polish, and no generic card-grid filler.
- Run available lint, build, test, and local browser checks when possible; report exactly what ran and what was not tested.
- Check desktop and mobile behavior when changing visible UI, especially overflow, focus, loading, empty, error, and reduced-motion states.

## Official Source Anchors

- Server and Client Components: https://nextjs.org/docs/app/getting-started/server-and-client-components
- React reference: https://react.dev/reference/react
- You Might Not Need an Effect: https://react.dev/learn/you-might-not-need-an-effect
