# Content Pruning Review Guide

## Purpose

- Make the page sharper by deleting what dilutes the main decision path.

## Discovery Questions

- What is the page's primary decision?
- Which sections repeat, distract, or lack proof?
- Which claims are unsupported or stale?
- What content is required for legal, trust, SEO, or conversion?

## Implementation Rules

- Cut content that does not support the user's decision.
- Merge repeated sections.
- Replace vague claims with proof or remove them.
- Do not prune required policy/legal/accessibility content.
- Preserve useful SEO content only when it helps humans too.

## Useful Patterns

- Keep: hero promise, proof, key details, objections, action.
- Cut: generic feature cards, repeated benefits, empty mission text, fake testimonials.
- Merge: similar service descriptions, duplicate CTAs, overlapping FAQs.
- Rewrite: unsupported claims into factual statements.

## Anti-Patterns

- Keeping content because the layout needs a section.
- Deleting useful details to look minimal.
- Pruning all SEO/context content.
- Leaving placeholders because they sound polished.

## QA Checklist

- Read headings only and verify no gaps.
- Count repeated claims.
- Check every remaining claim has proof.
- Inspect layout after content removal for awkward holes.

## Acceptance Criteria

- The page is clearer and more specific with required information preserved; reorganization or no deletion may be the correct result.
- Remaining content supports action and trust.
- No required or useful information was lost.

## Scoped execution

Apply the [shared web contract](../../website-operating-rules/references/scoped-web-contract.md) once when execution crosses phases; reuse it if already read. Load only the specialist guidance relevant to the requested surface and deliverable.

## Official Source Anchors

- Plain language guidelines: https://digital.gov/guides/plain-language
- W3C WAI page structure: https://www.w3.org/WAI/tutorials/page-structure/
- W3C WAI forms tutorial: https://www.w3.org/WAI/tutorials/forms/
- Google helpful people-first content: https://developers.google.com/search/docs/fundamentals/creating-helpful-content
- Google SEO starter guide: https://developers.google.com/search/docs/fundamentals/seo-starter-guide
- Google title links: https://developers.google.com/search/docs/appearance/title-link
- Google snippets and meta descriptions: https://developers.google.com/search/docs/appearance/snippet
- MDN meta element: https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/meta
- Open Graph protocol: https://ogp.me/
- Schema.org Organization: https://schema.org/Organization
