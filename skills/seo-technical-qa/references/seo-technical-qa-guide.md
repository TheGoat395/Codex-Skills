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

## Scoped execution

Apply the [shared web contract](../../website-operating-rules/references/scoped-web-contract.md) once when execution crosses phases; reuse it if already read. Load only the specialist guidance relevant to the requested surface and deliverable.

## Official Source Anchors

- Google SEO starter guide: https://developers.google.com/search/docs/fundamentals/seo-starter-guide
- Google sitemaps: https://developers.google.com/search/docs/crawling-indexing/sitemaps/overview
