# SEO Technical QA Guide

## Purpose

- Help search engines and shared previews understand the same page users see.

## Discovery Questions

- Which pages should be indexed?
- Do titles/descriptions/canonicals match visible content?
- Is there a sitemap/robots strategy?
- Does structured data reflect visible facts only?
- Can important content be crawled?

## Implementation Rules

- Do not add structured data for invisible or fake content.
- Avoid accidental noindex/robots blocks.
- Use unique useful titles and descriptions.
- Check canonicals and sitemap URLs after deployment.
- Make important content accessible without hidden client-only failure.

## Useful Patterns

- Metadata inventory for key routes.
- Sitemap/robots/canonical check.
- Open Graph/social preview check.
- Structured data validation for product/event/local/article pages.

## Anti-Patterns

- Homepage metadata copied to every page.
- Staging noindex shipped to production.
- Structured data claims invisible reviews/prices.
- Sitemap points to localhost or preview URL.

## QA Checklist

- Inspect rendered head and source where relevant.
- Check sitemap and robots files.
- Verify canonical/deployed domain.
- Run available SEO/structured-data tools or document skipped checks.

## Acceptance Criteria

- Indexable pages expose accurate metadata and crawl paths.
- No obvious technical SEO blockers remain.
- SEO claims match visible content.

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

- Google SEO starter guide: https://developers.google.com/search/docs/fundamentals/seo-starter-guide
- Google sitemaps: https://developers.google.com/search/docs/crawling-indexing/sitemaps/overview
