#!/usr/bin/env python3
from pathlib import Path
import zipfile

ROOT = Path(__file__).resolve().parents[1]
DEMOS = ROOT / "demos"
OUT = ROOT / "demo-zips"
OUT.mkdir(exist_ok=True)

for demo in sorted(p for p in DEMOS.iterdir() if p.is_dir()):
    zip_path = OUT / f"{demo.name}.zip"
    if zip_path.exists():
        zip_path.unlink()
    with zipfile.ZipFile(zip_path, "w", zipfile.ZIP_DEFLATED) as z:
        for file in sorted(demo.rglob("*")):
            if file.is_file():
                z.write(file, demo.name / file.relative_to(demo))
    print(zip_path.relative_to(ROOT))
