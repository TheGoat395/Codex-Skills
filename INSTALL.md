# Install and Preview

## Install the skill library

Clone the repository, inspect the scripts, then dry-run the default public core:

```bash
python3 scripts/install_skills.py --dry-run
```

Install the default public core:

```bash
python3 scripts/install_skills.py
```

Install a focused collection:

```bash
python3 scripts/install_skills.py --collection taste-and-build-gates --dry-run
python3 scripts/install_skills.py --collection taste-and-build-gates
```

After installing, start a new Codex conversation so skill discovery refreshes.

## Preview the showcase demos

Open the gallery directly in a browser:

```text
examples/premium-website-showcase/gallery/index.html
```

Or open a demo directly, for example:

```text
examples/premium-website-showcase/demos/michael-smith-portfolio/preview.html
```

No build step is required for the checked-in preview files.

## Create local ZIPs of every demo

```bash
python3 examples/premium-website-showcase/scripts/package_demos.py
```

ZIP files are written to:

```text
examples/premium-website-showcase/demo-zips/
```
