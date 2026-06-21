# Final Client Handoff Guide

## Purpose

- Give the user a calm, accurate closeout they can trust and act on.

## Discovery Questions

- What changed?
- What commands and browser checks actually ran?
- Where can the user view the result?
- What is not tested or still risky?
- What next steps are genuinely useful?

## Implementation Rules

- Keep handoff concise and evidence-based.
- Do not hide failed commands or skipped tests.
- Include URLs and file links when useful.
- Mention env vars without secret values.
- Avoid ending with vague optional fluff.

## Useful Patterns

- Changed files, commands run, local/deployed URL, verification, not tested, next risk.
- Design summary plus QA summary.
- Deployment handoff with production URL and smoke checks.
- CMS/env handoff with safe variable names and editor notes.

## Anti-Patterns

- All done, no details.
- Claims browser QA ran when it did not.
- Secret values in summary.
- Ten speculative next steps.

## QA Checklist

- Cross-check final answer against tool outputs.
- Confirm no running sessions are needed.
- Report failed/skipped checks.
- Use concise file links.

## Acceptance Criteria

- The user knows what changed and how it was verified.
- Risks are honest.
- The handoff is short enough to be useful.

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
- Vercel deployments: https://vercel.com/docs/deployments
- Vercel environment variables: https://vercel.com/docs/environment-variables
- GitHub Pages: https://docs.github.com/en/pages
