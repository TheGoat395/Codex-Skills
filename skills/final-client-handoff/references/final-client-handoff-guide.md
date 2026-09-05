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

## Scoped execution

Apply the [shared web contract](../../website-operating-rules/references/scoped-web-contract.md) once when execution crosses phases; reuse it if already read. Load only the specialist guidance relevant to the requested surface and deliverable.

## Official Source Anchors

- Playwright screenshots: https://playwright.dev/docs/screenshots
- Playwright visual comparisons: https://playwright.dev/docs/test-snapshots
- Playwright emulation: https://playwright.dev/docs/emulation
- Vercel deployments: https://vercel.com/docs/deployments
- Vercel environment variables: https://vercel.com/docs/environment-variables
- GitHub Pages: https://docs.github.com/en/pages
