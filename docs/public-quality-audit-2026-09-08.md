# Public skill quality audit — 2026-09-08

All 80 public skills were reviewed, including every root, discovery/display metadata file, bundled reference, data catalog, template and executable helper. The collection remains 80 skills. Changes affect 46 skill folders; 34 were deliberately retained after review. This is a content, portability and executable-helper audit, not a claim of universal model improvement.

The baseline is `40bbe413b834db3b77f6be4ceef303d694715f13`. The newer accessibility and optional-specialist fixes already on main were preserved. Source catalogs were read using lossless repeated-text normalization where useful; every record and unique field was included. The four raw reference catalogs and their original fingerprints remain unchanged. No private skill installation, personal configuration or private repository was changed in this pass.

## Material findings and fixes

| Priority | Confirmed issue | Repair and preserved constraint |
|---|---|---|
| High | Some public guides assumed private-only skills or local research CLIs existed. | Added standalone fallbacks and explicit unavailable-tool boundaries; preserved the relevant research and delivery knowledge. |
| High | Installer ignored CODEX_HOME and could follow source symlinks. | Honor selected destination, reject source links and recursive destinations before replacing installed data; preserve per-skill staging and rollback. |
| High | Stitched capture with --force could follow an output symlink. | Reject nonregular/symlink destinations before navigation and again before publication; existing targets remain protected. |
| High | Premium gate and some review workflows still imposed extra plans, edits or broad work. | Conditional preparation, reuse approved direction, preserve analysis-only boundaries and continue authorized implementation through relevant validation. |
| Medium | Metadata validation accepted nested overrides, duplicate/non-string fields; corpus thresholds accepted false/0.0. | Strict required-field handling and explicit scorer contracts, with negative fixtures. This remains a limited scalar parser, not a general YAML parser. |
| Medium | Fourteen roots repeated guide-loading instructions, including authoring instructions irrelevant to execution. | Consolidated each into one conditional guide route. No useful guide content was discarded. |
| Medium | Fourteen display descriptions were excessively long; a style-director prompt contradicted ownership. | Shortened display metadata and aligned the style-director purpose with refining an existing lane. |
| Medium | Motion shorthand overstated keyframe, CSS-variable, swipe and scroll-timeline rules. | Replaced blanket advice with specific conditions and tests; retained purposeful expression, interruption and reduced-motion access. |
| Medium | Large catalogs could enter context for one reference and implied unavailable local tools. | Added bounded search/exact-ID retrieval with source fingerprints and provenance; generic mechanisms remain historical leads, not verified code. |
| Medium | Capture manifests omitted font-settling uncertainty or explicit theme/DPR. | Record these conditions; helpers still return capture-only statuses requiring visual inspection. |
| Medium | Repository inventory lagged earlier main changes and lacked a freshness gate. | Regenerated both inventories and added portability/inventory validation to CI. |

Exact changes are in the commit diff. No skill was removed merely because another model authored it. The original ten agent-quality skills retain distinct jobs: evidence judgment, inference, creative search, research, reconciliation, debugging, verification, evaluation, memory provenance and orchestration.

## Verification actually performed

- Catalog validation and public-package checks pass for all 80 skills, including local references, source links, home-path screening and inventory agreement.
- 26 catalog/installer regressions pass, including replacement recovery, malformed metadata and missing/symlinked inventory.
- Nine helper regression tests pass, covering corpus rejection, collision-reader behavior, catalog retrieval/fingerprints, both evidence migrations and the stitched output guard.
- The bundled draft observer test passes; the 14-case regression corpus validates structurally. No model executed those 14 cases in this audit.
- Both capture helpers executed against an isolated local 2,400-pixel synthetic page: three settled baseline states and seven stitched segments. The resulting composite was visually inspected.
- Both motion HTML templates ran in Chromium at 1,440 and 390 pixels. No horizontal overflow or page exceptions were observed; pause/replay/resume and reduced-motion behavior passed. Relevant desktop/mobile template captures were visually inspected. This is sampled template inspection, not a whole-site accessibility certificate.
- Python and Node syntax checks, installer collection listing/dry run and diff whitespace checks pass.
- Gitleaks found no secrets in the current working tree or 65 commits reachable from the public baseline. Text and link review found no personal workspace data in the skill package; unbundled local-tool assumptions were corrected. This is scoped screening, not proof that no possible sensitive content exists in every repository image, branch or remote service.

