"""Validate NT-001 shot declarations and local PNG assets without rendering."""
import argparse
import csv
import re
from pathlib import Path

from PIL import Image

CHARACTERS = {"Minh": "C1", "Linh": "C2", "Mai": "C7"}
FIELDS = set("shot speaker characters held_props scene_props remove_props icons screen_text motion background".split())


def read_csv(path):
    with path.open(encoding="utf-8-sig", newline="") as stream:
        return list(csv.DictReader(stream))


def entries(value):
    return set(filter(None, map(str.strip, value.split(";"))))


def check(project):
    rows = read_csv(project / "action-sheet.csv")
    voice = {row["shot"]: row["speaker"] for row in read_csv(project / "kich-ban/voice.csv")}
    if not rows or any(set(row) != FIELDS or None in row.values() for row in rows):
        return ["Action sheet CSV has invalid columns or incomplete rows."]
    errors = []
    assets = {}
    previous = set()
    shots = [row["shot"] for row in rows]
    if shots != [f"{i:02}" for i in range(1, 12)]:
        errors.append("Expected exactly shots 01–11 in order.")
    for row in rows:
        shot = row["shot"]
        visible = set()
        required = []
        for item in sorted(entries(row["characters"])):
            if not re.fullmatch(r"C[127]:P0[1-8]:[a-z]+", item):
                errors.append(f"{shot}: invalid character/pose/expression {item}")
                continue
            character, _, expression = item.split(":")
            visible.add(character)
            if expression == "unspecified":
                errors.append(f"{shot}: expression unspecified for {character}")
                continue
            required.append(f"characters/{item.replace(':', '-')}.png")
        speaker = row["speaker"]
        if speaker != voice.get(shot, "") or (speaker and CHARACTERS.get(speaker) not in visible):
            errors.append(f"{shot}: declared speaker conflicts with voice CSV or visible cast")
        held = set()
        for item in sorted(entries(row["held_props"])):
            match = re.fullmatch(r"(C[127]):([a-z0-9-]+)", item)
            if not match or match[1] not in visible:
                errors.append(f"{shot}: invalid or absent holder for {item}")
                continue
            held.add(match[2])
        props = held | entries(row["scene_props"])
        icons = entries(row["icons"])
        current = props | icons
        removed = entries(row["remove_props"])
        if removed != previous - current:
            errors.append(f"{shot}: removals expected {sorted(previous-current)}, got {sorted(removed)}")
        previous = current
        for items, folder, pattern in (
            (props, "props", r"[a-z0-9-]+"),
            (icons, "icons", r"I-\d{2}"),
            ({row["background"]}, "backgrounds", r"BG-0[1-8]-[AB]"),
        ):
            for item in sorted(items):
                if re.fullmatch(pattern, item):
                    required.append(f"{folder}/{item}.png")
                else:
                    errors.append(f"{shot}: invalid {folder} ID {item!r}")
        if not row["motion"].strip():
            errors.append(f"{shot}: missing motion note")
        for name in required:
            assets.setdefault(name, []).append(shot)
    for name, used in sorted(assets.items()):
        path = project / "hinh/assets" / name
        prefix = f"shots {', '.join(used)}: {name}"
        if not path.is_file():
            errors.append(f"{prefix}: missing")
            continue
        try:
            with Image.open(path) as image:
                if image.format != "PNG":
                    errors.append(f"{prefix}: expected PNG")
                    continue
                lo, hi = image.convert("RGBA").getchannel("A").getextrema()
                if hi == 0 or (not name.startswith("backgrounds/") and lo == 255):
                    errors.append(f"{prefix}: expected visible pixels and real transparency on overlays")
        except OSError as exc:
            errors.append(f"{prefix}: unreadable PNG ({exc})")
    return errors


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("project", type=Path)
    args = parser.parse_args()
    try:
        findings = check(args.project)
    except (OSError, csv.Error, KeyError, TypeError) as exc:
        parser.exit(1, f"Invalid or missing input: {exc}\n")
    if findings:
        print("\n".join(findings))
    print(f"{len(findings)} issue(s). Checks cover declarations and files; review pixels and timing manually.")
    return bool(findings)


if __name__ == "__main__":
    raise SystemExit(main())
