# Accessibility Audit Websites Guide

## Purpose

- Make sites usable for more people and prevent polished visuals from hiding broken interaction.

## Discovery Questions

- What interactive controls and forms exist?
- Can the page be navigated by keyboard?
- Are headings, labels, alt text, and landmarks meaningful?
- Does motion/media need reduced-motion or captions?

## Implementation Rules

- Do not rely only on automated audits.
- Prefer semantic HTML over ARIA patches.
- Make focus visible and logical.
- Label every form control.
- Ensure important information is not image/video-only.

## Useful Patterns

- Keyboard pass: tab order, menus, dialogs, forms, CTAs.
- Screen-reader structure pass: headings, landmarks, labels.
- Media pass: alt text, captions, reduced motion.
- Contrast/focus pass for controls and links.

## Anti-Patterns

- Icon buttons without accessible names.
- Placeholder-only form labels.
- Hover-only content.
- Focus outline removed without replacement.

## QA Checklist

- Run available automated tools if present.
- Manually test keyboard navigation.
- Inspect accessible names/labels.
- Check motion/media alternatives.

## Acceptance Criteria

- Core content and actions are accessible by keyboard and assistive tech patterns.
- Forms and controls are named and understandable.
- Known accessibility gaps are fixed or reported.

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

- WCAG 2.2: https://www.w3.org/TR/WCAG22/
- MDN form validation: https://developer.mozilla.org/en-US/docs/Learn_web_development/Extensions/Forms/Form_validation
