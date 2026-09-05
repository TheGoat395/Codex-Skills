> Evidence age and interpretation: this file preserves the original dated research account. Its historical inspection statements are not recertified by the current installation. The 20 repeated `visual_study` objects are generic synthesis, not 20 distinct item-level observations. See `catalog-provenance-overlay.json` for exact known-path recovery checks and unresolved evidence. Do not invent new per-video observations or infer that historical inspection never happened.

# MotionSites and Viktor Oddy evidence

Verified from live public sources on 2026-08-16. Counts are a dated snapshot and must be refreshed before being described as current later.

## Connected primary sources

- [MotionSites](https://motionsites.ai/) and its [section catalog](https://motionsites.ai/sections)
- [MotionSites Academy](https://motionsites.ai/academy)
- [Viktor Oddy on X](https://x.com/viktoroddy)
- [Viktor Oddy on YouTube](https://www.youtube.com/@ViktorOddy), channel ID `UCYrXebwbK6IE--7z4JJE5mA`
- [DesignRocket](https://designrocket.io/)

MotionSites links to the Viktor Oddy YouTube channel. Treat this as a verified connected creator/product source set.

## Public catalog audit

- 440 unique public catalog metadata records: 147 marked free and 293 marked paid.
- 330 records exposed at least one public preview URL; 110 exposed no public preview.
- 445 distinct public preview assets were available because some records exposed both image and video.
- All 445 public assets were downloaded successfully for visual inspection: 277 WebP, 143 MP4, 14 PNG, 5 HLS playlists, 5 GIF, and 1 JPEG; 618,670,727 bytes total.
- A still was rendered from every asset and all nine contact sheets were inspected.
- Dominant catalog types were hero sections, mobile views, feature sections, calls to action, footers, about sections, and carousels.

The live app retrieves some prompt bodies through access and usage gates. Preserve exact prompts supplied by the user or present in a user-owned repository. Where exact text is not locally available, use the independently written reconstruction and label it accurately.

## Academy audit

The live app exposed four lesson routes and eight named tutorials. Three lessons contained detailed public build prompts; the fourth documented a shorter image-to-3D-to-Three.js workflow.

Reusable prompt characteristics:

- specify framework, language, styling, and motion stack;
- define exact page structure, visual hierarchy, type, palette, and interaction states;
- state animation timing, scroll mapping, asset behavior, and responsive rules;
- include performance constraints such as frame caching, device-pixel-ratio bounds, and fallbacks;
- use references as input while requiring an original composition and business-specific copy.

## Viktor YouTube corpus audit

- 163 public-channel entries inventoried.
- 156 inspected through available English transcripts.
- 6 public videos had no English caption track.
- 1 entry was members-only.
- 392,548 normalized transcript words inspected.

The corpus repeatedly connects visual direction and motion with AI-assisted production, Figma, prompts, scroll, Framer, mobile treatment, client work, pricing, portfolios, agency positioning, testing, SEO, conversion, and delivery. This is transcript-level coverage, not a claim of frame-by-frame inspection of all 163 videos.

### Frame-based visual studies

- 20 public videos were sampled with four real frames each at approximately 8%, 34%, 64%, and 90% of runtime.
- The frame contacts were visually inspected after replacing an unusable MHTML/storyboard attempt; the current evidence contains real browser, design-tool, prompt, build, and rendered-site frames rather than placeholder color bands.
- Machine-readable records live in `references/viktor-visual-studies.json`; the global research copy is under `~/.codex/toolchains/enterprise-web/research/viktor-oddy-public-corpus/`.
- Treat the sampled frames as bounded evidence of those moments, not as proof that every full-resolution frame of every video was watched.

## Three-tier prompt output layer

- `sellable-web-prompts` searches 1,320 reusable prompt/spec outputs: 440 MotionSites-grounded original reconstructions at each of the three defined sellable tiers.
- Tier 1 is regular wow-effect; Tier 2 is agency/SaaS; Tier 3 is enterprise design.
- Every variant carries a public Refero style-system overlay, its source mode, its visual-confidence boundary, and a tier-specific delivery/verification gate.
- Eleven existing prompt or demo records from a user-owned `Codex-Skills` repository are indexed separately as exact user-owned sources. They remain visually unqualified until inspected.

Use `sellable-web-prompts stats`, `sellable-web-prompts search "<concept>" --tier <1|2|3>`, and `sellable-web-prompts show <source-id> --tier <1|2|3>`.

## Refero public style-system layer

- The local public catalog contains 1,290 style records and 51 public design/prompt collection records captured from the public sitemaps.
- Each style record retains its visual north star, typography, color roles, components, do rules, do-not rules, public screenshot, and public source page.
- Search and export with `refero-style-catalog`. This is a local public-reference database, not Refero's private server or account backend.
- No legal, privacy, terms, account, admin, or private extraction-service page is part of this catalog.

## Supplementary public footprint

- [Framer Community](https://www.framer.com/%40viktor-odainyi/) verifies Viktor Oddy as an Expert and currently lists three gallery sites: Syneo AI, GlobaChain, and Nexaloom AI. Syneo was live but contained substantial placeholder and duplicated content; the other two current direct domains were not fetchable during the audit. Use these as visual portfolio leads, not Tier 2 or Tier 3 delivery proof.
- [Dribbble](https://dribbble.com/Viktor_product_design) currently rendered 24 public shots spanning landing pages, mobile UI, web3, dashboards, and agency/product concepts.
- Viktor's public [Medium feed](https://medium.com/feed/@viktoroddy) contained one story. Its strongest reusable rule is to animate only high-leverage assets that communicate or teach; its quantitative marketing claims were not independently validated.
- [DesignRocket](https://designrocket.io/) publicly describes a 50-plus-lesson AI-design curriculum covering page blueprints, Figma-to-AI workflows, multi-page apps, mobile, CMS, search, templates, motion backgrounds, launch checklists, and selling websites. Course/template bodies remain hosted and paid; the public sales page is reference evidence, not installed course access.
- Viktor's X profile and the supplied public $15K tutorial post were verified through live search. The complete historical X timeline was not enumerable through the unauthenticated public surface, so do not claim every X post was inspected.

## Visual and build rules extracted

- Lead with one art-directed concept, not a pile of effects.
- Use oversized editorial type, high-contrast hierarchy, and restrained interface chrome.
- Make imagery, product UI, 3D, or video carry the narrative instead of decorating empty copy.
- Choreograph scroll in scenes with a clear before, transition, and resolved state.
- Use layered depth, masks, controlled parallax, material/light treatment, and tactile microinteractions selectively.
- Give mobile a separate composition and motion budget.
- Preserve reduced motion, readable content, fast first meaning, stable loading, and a non-WebGL fallback.
- For commercial work, add proof, conversion, CMS/integration, ownership, performance, accessibility, and release QA; a striking hero alone is Tier 1, not enterprise delivery.

## Coverage boundary

This evidence covers the discoverable public MotionSites catalog metadata, every public preview asset exposed by that catalog snapshot, the four public lesson routes exposed in the live app, the Viktor YouTube channel inventory/transcript surface, the current Framer gallery listing, the current Dribbble-rendered portfolio surface, the public Medium feed, and the public DesignRocket sales/curriculum page. It does not claim access to paid prompt bodies, members-only video content, paid course/template bodies, private account data, deleted posts, or every historical X post.
