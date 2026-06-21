---
name: browser-inspection-workflow
description: "Run browser inspection for websites and apps. Use after building or changing frontend work to open the rendered site, inspect console and network errors, verify layout and interactions, test links/forms/media, capture screenshots, check responsive behavior, and perform the second visual polish pass before final delivery."
---

# Browser Inspection Workflow

Use this skill to make rendered-browser inspection a default part of shipping frontend work.

## Workflow

1. Inspect the project, scripts, routes, local/deployed URL, production surfaces, and available QA/deployment tooling.
2. Read [Browser Inspection Workflow Guide](references/browser-inspection-workflow-guide.md) before claiming the site is ready.
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