Version-sensitive guidance was checked against [Next.js page conventions](https://nextjs.org/docs/app/api-reference/file-conventions/page), [React ViewTransition](https://react.dev/reference/react/ViewTransition), [Tailwind theme variables](https://tailwindcss.com/docs/theme), [Motion layout guidance](https://motion.dev/docs/react-layout-animations), [MDN animation timelines](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/animation-timeline) and [Google Web Vitals](https://web.dev/articles/vitals?hl=en). These checks do not recertify every historical gallery URL or video observation.

## Interaction walkthroughs

These are paper walkthroughs of the revised instructions, not observed model runs.

| Request | Expected instruction/reading path | Actions and boundary | Finish condition |
|---|---|---|---|
| Fix one typo | Applicable project rules and affected text; no design router or full blueprint. | Local edit and decisive check. | Correct text; no unrelated redesign. |
| Database migration | Project database/change rules, relevant schema and recovery sources; web-only skills stay inactive. | Reversible preparation, representative migration checks; retain actual production approval. | Required validation and explicit production state, not just a generated migration file. |
| UI focus repair | Existing component/primitive owner, relevant accessibility guide; reuse design and shared evidence. | Repair when requested, run keyboard/focus and relevant rendered states. | Original defect corrected, regressions checked, actual coverage stated. |
| Failing local test | Systematic debugging plus affected code and meaningful hypothesis tests. | Reproduce, discriminate cause, repair and rerun focused/required checks. | Evidence supports repair or a concrete blocker remains. |
| Deployment requiring approval | Project release rules, relevant build/runtime evidence and recovery target. | Prepare/verify concrete release; stop at the intentional approval boundary. | Authorized deployment read back, or verified preparation clearly marked awaiting approval. |

Additional semantic boundary checks covered exact-source reconstruction, one requested creative concept, optional specialist absence, no-defect design review and historical catalog retrieval. Predicted reductions in redundant reading, confirmations or overtesting remain hypotheses until matched model trials establish them.

## Coverage and retained knowledge

Every row includes the skill root, agents metadata and all files under that skill folder. A retained row means no material edit was justified by this review, not that its domain can never improve. The two evidence validators intentionally remain self-contained copies so either skill can be installed independently without a cross-skill Python dependency.

| Skill | Files | Disposition | Review result |
|---|---:|---|---|
| [accessibility-audit-websites](../skills/accessibility-audit-websites/SKILL.md) | 3 | Retained | Trigger, specialist procedure, evidence and scope reviewed; no material defect identified. |
| [accessibility-performance-polish](../skills/accessibility-performance-polish/SKILL.md) | 3 | Updated | Duplicate guide preload and authoring-only instruction removed; scope and completion clarified. |
| [agent-evaluation-operations](../skills/agent-evaluation-operations/SKILL.md) | 10 | Updated | Optional fixture fallback; folded metadata, missing-root and symlink accounting; strict corpus thresholds/scorer contracts. |
| [agent-memory-provenance](../skills/agent-memory-provenance/SKILL.md) | 2 | Retained | Trigger, specialist procedure, evidence and scope reviewed; no material defect identified. |
| [agent-orchestration-architecture](../skills/agent-orchestration-architecture/SKILL.md) | 2 | Retained | Trigger, specialist procedure, evidence and scope reviewed; no material defect identified. |
| [animation-easing-language](../skills/animation-easing-language/SKILL.md) | 3 | Retained | Trigger, specialist procedure, evidence and scope reviewed; no material defect identified. |
| [animation-jank-qa](../skills/animation-jank-qa/SKILL.md) | 3 | Updated | Concrete trace probes distinguish CPU, layout, raster, decode and lifecycle causes. |
| [animation-tool-router](../skills/animation-tool-router/SKILL.md) | 2 | Retained | Trigger, specialist procedure, evidence and scope reviewed; no material defect identified. |
| [anti-generic-website-review](../skills/anti-generic-website-review/SKILL.md) | 3 | Updated | No defect quota or unconditional redesign of intentional card collections. |
| [brand-voice-to-ui-copy](../skills/brand-voice-to-ui-copy/SKILL.md) | 3 | Updated | Compact display description; substantive specialist guidance retained. |
| [browser-inspection-workflow](../skills/browser-inspection-workflow/SKILL.md) | 3 | Updated | Compact display description; substantive specialist guidance retained. |
| [code-change-safety-checkpoint](../skills/code-change-safety-checkpoint/SKILL.md) | 2 | Retained | Trigger, specialist procedure, evidence and scope reviewed; no material defect identified. |
| [code-change-undo-revert](../skills/code-change-undo-revert/SKILL.md) | 2 | Retained | Trigger, specialist procedure, evidence and scope reviewed; no material defect identified. |
| [color-material-lighting-direction](../skills/color-material-lighting-direction/SKILL.md) | 3 | Updated | Duplicate guide preload and authoring-only instruction removed; scope and completion clarified. |
| [content-pruning-review](../skills/content-pruning-review/SKILL.md) | 3 | Retained | Trigger, specialist procedure, evidence and scope reviewed; no material defect identified. |
| [content-structure-information-architecture](../skills/content-structure-information-architecture/SKILL.md) | 3 | Retained | Trigger, specialist procedure, evidence and scope reviewed; no material defect identified. |
| [conversion-forms-checkout-polish](../skills/conversion-forms-checkout-polish/SKILL.md) | 3 | Retained | Trigger, specialist procedure, evidence and scope reviewed; no material defect identified. |
| [creativity](../skills/creativity/SKILL.md) | 6 | Updated | Public fallback for optional direction specialists; concept count follows the request. |
| [critical-thinking](../skills/critical-thinking/SKILL.md) | 6 | Updated | Assertion calibration works without unbundled honesty skill. |
| [cross-browser-qa](../skills/cross-browser-qa/SKILL.md) | 3 | Updated | Engine-specific scope and compact display metadata. |
| [css-grid-editorial-systems](../skills/css-grid-editorial-systems/SKILL.md) | 3 | Retained | Trigger, specialist procedure, evidence and scope reviewed; no material defect identified. |
| [cta-language-systems](../skills/cta-language-systems/SKILL.md) | 3 | Updated | Compact display description; substantive specialist guidance retained. |
| [deep-research](../skills/deep-research/SKILL.md) | 7 | Updated | Exact-source fidelity with proportional reading; optional execution specialist. |
| [design-motion-principles](../skills/design-motion-principles/SKILL.md) | 16 | Updated | Conditional recipe reading, rendered completion, contextual technical advice, reduced-motion reveal and truthful report guidance. |
| [editorial-typography-systems](../skills/editorial-typography-systems/SKILL.md) | 3 | Updated | Duplicate guide preload and authoring-only instruction removed; scope and completion clarified. |
| [evidence-reconciliation](../skills/evidence-reconciliation/SKILL.md) | 3 | Updated | Affected-source inventory; conditional commercial checks; authority scope clarified. |
| [final-client-handoff](../skills/final-client-handoff/SKILL.md) | 6 | Updated | Compact display description; substantive specialist guidance retained. |
| [frontend-quality-auditor](../skills/frontend-quality-auditor/SKILL.md) | 3 | Updated | No minimum finding count; checklist preserves review-only boundary. |
| [frontend-tooling-trust-gate](../skills/frontend-tooling-trust-gate/SKILL.md) | 2 | Retained | Trigger, specialist procedure, evidence and scope reviewed; no material defect identified. |
| [gsap-performance](../skills/gsap-performance/SKILL.md) | 2 | Retained | Trigger, specialist procedure, evidence and scope reviewed; no material defect identified. |
| [hero-image-art-direction](../skills/hero-image-art-direction/SKILL.md) | 3 | Updated | Compact display description; substantive specialist guidance retained. |
| [image-crop-responsive-qa](../skills/image-crop-responsive-qa/SKILL.md) | 3 | Updated | Review does not implement repairs; compact display metadata. |
| [image-video-loading-qa](../skills/image-video-loading-qa/SKILL.md) | 3 | Updated | Media loading/failure probes replace unrelated QA categories. |
| [logical-thinking](../skills/logical-thinking/SKILL.md) | 6 | Updated | Premise consistency precedes entailed/contradicted/unknown classification. |
| [mobile-responsive-qa](../skills/mobile-responsive-qa/SKILL.md) | 3 | Updated | Input, keyboard occlusion and device-evidence distinctions. |
| [modern-site-engineering](../skills/modern-site-engineering/SKILL.md) | 3 | Retained | Trigger, specialist procedure, evidence and scope reviewed; no material defect identified. |
| [motion-language-director](../skills/motion-language-director/SKILL.md) | 3 | Updated | Duplicate guide preload and authoring-only instruction removed; scope and completion clarified. |
| [motion-performance-qa](../skills/motion-performance-qa/SKILL.md) | 3 | Retained | Trigger, specialist procedure, evidence and scope reviewed; no material defect identified. |
| [motion-react-layout-transitions](../skills/motion-react-layout-transitions/SKILL.md) | 3 | Updated | Version-aware scroll/fixed-root measurement and scale-distortion diagnosis. |
| [motion-react-microinteractions](../skills/motion-react-microinteractions/SKILL.md) | 3 | Retained | Trigger, specialist procedure, evidence and scope reviewed; no material defect identified. |
| [motion-react-page-transitions](../skills/motion-react-page-transitions/SKILL.md) | 4 | Retained | Trigger, specialist procedure, evidence and scope reviewed; no material defect identified. |
| [motion-react-patterns](../skills/motion-react-patterns/SKILL.md) | 3 | Retained | Trigger, specialist procedure, evidence and scope reviewed; no material defect identified. |
| [nextjs-app-router-routing](../skills/nextjs-app-router-routing/SKILL.md) | 3 | Updated | Current async params/searchParams guidance with legacy-version boundary. |
| [nextjs-server-client-boundaries](../skills/nextjs-server-client-boundaries/SKILL.md) | 3 | Retained | Trigger, specialist procedure, evidence and scope reviewed; no material defect identified. |
| [nextjs-site-architecture](../skills/nextjs-site-architecture/SKILL.md) | 3 | Retained | Trigger, specialist procedure, evidence and scope reviewed; no material defect identified. |
| [non-generic-web-copy](../skills/non-generic-web-copy/SKILL.md) | 3 | Updated | Duplicate guide preload and authoring-only instruction removed; scope and completion clarified. |
| [performance-audit-websites](../skills/performance-audit-websites/SKILL.md) | 4 | Updated | Matched measurements and dominant-bottleneck ownership; authorized repairs only. |
| [performance-budget-lab](../skills/performance-budget-lab/SKILL.md) | 2 | Updated | Core metrics distinguished from supporting TTFB diagnostic. |
| [premium-visual-reference-library](../skills/premium-visual-reference-library/SKILL.md) | 12 | Updated | Bounded exact-ID/search helper with fingerprinted provenance; remove unbundled tool assumptions. |
| [premium-web-build-gate](../skills/premium-web-build-gate/SKILL.md) | 3 | Updated | Compact conditional root; preserved detailed build guidance behind a reference. |
| [radix-accessible-primitives](../skills/radix-accessible-primitives/SKILL.md) | 3 | Retained | Trigger, specialist procedure, evidence and scope reviewed; no material defect identified. |
| [react-accessible-components](../skills/react-accessible-components/SKILL.md) | 3 | Retained | Trigger, specialist procedure, evidence and scope reviewed; no material defect identified. |
| [react-component-composition](../skills/react-component-composition/SKILL.md) | 3 | Retained | Trigger, specialist procedure, evidence and scope reviewed; no material defect identified. |
| [react-component-craft](../skills/react-component-craft/SKILL.md) | 3 | Retained | Trigger, specialist procedure, evidence and scope reviewed; no material defect identified. |
| [react-error-loading-empty-states](../skills/react-error-loading-empty-states/SKILL.md) | 3 | Retained | Trigger, specialist procedure, evidence and scope reviewed; no material defect identified. |
| [react-form-patterns](../skills/react-form-patterns/SKILL.md) | 3 | Retained | Trigger, specialist procedure, evidence and scope reviewed; no material defect identified. |
| [react-responsive-components](../skills/react-responsive-components/SKILL.md) | 3 | Retained | Trigger, specialist procedure, evidence and scope reviewed; no material defect identified. |
| [react-state-and-effects-discipline](../skills/react-state-and-effects-discipline/SKILL.md) | 3 | Retained | Trigger, specialist procedure, evidence and scope reviewed; no material defect identified. |
| [reduced-motion-design](../skills/reduced-motion-design/SKILL.md) | 3 | Retained | Trigger, specialist procedure, evidence and scope reviewed; no material defect identified. |
| [responsive-visual-polish-qa](../skills/responsive-visual-polish-qa/SKILL.md) | 3 | Updated | Duplicate guide preload and authoring-only instruction removed; scope and completion clarified. |
| [section-layout-systems](../skills/section-layout-systems/SKILL.md) | 3 | Updated | Duplicate guide preload and authoring-only instruction removed; scope and completion clarified. |
| [seo-technical-qa](../skills/seo-technical-qa/SKILL.md) | 3 | Updated | HTTP/indexability/canonical/source scope replaces generic QA list. |
| [surface-shadow-material-systems](../skills/surface-shadow-material-systems/SKILL.md) | 3 | Updated | Compact display description; substantive specialist guidance retained. |
| [systematic-debugging](../skills/systematic-debugging/SKILL.md) | 3 | Updated | Focused reproduction and required gates; broader checks tied to risk. |
| [tailwind-design-tokens](../skills/tailwind-design-tokens/SKILL.md) | 3 | Retained | Trigger, specialist procedure, evidence and scope reviewed; no material defect identified. |
| [tailwind-responsive-layouts](../skills/tailwind-responsive-layouts/SKILL.md) | 3 | Retained | Trigger, specialist procedure, evidence and scope reviewed; no material defect identified. |
| [testimonial-proof-systems](../skills/testimonial-proof-systems/SKILL.md) | 3 | Updated | Compact display description; substantive specialist guidance retained. |
| [ui-primitives-shadcn-lucide](../skills/ui-primitives-shadcn-lucide/SKILL.md) | 3 | Retained | Trigger, specialist procedure, evidence and scope reviewed; no material defect identified. |
| [ui-screenshot-composition](../skills/ui-screenshot-composition/SKILL.md) | 3 | Updated | Compact display description; substantive specialist guidance retained. |
| [verification-before-completion](../skills/verification-before-completion/SKILL.md) | 2 | Retained | Trigger, specialist procedure, evidence and scope reviewed; no material defect identified. |
| [visual-assets-direction](../skills/visual-assets-direction/SKILL.md) | 3 | Updated | Duplicate guide preload and authoring-only instruction removed; scope and completion clarified. |
| [visual-polish-qa](../skills/visual-polish-qa/SKILL.md) | 3 | Retained | Trigger, specialist procedure, evidence and scope reviewed; no material defect identified. |
| [visual-regression-lab](../skills/visual-regression-lab/SKILL.md) | 6 | Updated | Comparable capture scope, no edit quota, symlink destination refusal and explicit settling metadata. |
| [web-design-direction-system](../skills/web-design-direction-system/SKILL.md) | 3 | Updated | No mandatory router or dials; zero-finding outcomes allowed; public attribution corrected. |
| [web-design-vocabulary](../skills/web-design-vocabulary/SKILL.md) | 3 | Updated | Duplicate guide preload and authoring-only instruction removed; scope and completion clarified. |
| [web-imagegen-prompting](../skills/web-imagegen-prompting/SKILL.md) | 3 | Updated | Compact display description; substantive specialist guidance retained. |
| [web-reference-research](../skills/web-reference-research/SKILL.md) | 6 | Updated | Single guide route; exact-fidelity records need no forced originality change. |
| [web-style-director](../skills/web-style-director/SKILL.md) | 3 | Updated | Metadata, guide and root consistently refine an existing lane. |
| [website-blueprint-first](../skills/website-blueprint-first/SKILL.md) | 3 | Updated | Duplicate guide preload and authoring-only instruction removed; scope and completion clarified. |
| [website-operating-rules](../skills/website-operating-rules/SKILL.md) | 5 | Updated | Portable tier/release fallback; cross-phase scope; duplicate guide preload removed. |

## Measured instruction delivery

The combined 80 root SKILL.md files went from 158,088 to approximately 153,700 characters (about 2.8% less), while retaining detailed references. This measures stored root text, not the context loaded in a typical task. The selected M-01 catalog record plus provenance is 1,446 output characters; the helper avoids dumping whole catalogs for that lookup. Neither figure measures token billing, model intelligence or end-to-end efficiency.

Historical Git author identities remain in shared history; this pass does not rewrite prior commits or claim their metadata is anonymous. New audit commits use a GitHub no-reply identity.

## Limits and rollback

No comparative Astra/Sol/Luna evaluation or account-usage benchmark was run. Fewer active characters and narrower retrieval are measurable delivery changes; higher answer quality, faster completion and quota savings are not yet quantified. No statement here certifies every browser, framework version, external source or production use case.

Use the repository commit/PR to review or revert this batch. Existing release archives remain immutable snapshots and may predate current main. Do not overwrite a personalized installation with the public collection merely to reproduce this audit; evaluate the relevant changes first.
