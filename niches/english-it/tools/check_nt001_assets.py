"""Check NT-001 assets by owner filenames and action sheet continuity."""
import argparse
import csv
from pathlib import Path

from PIL import Image


def read(path):
    with path.open(encoding="utf-8-sig", newline="") as stream:
        return list(csv.DictReader(stream))


def tokens(value):
    return set(filter(None, value.split(";")))


def check(project):
    mapping = read(project / "asset-map.csv")
    shots = read(project / "action-sheet.csv")
    problems = []
    if len(mapping) != 15 or len({r["path"] for r in mapping}) != 15:
        problems.append("Expected 15 unique owner PNGs.")
    previous = set()
    for shot in shots:
        number = shot["shot"]
        filenames = set().union(*(tokens(shot[key]) for key in ("characters", "scene_props", "icons", "background")))
        expected = {Path(r["path"]).name for r in mapping if number in tokens(r["shots"])}
        if filenames != expected:
            problems.append(f"Shot {number}: asset map delta: {sorted(filenames ^ expected)}")
        active = set().union(*(tokens(shot[key]) for key in ("held_props", "scene_props", "icons")))
        if tokens(shot["remove_props"]) != previous - active:
            problems.append(f"Shot {number}: inconsistent removed props.")
        previous = active
    asset_root = (project / "hinh/assets").resolve()
    for row in mapping:
        name = row["path"]
        path = (asset_root / name).resolve()
        if not path.is_relative_to(asset_root):
            problems.append(f"{name}: outside asset directory")
            continue
        if not path.is_file():
            problems.append(f"{name}: missing")
            continue
        try:
            with Image.open(path) as image:
                w, h = image.size
                if image.format != "PNG":
                    problems.append(f"{name}: expected PNG")
                if name.startswith("backgrounds/") and (w < 1080 or h < 1920):
                    problems.append(f"{name}: {w}x{h}; needs 1080x1920 crop coverage at native size")
                lo, hi = image.convert("RGBA").getchannel("A").getextrema()
                if hi == 0 or (not name.startswith("backgrounds/") and lo == 255):
                    problems.append(f"{name}: missing visible pixels or actual overlay transparency")
                print(f"{name}: {w}x{h}, alpha {lo}–{hi}")
        except OSError as exc:
            problems.append(f"{name}: unreadable ({exc})")
    return problems


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("project", type=Path)
    failures = check(parser.parse_args().project)
    for finding in failures:
        print(finding)
    print(f"{len(failures)} issue(s)")
    raise SystemExit(bool(failures))
