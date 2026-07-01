# Frontend Quality Audit Checklist

Use this checklist for a complete launch-readiness review. Keep the final report prioritized; do not dump every checklist item if it passed.

## Project And Evidence

- Identify framework, package manager, scripts, routes, styling system, deployment target, and preview URL.
- Run available lint, build, test, typecheck, or preview commands when appropriate.
- Capture exact evidence for claims: file paths, URLs, screenshots, console errors, network failures, viewport sizes, or command output.
- Separate verified issues from risks that were inferred from source only.

## First Impression

- First viewport communicates what the product, service, person, or page is.
- Primary action is visible, specific, and credible.
- Visual subject is present when the page benefits from product, place, person, media, or UI imagery.
- Layout avoids generic centered hero plus repetitive feature cards unless the brief truly calls for it.
- Typography scale fits the container and does not overflow on mobile or tablet.

## Responsive And Layout

- Test common widths: mobile, tablet, laptop, and desktop.
- Check horizontal overflow, clipped controls, awkward wrapping, and excessive whitespace.
- Verify navigation, menus, forms, sticky elements, modals, carousels, and media at mobile sizes.
- Confirm tap targets are large enough and controls are not crowded.
- Check image crops, video posters, screenshot framing, and canvas/WebGL fallback behavior.

## Accessibility

- Use semantic elements where possible.
- Confirm one logical `h1` and a sensible heading order.
- Check form labels, help text, validation errors, required states, and autocomplete.
- Confirm visible focus states and keyboard access for menus, dialogs, tabs, accordions, and custom controls.
- Verify contrast for body text, muted text, buttons, links, badges, and form states.
- Provide alt text or captions for meaningful media.
- Respect `prefers-reduced-motion` for large motion, parallax, scroll scenes, and looping effects.

## Performance

- Look for oversized images, unoptimized videos, missing dimensions, layout shift, lazy-loading mistakes, and heavy background media.
- Check font loading, third-party scripts, hydration cost, animation loops, scroll handlers, and unnecessary client bundles.
- Flag likely Core Web Vitals risks: LCP, INP, CLS, and excessive main-thread work.
- Prefer concrete budgets when the project already defines them.

## SEO And Sharing

- Check title, description, canonical URL, Open Graph/Twitter metadata, favicon, robots, sitemap, and structured data when relevant.
- Verify crawlable page content, descriptive links, image alt text, and non-duplicative headings.
- Flag accidental `noindex`, broken canonical URLs, missing social preview images, and JavaScript-only critical content.

## Interaction States

- Inspect hover, focus, active, disabled, loading, error, success, empty, offline, and retry states.
- Confirm buttons and links look and behave differently.
- Check forms, checkout, booking, newsletter, search, filtering, and dashboard actions.
- Verify destructive or irreversible actions have appropriate confirmation or undo behavior.

## Content And Trust

- Remove placeholder copy, vague claims, unsupported metrics, fake testimonials, and generic AI phrasing.
- Check CTA specificity and whether the user can understand the next step.
- Confirm pricing, contact, booking, support, legal, privacy, and security signals where expected.
- Verify testimonials, logos, case studies, and proof points are credible and not overused decoration.

## Final Judgment

- **Ship** only when no blockers or high-risk trust issues remain.
- **Ship after fixes** when issues are limited, understood, and quick to address.
- **Do not ship yet** when core flows, accessibility, mobile layout, performance, or trust signals are materially broken.
