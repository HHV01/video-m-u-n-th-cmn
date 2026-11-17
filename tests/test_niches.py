import os
from pathlib import Path
import sys
import tempfile
import unittest
from unittest.mock import patch

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))
from pipeline import common, niches


class NicheTests(unittest.TestCase):
    def setUp(self):
        tmp = tempfile.TemporaryDirectory()
        self.addCleanup(tmp.cleanup)
        self.root = Path(tmp.name).resolve()
        for name, value in {
            "config/settings.yaml": "flow: {}\nitems: [old]\n",
            "config/channel-direction.yaml": "items: [direction]\nflag: shared\n",
            "config/style.yaml": "{}",
            "projects/existing/project.yaml": "niche: human memory\n",
            "niches/alpha/niche.yaml": "niche_id: alpha\nitems: [alpha]\n",
            "niches/alpha/AGENTS.md": "",
            "niches/alpha/projects/sample/project.yaml": "niche_id: alpha\n",
            "niches/beta/niche.yaml": "niche_id: beta\n",
            "niches/beta/AGENTS.md": "",
        }.items():
            file = self.root / name
            file.parent.mkdir(exist_ok=True, parents=True)
            file.write_text(value, encoding="utf-8")
        for key, value in {"ROOT": self.root, "CONFIG": self.root/"config",
                           "PROJECTS": self.root/"projects"}.items():
            mock = patch.object(common, key, value)
            mock.start()
            self.addCleanup(mock.stop)
        env = patch.dict(os.environ, {}, clear=True)
        env.start()
        self.addCleanup(env.stop)

    def test_legacy(self):
        project = common.Project("existing", resolve_niche=True)
        self.assertEqual(project.dir, self.root/"projects/existing")
        self.assertEqual(project.cfg["niche"], "human memory")
        self.assertEqual(project.settings["items"], ["old"])
        self.assertEqual(niches.template(None), self.root/"projects/_template")

    def test_priority_and_directory(self):
        self.assertEqual(niches.select(name="sample"), "alpha")
        self.assertEqual(common.Project("sample", "alpha").dir, self.root/"niches/alpha/projects/sample")
        os.environ["NICHE"] = "beta"
        self.assertEqual(niches.select(name="sample"), "beta")
        self.assertEqual(niches.select("alpha", "sample"), "alpha")

    def test_merge(self):
        self.assertEqual(niches.settings("alpha")["items"], ["alpha"])
        self.assertEqual(niches.settings("alpha")["flag"], "shared")
        self.assertEqual(niches.settings("alpha", {"items": ["project"]})["items"], ["project"])

    def test_whisper_language_override_is_scoped_to_english_it(self):
        repo = Path(__file__).resolve().parents[1]
        config = self.root / "niches/english-it"
        config.mkdir()
        (config / "niche.yaml").write_bytes((repo / "niches/english-it/niche.yaml").read_bytes())
        (config / "AGENTS.md").touch()
        (self.root / "config/settings.yaml").write_bytes((repo / "config/settings.yaml").read_bytes())
        self.assertEqual(niches.settings("english-it")["voice"]["whisper"]["language"], "en")
        self.assertEqual(niches.settings(None)["voice"]["whisper"]["language"], "vi")
        self.assertEqual(niches.settings("alpha")["voice"]["whisper"]["language"], "vi")

    def test_unknown_niche_id(self):
        (self.root/"projects/existing/project.yaml").write_text("niche_id: missing", encoding="utf-8")
        with self.assertRaisesRegex(ValueError, "Niche không tồn tại"):
            niches.select(name="existing")

    def test_isolation(self):
        alpha, beta = [niches.settings(i)["flow"]["playwright"]["profile_dir"] for i in ("alpha", "beta")]
        self.assertNotEqual(alpha, beta)
        left, right = [niches.flow_gen_paths(i, self.root/"out", self.root/"profiles") for i in ("alpha", "beta")]
        self.assertNotEqual(left[0]/"state.json", right[0]/"state.json")
        self.assertNotEqual(left[1], right[1])
