---
name: frontend-quality-auditor
description: Audit frontend websites and apps before launch. Use for production-readiness reviews, visual polish checks, responsive QA, accessibility risks, performance and SEO basics, interaction states, forms, media, copy clarity, trust signals, and ship/no-ship recommendations for React, Next.js, static sites, dashboards, landing pages, portfolios, and product UI.
---

# Frontend Quality Auditor

Use this skill to decide whether a frontend is ready to ship and what should be fixed first.

## Core Contract

Produce a concise, evidence-based quality report. Do not redesign the product unless the user explicitly asks for fixes. The default output is an audit, not a rebuild.

## Audit Workflow

1. Identify the project type, framework, entry routes, styling system, scripts, and available preview or deployment URL.
2. Inspect source structure first, then inspect rendered output when a browser or screenshot workflow is available.
3. Review desktop and mobile breakpoints before judging visual quality.
4. Check the launch-critical surfaces: hero or first screen, navigation, primary CTA, forms, media, interactive states, footer, error/loading/empty states, and any checkout, booking, pricing, or dashboard flows.
5. Classify issues by severity:
   - **Blocker**: likely broken, inaccessible, misleading, unusable, or launch-damaging.
   - **High**: visibly unprofessional, confusing, slow, fragile, or trust-reducing.
   - **Medium**: polish, consistency, or resilience issue worth fixing soon.
   - **Low**: minor refinement that should not block launch.
6. Recommend the smallest useful next action for each meaningful issue.
7. End with a clear **Ship**, **Ship after fixes**, or **Do not ship yet** judgment.

## Review Areas

- **Visual polish**: hierarchy, spacing, typography, alignment, density, color, contrast, icon use, media treatment, empty space, and generic AI-looking patterns.
- **Responsive behavior**: mobile composition, tablet layout, overflow, touch targets, nav behavior, media crops, and text wrapping.
- **Accessibility**: semantic structure, headings, labels, focus states, keyboard paths, alt text, contrast, reduced motion, ARIA misuse, and modal/menu behavior.
- **Performance**: image and video weight, layout shift risk, font loading, animation cost, bundle hints, third-party scripts, and Core Web Vitals concerns.
- **SEO and sharing basics**: title, description, canonical, Open Graph, heading order, crawlable content, image alt text, sitemap/robots signals when relevant.
- **Interaction quality**: hover, focus, active, disabled, loading, error, success, offline, retry, and empty states.
- **Content and trust**: vague claims, placeholder copy, weak CTAs, unsupported proof, unclear pricing or contact flows, missing legal or support signals where expected.

## Use Specialist Skills When Available

Route deep follow-up work to focused skills instead of bloating this audit:

- `browser-inspection-workflow` for rendered browser inspection and evidence capture.
- `visual-polish-qa` or `responsive-visual-polish-qa` for visual fixes.
- `mobile-responsive-qa` for phone and tablet layout issues.
- `accessibility-audit-websites` for detailed accessibility remediation.
- `performance-audit-websites` or `performance-budget-lab` for speed and Core Web Vitals.
- `seo-technical-qa` for launch SEO checks.
- `cross-browser-qa` for browser compatibility.
- `anti-generic-website-review` for generic AI output and weak design patterns.
- `content-pruning-review`, `non-generic-web-copy`, or `cta-language-systems` for copy and conversion clarity.

## Output Format

Use this structure unless the user asks for something else:

1. **Verdict**: Ship, ship after fixes, or do not ship yet.
2. **Top Risks**: The 3-5 issues most likely to affect users or trust.
3. **Findings**: Severity, location, evidence, impact, and recommended fix.
4. **Quick Wins**: Small improvements with high visible payoff.
5. **Specialist Follow-Ups**: Which focused skills or checks should be run next.
6. **Verification Notes**: Commands, URLs, viewports, screenshots, and checks actually performed.

Read `references/audit-checklist.md` for the full checklist when performing a complete launch-readiness review.
