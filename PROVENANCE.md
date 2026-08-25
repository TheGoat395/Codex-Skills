# Skill Provenance

This ledger distinguishes original repository work, adapted public guidance, and externally sourced material. It supplements `THIRD_PARTY_NOTICES.md`; it does not replace licenses inside individual skill folders.

| Skill or surface | Classification | Source / basis | Notes |
|---|---|---|---|
| Original 70-skill public core, except entries below | Repository-original packaging and workflows | Initial public-core release in commit `2caaecc1d1c2f76a8652ed427667e4d0d366571d` | Review individual Git history before asserting sole authorship of pre-release drafts. |
| `design-motion-principles` | Original synthesis informed by public work | Public work of Emil Kowalski, Jakub Krehel, and Jhey Tompkins, as disclosed in the skill | Not authored, reviewed, or endorsed by the referenced designers. Exact reference URLs should remain documented in the skill's reference files. |
| `gsap-performance` | Original/adapted general guidance | Browser rendering principles and GSAP API concepts | Verify API-specific recommendations against current official GSAP documentation when used. |
| Historical `impeccable` folder | External-style imported bundle; removed | Present in repository history and replaced by `frontend-quality-auditor` in commit `e4c0169c35352bcab0c218a26717f8e356ed2d6a` | Do not restore or redistribute without establishing its upstream source and license. |
| `website-operations` collection | Repository-original synthesis with one externally inspired audit input | User website canon plus review of `darthv95/full-stack-audit` | No text copied wholesale. Security/paywall concepts were retained; automatic-fix and time-sensitive legal assertions were excluded. |
| `full-stack-audit` input | External repository/workflow | `darthv95/full-stack-audit`, initial commits attributed in its Git history to Jalaaldeen / Rolling dollars | Treat as an input for review, not as part of this repository's license or authorship claim. |

## Maintenance rule

For every future imported or materially adapted skill, record the skill name, classification, upstream URL, upstream commit/tag, license, import commit, material changes, and last review date before release.
