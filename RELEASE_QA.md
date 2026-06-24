# Release QA

This document records the practical checks for the public Codex Premium Website Skills release. It is not a legal audit and does not replace measured benchmarks, but it gives reviewers a clear view of what has been packaged and verified.

## Current Release State

- Default public core: `70` skills.
- Showcase demos: `9` local preview demos.
- Showcase ZIP deliverables: `9` demo ZIP files.
- Provider/account integrations: excluded from the public core pending separate review.
- Formal measured benchmarks: planned.
- Projected benchmark estimate: included under `examples/benchmarks/premium-website-workflow-estimate/`.

## Repository Structure Checks

| Check | Expected State | Status |
|---|---|---|
| Root README introduces the project and showcase | `README.md` describes the unofficial public skill library and points to the demo gallery | Done |
| Install instructions exist | `INSTALL.md` documents dry-run install, install, focused collection install, and local preview | Done |
| Demo index exists | `DEMOS.md` lists the confirmed demo set and preview paths | Done |
| Security policy exists | `SECURITY.md` describes installer behavior and safe-use expectations | Done |
| Skill quality standard exists | `SKILL_QUALITY_STANDARD.md` defines acceptance and rejection criteria | Done |
| Third-party notices exist | `THIRD_PARTY_NOTICES.md` defines notice expectations and excluded integrations | Done |
| Benchmark standards exist | `BENCHMARKS.md` distinguishes projected estimates from measured benchmarks | Done |
| Application draft exists | `OPEN_SOURCE_APPLICATION_DRAFT.md` includes the public-core, showcase, and benchmark-estimate story | Done |

## Skill Inventory Checks

| Check | Expected State | Status |
|---|---|---|
| Public core count | `curated_collections.json` defines a 70-skill public core | Done |
| Manifest count | `manifest.json` reports `"skill_count": 70` | Done |
| Inventory count | `SKILL_INVENTORY.md` reports `Total skills: 70` | Done |
| Public release checklist exists | `PUBLIC_RELEASE_CHECKLIST.md` documents release checks before publishing | Done |

## Showcase Checks

| Check | Expected State | Status |
|---|---|---|
| Gallery page exists | `examples/premium-website-showcase/gallery/index.html` | Done |
| Demo manifest exists | `examples/premium-website-showcase/demo-manifest.json` | Done |
| Demo README exists | `examples/premium-website-showcase/README.md` | Done |
| Packaging script exists | `examples/premium-website-showcase/scripts/package_demos.py` | Done |
| Preview files exist | 9 `preview.html` files under `examples/premium-website-showcase/demos/` | Done |
| Demo ZIP files exist | 9 ZIP files under `examples/premium-website-showcase/demo-zips/` | Done |

## Showcase Demo Set

The confirmed showcase demos are:

1. Asteria Capital
2. Asteria Space Travel
3. Mainframe Contact Hero
4. VEX Hero Section
5. Securify Hero Section
6. LinkFlow Hero Section
7. Halo / USD Halo Landing Page
8. Prisma Creative Studio
9. Michael Smith Portfolio

## Recommended Verification Commands

Run from the repository root:

```bash
python3 scripts/install_skills.py --dry-run
python3 scripts/install_skills.py --list-collections
python3 -m py_compile scripts/install_skills.py scripts/generate_inventory.py scripts/validate_skills.py
python3 scripts/validate_skills.py
find examples/premium-website-showcase/demos -name "preview.html" | wc -l
ls examples/premium-website-showcase/demo-zips | wc -l
git diff --check
git status
```

Expected high-level results:

- preview count: `9`
- demo ZIP count: `9`
- working tree: clean before release
- no whitespace errors from `git diff --check`

## Known Limitations

- Some showcase previews use external fonts, CDNs, or browser-loaded media for lightweight local preview. They are local preview artifacts, not guaranteed fully offline bundles.
- The benchmark folder currently includes a projected impact estimate, not a measured baseline-vs-skill-assisted benchmark.
- Human review is still required before using any skill-generated output in production.

## Recommended Next Hardening Steps

1. Add one measured baseline-vs-skill-assisted benchmark with screenshots and QA notes.
2. Add screenshots to the showcase gallery or benchmark folder.
3. Run the full `PUBLIC_RELEASE_CHECKLIST.md` before any major public announcement.
4. Add GitHub repository topics for discovery, such as `codex`, `codex-skills`, `frontend`, `web-design`, `accessibility`, `motion`, and `design-engineering`.
