# Install and Preview

## Install the skill library

Clone the repository, inspect the scripts, then dry-run the default public core:

```bash
git clone https://github.com/TheGoat395/Codex-Skills.git
cd Codex-Skills
python3 scripts/install_skills.py --dry-run
```

Install the default `public-core` collection:

```bash
python3 scripts/install_skills.py
```

Install a focused collection:

```bash
python3 scripts/install_skills.py --collection taste-and-build-gates --dry-run
python3 scripts/install_skills.py --collection taste-and-build-gates
```

List available collections:

```bash
python3 scripts/install_skills.py --list-collections
```

After installing, start a new Codex conversation so skill discovery refreshes.

## Install from a release archive

If you prefer not to clone the repository, download the latest packaged archive from:

```text
https://github.com/TheGoat395/Codex-Skills/releases/latest
```

Extract the archive, open a terminal in the extracted folder, then run the same dry-run and install commands:

```bash
python3 scripts/install_skills.py --dry-run
python3 scripts/install_skills.py
```

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

See `DEMOS.md` and `examples/premium-website-showcase/README.md` for the complete proof-of-output gallery.

## Create local ZIPs of every demo

```bash
python3 examples/premium-website-showcase/scripts/package_demos.py
```

ZIP files are written to:

```text
examples/premium-website-showcase/demo-zips/
```
