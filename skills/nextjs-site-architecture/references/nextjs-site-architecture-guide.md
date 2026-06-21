# Next.js Site Architecture Guide

## Lens

Architecture should let the design stay consistent while keeping pages easy to refine.

## Rules

- Inspect existing Next.js version, app/pages router, src directory, styling, and scripts.
- Keep page files as composition once sections grow.
- Use next/font or project-approved font loading.
- Use next/image or appropriate image strategy for real assets.
- Keep client components limited to interactions that need the client.

## Useful Patterns

- src/app/page.tsx for composition.
- src/components/sections for page sections.
- src/components/ui for primitives.
- src/lib/content.ts for structured copy and content.
- src/app/globals.css for tokens and base styles.

## Avoid

- Putting all page logic, content, and styling in one huge file.
- Making the whole app a client component unnecessarily.
- Ignoring metadata and accessible document structure.

## Acceptance Criteria

- The site structure supports iteration and polish.
- Build commands pass or failures are reported honestly.

## Shared Requirements

- Inspect before coding: structure, framework, homepage or main entry file, styling system, JavaScript or interaction system, assets, and build commands.
- Before major changes, explain planned files and wait unless the user clearly says proceed, build, create, implement, or fix.
- Use existing project conventions first. Explain major new dependencies before adding them.
- Never ship generic visual work: no default card grids, placeholder copy, weak type, random gradients, stock-like media, or template heroes.
- Build version 1, inspect the rendered result, improve spacing, type, hierarchy, motion, media, hover states, and responsiveness, then run checks again.
- Run available lint, build, and test commands when possible. Report commands, changed files, and any untested areas honestly.
- Check desktop and mobile. Respect accessibility, semantic markup, focus states, and reduced-motion preferences.
