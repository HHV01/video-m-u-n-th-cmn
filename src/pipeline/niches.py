"""Resolve niche selection without changing the legacy project tree."""
import os
import re
from pathlib import Path

from . import common


def directory(niche_id):
    if not isinstance(niche_id, str) or not re.fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+)*", niche_id):
        raise ValueError(f"Niche ID không hợp lệ: {niche_id!r}")
    path = common.ROOT / "niches" / niche_id
    if path.resolve() != path or not path.is_dir():
        raise ValueError(f"Niche không tồn tại: {niche_id}")
    return path


def configuration(niche_id):
    path = directory(niche_id)
    for name in ("niche.yaml", "AGENTS.md"):
        if not (path / name).is_file():
            raise ValueError(f"Niche {niche_id} thiếu {name}")
    cfg = common.load_yaml(path / "niche.yaml")
    if not isinstance(cfg, dict) or cfg.get("niche_id") != niche_id:
        raise ValueError(f"niche.yaml phải khai báo niche_id: {niche_id}")
    return cfg


def select(explicit=None, name=None):
    chosen = explicit if explicit is not None else os.getenv("NICHE")
    if chosen is None and name is not None:
        legacy = common.PROJECTS / name / "project.yaml"
        if legacy.is_file():
            chosen = common.load_yaml(legacy).get("niche_id")
        else:
            matches = []
            for path in (common.ROOT / "niches").glob(f"*/projects/{name}/project.yaml"):
                declared = common.load_yaml(path).get("niche_id")
                if declared is not None:
                    directory(declared)
                    if declared != path.parents[2].name:
                        raise ValueError(f"niche_id không khớp thư mục: {path}")
                    matches.append(declared)
            if len(matches) > 1:
                raise ValueError("Tên tập trùng giữa các niche; dùng --niche.")
            if matches:
                chosen = matches[0]
    if chosen is not None:
        configuration(chosen)
    return chosen


def projects(niche_id):
    return directory(niche_id) / "projects" if niche_id else common.PROJECTS


def template(niche_id):
    if niche_id:
        path = directory(niche_id) / "templates"
        if path.is_dir():
            return path
    return common.PROJECTS / "_template"


def settings(niche_id, overrides=None):
    result = common.load_yaml(common.CONFIG / "settings.yaml")
    if niche_id:
        result = common.deep_merge(result, common.load_yaml(common.CONFIG / "channel-direction.yaml"))
        result = common.deep_merge(result, configuration(niche_id))
    result = common.deep_merge(result, overrides)
    if niche_id:
        flow = result.setdefault("flow", {})
        flow.setdefault("playwright", {})["profile_dir"] = (
            directory(niche_id) / ".flow-profile"
        ).as_posix()
    return result


def flow_gen_paths(niche_id, out=None, profile=None):
    """Scope even caller-supplied base paths for the standalone runner."""
    out = Path("out") if out is None else out
    profile = Path.home() / ".flow_gen_profile" if profile is None else profile
    if niche_id:
        configuration(niche_id)
        return out / niche_id, profile / niche_id
    return out, profile
