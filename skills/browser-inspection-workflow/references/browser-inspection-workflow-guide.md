# Browser Inspection Workflow Guide

## Purpose

- Make rendered-browser inspection a default part of shipping frontend work.

## Discovery Questions

- What URL or local server should be inspected?
- Which pages, modals, menus, forms, media, and interactions are critical?
- What browser/device sizes matter?
- Which errors are known versus new?

## Implementation Rules

- Inspect rendered output after substantial UI changes.
- Check console and failed requests.
- Test links/buttons/forms, not just static appearance.
- Use screenshots for visual claims.
- Report what was not inspectable.

## Useful Patterns

- Local dev server plus Playwright/Chrome inspection.
- Desktop and mobile smoke path through homepage, nav, CTA, form.
- Console/network capture before final answer.
- Screenshot proof for hero, mid-page, and mobile menu.

## Anti-Patterns

- Final says polished without opening the site.
- Console errors ignored.
- Only source code reviewed.
- Mobile nav or form never clicked.

## QA Checklist

- Open page, wait for assets, inspect console/network.
- Interact with nav, CTAs, forms, and media.
- Capture screenshots at key viewports.
- Fix or report visible defects.

## Acceptance Criteria

- Rendered browser behavior matches the intended design.
- Console/network issues are fixed or documented.
- The final report reflects actual inspection.

## Shared Website Requirements

- Inspect before changing or shipping: framework, package scripts, build output, routes, forms, media, animation stack, deployment target, environment variables, analytics, SEO metadata, accessibility risks, and available browser QA tooling.
- Do not claim something was tested unless it was actually tested; report exact commands, URLs, screenshots, viewports, failures, skipped checks, and remaining risk.
- Verify desktop and mobile rendered output, not only source code. For visual or motion work, inspect screenshots, browser behavior, console errors, network failures, and responsive layout.
- Treat forms, checkout, booking, CMS content, analytics, environment variables, and deployments as production surfaces with error, loading, empty, success, and rollback states.
- Respect accessibility, performance, reduced-motion, and no-JavaScript/no-WebGL/no-autoplay fallbacks where relevant.
- Keep secrets out of code, logs, screenshots, summaries, widgets, and committed files.
- Prefer project-local tooling and existing scripts before adding dependencies. Explain any new dependency before installing it.
- End with a concise handoff: changed files, commands run, checks passed, checks not run, deployment URL if any, and next risks.

## Official Source Anchors

- Playwright screenshots: https://playwright.dev/docs/screenshots
- Playwright visual comparisons: https://playwright.dev/docs/test-snapshots
- Playwright emulation: https://playwright.dev/docs/emulation
- web.dev Web Vitals: https://web.dev/articles/vitals
- MDN Performance API: https://developer.mozilla.org/en-US/docs/Web/API/Performance_API
