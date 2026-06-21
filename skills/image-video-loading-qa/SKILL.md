---
name: image-video-loading-qa
description: "Run image and video loading QA. Use after adding or changing images, videos, posters, responsive sources, lazy loading, galleries, hero media, product media, background videos, image sequences, or CMS media to verify loading, dimensions, crops, network errors, alt/captions, and performance."
---

# Image Video Loading QA

Use this skill to make media-rich sites look intentional instead of broken, cropped, or slow.

## Workflow

1. Inspect the project, scripts, routes, local/deployed URL, production surfaces, and available QA/deployment tooling.
2. Read [Image Video Loading QA Guide](references/image-video-loading-qa-guide.md) before claiming the site is ready.
3. Run the narrowest meaningful checks for the risk: visual, mobile, accessibility, performance, forms, media, SEO, analytics, deployment, or handoff.
4. Fix issues when they are in scope; otherwise record exact evidence and remaining risk.
5. Summarize commands, URLs, screenshots/checks, changed files, and what was not tested.

## Always Protect

- Inspect before changing or shipping: framework, package scripts, build output, routes, forms, media, animation stack, deployment target, environment variables, analytics, SEO metadata, accessibility risks, and available browser QA tooling.
- Do not claim something was tested unless it was actually tested; report exact commands, URLs, screenshots, viewports, failures, skipped checks, and remaining risk.
- Verify desktop and mobile rendered output, not only source code. For visual or motion work, inspect screenshots, browser behavior, console errors, network failures, and responsive layout.
- Treat forms, checkout, booking, CMS content, analytics, environment variables, and deployments as production surfaces with error, loading, empty, success, and rollback states.
- Respect accessibility, performance, reduced-motion, and no-JavaScript/no-WebGL/no-autoplay fallbacks where relevant.
- Keep secrets out of code, logs, screenshots, summaries, widgets, and committed files.
- Prefer project-local tooling and existing scripts before adding dependencies. Explain any new dependency before installing it.
- End with a concise handoff: changed files, commands run, checks passed, checks not run, deployment URL if any, and next risks.
