import json
import os
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile
import unittest
import uuid
from unittest.mock import patch

from workbench import core

ROOT = Path(__file__).resolve().parents[1]


class JourneyTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.temp = tempfile.TemporaryDirectory()
        cls.root = Path(cls.temp.name)
        cls.project = cls.root / "authoring"
        example = ROOT / "examples/buy-side-dd"
        core.describe(cls.project, example / "brief.md")
        core.model(cls.project, example / "manifest.json")
        core.resolve(cls.project)
        core.build(cls.project)
        suite = core.read(example / "suite.json")
        suite["cases"] = [suite["cases"][0], suite["cases"][3]]
        core.write(cls.root / "suite.json", suite)
        cls.report = core.rehearse(cls.project, cls.root / "suite.json")

    @classmethod
    def tearDownClass(cls):
        cls.temp.cleanup()

    def project_copy(self):
        temp = tempfile.TemporaryDirectory()
        self.addCleanup(temp.cleanup)
        dest = Path(temp.name) / "project"
        shutil.copytree(self.project, dest)
        # Candidate pointers remain shared but tests never mutate the shared candidate.
        return dest

    def test_rehearsal_observes_success_and_refusal(self):
        self.assertTrue(self.report["passed"])
        self.assertEqual([r["business_success"] for r in self.report["cases"]], [True, False])
        self.assertTrue(all(t["accepted"] for r in self.report["cases"] for t in r["trace"]))

    def test_rejection_and_synthetic_promotion_are_blocked(self):
        p = self.project_copy()
        core.review(p, "reject", "SYNTHETIC reviewer", "SYNTHETIC rejection", True)
        with self.assertRaises(core.WorkbenchError): core.release(p, p / "out")
        core.review(p, "approve", "SYNTHETIC reviewer", "SYNTHETIC acceptance", True)
        with self.assertRaises(core.WorkbenchError): core.release(p, p / "out", "reviewed")

    def test_immutable_release_clean_install_and_conflict(self):
        p = self.project_copy()
        core.review(p, "approve", "SYNTHETIC reviewer", "SYNTHETIC review", True)
        release = core.release(p, p / "releases")["release"]
        with self.assertRaises(core.WorkbenchError): core.release(p, p / "releases")
        installed = Path(core.install(release, p / "clean-host")["installed"])
        # Execute the installed runtime from outside both source and authoring project.
        r = subprocess.run([sys.executable, str(installed / "scripts/runtime.pyz"), "validate", str(installed / "manifest.json")],
                           cwd=p.parent, capture_output=True, encoding="utf-8")
        self.assertTrue(json.loads(r.stdout)["ok"], r.stdout)
        core.install(release, p / "clean-host")  # exact reinstall is idempotent
        (installed / "SKILL.md").write_text("changed", encoding="utf-8")
        with self.assertRaises(core.WorkbenchError): core.install(release, p / "clean-host")

    def test_published_folders_inherit_destination_permissions(self):
        # Regression: mkdtemp staging kept an owner-only ACL/0700 mode after rename,
        # so a different host identity could not scan an installed skill.
        def access(path):
            if os.name == "nt":
                out = subprocess.run(["icacls", str(path)], capture_output=True, text=True).stdout
                return sorted(line.replace(str(path), "").strip() for line in out.splitlines()
                              if ":" in line and "Successfully" not in line)
            return oct(path.stat().st_mode & 0o777)
        p = self.project_copy()
        core.review(p, "approve", "SYNTHETIC reviewer", "SYNTHETIC review", True)
        # Publish under a normally inheriting folder, not a mkdtemp test folder.
        base = ROOT / ".workbench" / ("acl-test-" + uuid.uuid4().hex[:8])
        base.mkdir(parents=True)
        self.addCleanup(shutil.rmtree, base, True)
        release = Path(core.release(p, base / "releases")["release"])
        installed = Path(core.install(release, base / "host")["installed"])
        for published in (release, installed, installed / "scripts"):
            sibling = published.parent / ("plain-" + published.name)
            sibling.mkdir()
            self.assertEqual(access(published), access(sibling), published)
            sibling.rmdir()
        self.assertEqual([c.name for c in installed.parent.iterdir()], [installed.name])  # no stage residue

    def test_changed_brief_invalidates_review(self):
        p = self.project_copy()
        core.review(p, "approve", "SYNTHETIC reviewer", "SYNTHETIC review", True)
        (p / "brief.md").write_text("A different scope", encoding="utf-8")
        with self.assertRaises(core.WorkbenchError): core.release(p, p / "out")

    def test_release_tamper_detected(self):
        p = self.project_copy()
        core.review(p, "approve", "SYNTHETIC reviewer", "SYNTHETIC review", True)
        release = Path(core.release(p, p / "releases")["release"])
        (release / "skill.zip").write_bytes(b"tampered")
        with self.assertRaises(core.WorkbenchError): core.install(release, p / "host")

    def test_publication_retries_transient_lock_but_preserves_conflicts(self):
        with tempfile.TemporaryDirectory() as tmp:
            stage, target = Path(tmp) / "stage", Path(tmp) / "target"
            stage.mkdir()
            real_rename = Path.rename
            calls = []
            def flaky(source, destination):
                calls.append(1)
                if len(calls) == 1:
                    raise PermissionError("simulated scanner lock")
                return real_rename(source, destination)
            with patch.object(Path, "rename", flaky):
                core.publish_directory(stage, target)
            self.assertTrue(target.is_dir())
            stage.mkdir()
            with self.assertRaises(core.WorkbenchError): core.publish_directory(stage, target)
            self.assertTrue(stage.is_dir())

    def test_reuse_and_changed_source(self):
        p = self.project_copy()
        candidate, info = core.current(p)
        original = candidate / "package" / info["workflow"] / "methods/dd-ingest-classify-extract"
        source = p / "reusable-method"
        shutil.copytree(original, source)
        result = core.resolve(p, {"dd-ingest-classify-extract": source})
        self.assertEqual(result["skills"][0]["decision"], "reuse")
        built = core.build(p)
        self.assertTrue(Path(built["candidate"]).exists())
        (source / "SKILL.md").write_text("changed", encoding="utf-8")
        with self.assertRaises(core.WorkbenchError): core.current(p)

    def test_wrong_expected_outcome_does_not_pass(self):
        p = self.project_copy()
        suite = core.read(self.root / "suite.json")
        suite["cases"] = [suite["cases"][1]]  # short manual refusal route
        suite["cases"][0]["expected"]["business_success"] = True
        path = p / "bad-expectation.json"
        core.write(path, suite)
        self.assertFalse(core.rehearse(p, path)["passed"])
        core.review(p, "approve", "SYNTHETIC reviewer", "SYNTHETIC", True)
        with self.assertRaises(core.WorkbenchError): core.release(p, p / "out")


if __name__ == "__main__":
    unittest.main()
