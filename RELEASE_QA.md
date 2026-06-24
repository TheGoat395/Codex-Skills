# Release Checks

This document summarizes the public release package for Codex Premium Website Skills and the checks used to verify it.

## Package Summary

- Default public core: `70` skills.
- Showcase demos: `9` local preview demos.
- Showcase ZIP deliverables: `9` demo ZIP files.
- Provider/account integrations: not included in the public core.
- Benchmarking: workflow impact estimate included; measured benchmark examples are tracked as future work.

## Repository Structure

| Check | Expected State | Status |
|---|---|---|
| Root README | Introduces the project and points to the demo gallery | Done |
| Install instructions | Documents dry-run install, install, focused collection install, and local preview | Done |
| Demo index | Lists the confirmed demo set and preview paths | Done |
| Security policy | Describes installer behavior and safe-use expectations | Done |
| Skill quality standard | Defines acceptance and rejection criteria | Done |
| Third-party notices | Describes notice expectations and excluded integrations | Done |
| Benchmark standards | Defines scoring, benchmark format, and estimate format | Done |

## Skill Inventory

| Check | Expected State | Status |
|---|---|---|
| Public core count | `curated_collections.json` defines a 70-skill public core | Done |
| Manifest count | `manifest.json` reports `"skill_count": 70` | Done |
| Inventory count | `SKILL_INVENTORY.md` reports `Total skills: 70` | Done |
| Release checklist | `PUBLIC_RELEASE_CHECKLIST.md` documents release checks | Done |

## Showcase

| Check | Expected State | Status |
|---|---|---|
| Gallery page | `examples/premium-website-showcase/gallery/index.html` | Done |
| Demo manifest | `examples/premium-website-showcase/demo-manifest.json` | Done |
| Showcase README | `examples/premium-website-showcase/README.md` | Done |
| Packaging script | `examples/premium-website-showcase/scripts/package_demos.py` | Done |
| Preview files | 9 `preview.html` files under `examples/premium-website-showcase/demos/` | Done |
| Demo ZIP files | 9 ZIP files under `examples/premium-website-showcase/demo-zips/` | Done |

## Confirmed Showcase Demos

1. Asteria Capital
2. Asteria Space Travel
3. Mainframe Contact Hero
4. VEX Hero Section
5. Securify Hero Section
6. LinkFlow Hero Section
7. Halo / USD Halo Landing Page
8. Prisma Creative Studio
9. Michael Smith Portfolio

## Verification Commands

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

## Notes

- Some showcase previews use external fonts, CDNs, or browser-loaded media for lightweight local preview.
- The benchmark folder currently includes a workflow impact estimate. A measured baseline-vs-skill-assisted benchmark is the next evidence upgrade.
- The showcase artifacts are local preview examples. Production use still requires project-specific review.
