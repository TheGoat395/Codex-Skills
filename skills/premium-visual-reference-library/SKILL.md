---
name: premium-visual-reference-library
description: "Find references, Viktor Oddy and MotionSites."
---

# Premium Visual Reference Library

Use this skill to pick reference sources before designing a premium website.

## Workflow

1. Identify the site category: product/devtool, luxury/editorial, portfolio, hospitality, commerce, personal, agency, or content/media.
2. Read [sources.md](references/sources.md) for the relevant source clusters.
3. When the user names a creator, asks for many examples, or uses a style shorthand, also read [creator-and-pattern-index.md](references/creator-and-pattern-index.md) and [creator-methods-evidence.md](references/creator-methods-evidence.md).
4. When Viktor Oddy or MotionSites is named, read [motionsites-viktor-evidence.md](references/motionsites-viktor-evidence.md) and refresh any count or catalog claim that matters to the current project.
5. Select enough distinct references for the open decision; 3–7 is a broad direction-study option, not a quota for a supplied exact reference.
6. Extract concrete patterns: type, layout, density, media, motion, CTA, proof, navigation, section rhythm, and mobile behavior.
7. State what not to copy.
8. When implementation is in scope, add selected traits to the shared build spec; a reference-only request ends with the source-backed study.

## Retrieve only the selected material

Use the bundled read-only helper from any working directory:

```bash
python3 "<skill-root>/scripts/query_catalog.py" --search "reorder" --limit 5
python3 "<skill-root>/scripts/query_catalog.py" --id M-01
```

Resolve `<skill-root>` to this skill's actual installation. Search returns bounded discovery results; exact ID returns the original record with its provenance and limitations. The helper checks source fingerprints against the overlay, makes no external requests and writes nothing. If Python is unavailable, search the named JSON file for the selected ID and read that record plus its matching overlay record; no helper installation is required.

The four raw catalogs preserve 50 author-created style playbooks, 100 implementation leads, 22 dated creator-method interpretations and 20 historical video-study records. Repeated mechanism text is generic inference, not verified example code; repeated video-study text is synthesis, not independent per-video observation. Fixed palette, timing, target-size, frame-time and DPR values are illustrative starting choices, not universal standards or measured budgets. Inspect the selected live source and current technical documentation before relying on its actual behavior. Do not load or recrawl every catalog for one reference.

## Source Fidelity

Preserve exact user-supplied or user-owned prompts when requested. Otherwise use references to understand quality and label independent reconstructions accurately; do not claim third-party brand assets, copy, or unobserved behavior as owned or verified.

Use the matching record in the [catalog provenance overlay](references/catalog-provenance-overlay.json) before item-level evidence claims; the exact-ID helper includes it. Raw catalogs retain all original text/URLs unchanged. The overlay separates dated claims, generalized defaults and currently recoverable evidence. Generic repeated study text is not independently observed per-item evidence. Inspect exact selected references when reusing them; do not recrawl every catalog or assume all historical image paths still resolve.
