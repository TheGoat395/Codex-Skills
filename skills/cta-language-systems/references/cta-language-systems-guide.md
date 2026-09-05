# CTA Language Systems Guide

## Purpose

- Make every action label tell users what happens next.

## Discovery Questions

- What happens after the click?
- What commitment or risk does the action imply?
- What stage is the user in: explore, compare, try, buy, book, contact, subscribe?
- Does the CTA match the destination page/state?

## Implementation Rules

- Use verb-led labels tied to the actual next step.
- Do not use Learn More as the default.
- Make primary and secondary actions distinct.
- Avoid pressure, fake urgency, or misleading free language.
- Keep labels short enough for mobile but specific enough to trust.

## Useful Patterns

- Start free, View pricing, Book a table, Check availability, Copy install, Read docs, Request quote, Join waitlist.
- Secondary CTAs: See how it works, Compare plans, View rooms, Browse work.
- Risk-reducing helper text below high-commitment CTAs.
- State-specific CTAs for sold-out, beta, unavailable, or contact-sales flows.

## Anti-Patterns

- Submit.
- Click here.
- Unlock now.
- Learn more everywhere.
- Free trial CTA when credit card is required but undisclosed.

## QA Checklist

- Click through mentally and verify label matches destination.
- Check mobile button fit.
- Audit repeated CTA language across page.
- Add helper text for high-risk actions.

## Acceptance Criteria

- Users know what each action does.
- Primary action hierarchy is clear.
- CTA copy is honest and conversion-aware.

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
