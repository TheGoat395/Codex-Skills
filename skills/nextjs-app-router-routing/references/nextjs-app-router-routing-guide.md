# Next.js App Router Routing Guide

## Purpose

Keep routing clear, idiomatic, and visually useful instead of turning every page into one giant component.

## Use When

- A Next.js project uses or should use the `app/` directory.
- The user asks for a new page, homepage, route, route group, landing page, portfolio route, product route, blog route, or nested layout.
- Navigation state, loading boundaries, route-level errors, or shared UI need to be shaped deliberately.

## Do Not Use When

- The project is plain React, Vite, Astro, static HTML, or another framework without Next.js.
- The app uses the legacy `pages/` router and the user did not ask to migrate.
- The change is only visual styling inside an existing component with no route implications.

## Discovery Questions

- Is the project using `app/`, `pages/`, or both?
- What route should be the homepage or primary entry?
- Which UI should persist across navigation: header, product shell, sidebar, filters, audio/video, or cart?
- Does the route need dynamic params, route groups, loading, error, or not-found states?

## Decision Tree

- If `app/` exists, map route folders before editing.
- If shared UI should persist, place it in the closest stable layout.
- If a segment needs route-level feedback, add scoped `loading`, `error`, or `not-found` files.
- If route organization is for code clarity only, use route groups rather than URL-changing folders.
- If a component only navigates, prefer `Link`; use router hooks only inside Client Components for imperative behavior.

## Implementation Rules

- Keep route files small enough to reveal page intent at a glance.
- Use `page` files for route UI and `layout` files for shared chrome.
- Use route-specific loading and error states that match the visual system, not default text.
- Do not mark layouts as client components just to make one small nav/search/menu interactive.
- Make navigation labels concrete and brand/site-specific.

## Useful Patterns

- `app/(marketing)/page.tsx` for a polished marketing homepage without exposing `(marketing)` in the URL.
- `app/work/[slug]/page.tsx` for case studies or portfolio detail pages.
- `app/dashboard/layout.tsx` for persistent operational chrome and nested dashboard pages.
- Route-level `not-found.tsx` for editorial or commerce detail pages with a designed recovery path.

## Anti-Patterns

- One monster homepage file that contains all routing, layout, data, content, and animation.
- Using Client Components for the whole app because one menu opens.
- Adding folders that accidentally change public URLs.
- Leaving route loading/error/not-found states as raw framework defaults on a premium site.

## QA Checklist

- Check direct URL loads and client-side navigation.
- Confirm shared layouts preserve intended UI state.
- Inspect loading, error, and not-found screens where changed.
- Verify mobile nav and skip/focus behavior across routes.

## Acceptance Criteria

- The route tree matches the product or content model.
- Navigation feels intentional and does not require excess client JavaScript.
- Every touched route has a polished success, loading, and failure path when relevant.

## Shared Website Requirements

- Inspect before coding: project structure, framework, router, homepage or main entry, styling system, JavaScript or motion system, assets, and available commands.
- Prefer the existing project stack and conventions before adding dependencies or moving architecture.
- For Next.js App Router projects, keep Server Components as the default and introduce Client Components only for interactivity, browser APIs, effects, or client-only libraries.
- For React work, keep components pure, derive render data during render, and use Effects only to synchronize with external systems.
- Default website output must still follow the premium visual baseline: strong type, real content, designed states, responsive polish, and no generic card-grid filler.
- Run available lint, build, test, and local browser checks when possible; report exactly what ran and what was not tested.
- Check desktop and mobile behavior when changing visible UI, especially overflow, focus, loading, empty, error, and reduced-motion states.

## Official Source Anchors

- Next.js docs overview: https://nextjs.org/docs
- App Router layouts and pages: https://nextjs.org/docs/app/getting-started/layouts-and-pages
- Server and Client Components: https://nextjs.org/docs/app/getting-started/server-and-client-components
