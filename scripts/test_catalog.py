#!/usr/bin/env python3
"""Focused regressions for catalog metadata and recoverable installation."""
import contextlib
import importlib.util
import io
from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch


def module(name):
    spec = importlib.util.spec_from_file_location(name, Path(__file__).with_name(name + ".py"))
    value = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(value)
    return value


installer = module("install_skills")
validator = module("validate_skills")
inventory = module("generate_inventory")


class CatalogTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        self.source = self.root / "source" / "parse-csv"
        self.source.mkdir(parents=True)
        self.source.joinpath("SKILL.md").write_text("---\nname: parse-csv\ndescription: Parse CSV records.\n---\n\nParse the requested CSV.\n")
        self.dest = self.root / "installed"
        self.dest.mkdir()
        self.target = self.dest / self.source.name
        self.target.mkdir()
        self.target.joinpath("old.txt").write_text("original")
        self.backups = self.root / "backups"

    def validate(self):
        with patch.object(validator, "SKILLS_DIR", self.source.parent), patch.object(validator, "COLLECTIONS", self.root / "absent.json"), contextlib.redirect_stdout(io.StringIO()), contextlib.redirect_stderr(io.StringIO()):
            return validator.main()

    def test_short_meaningful_description_is_valid(self):
        self.assertEqual(self.validate(), 0)

    def test_blank_description_is_rejected(self):
        p = self.source / "SKILL.md"
        p.write_text(p.read_text().replace("Parse CSV records.", "   "))
        self.assertEqual(self.validate(), 1)

    def test_mismatched_skill_name_is_rejected(self):
        p = self.source / "SKILL.md"
        p.write_text(p.read_text().replace("name: parse-csv", "name: other-name"))
        self.assertEqual(self.validate(), 1)

    def test_inventory_ignores_compilation_cache(self):
        before = inventory.skill_info(self.source)
        cache = self.source / "__pycache__"
        cache.mkdir()
        (cache / "test.pyc").write_bytes(b"cache")
        self.assertEqual(before, inventory.skill_info(self.source))

    def test_dry_run_preserves_existing_installation(self):
        self.assertEqual(installer.copy_skill(self.source, self.dest, True, True, self.backups), "would_replace")
        self.assertEqual((self.target / "old.txt").read_text(), "original")
        self.assertFalse(self.backups.exists())

    def test_replacement_preserves_backup(self):
        self.assertEqual(installer.copy_skill(self.source, self.dest, False, True, self.backups), "replaced")
        self.assertTrue((self.target / "SKILL.md").exists())
        self.assertEqual((self.backups / self.source.name / "old.txt").read_text(), "original")

    def test_copy_failure_leaves_existing_installation(self):
        with patch.object(installer.shutil, "copytree", side_effect=OSError("fixture copy failure")):
            with self.assertRaises(OSError):
                installer.copy_skill(self.source, self.dest, False, True, self.backups)
        self.assertEqual((self.target / "old.txt").read_text(), "original")
        self.assertFalse(self.backups.exists())

    def test_backup_collision_preserves_both_versions(self):
        backup = self.backups / self.source.name
        backup.mkdir(parents=True)
        (backup / "older.txt").write_text("older")
        with self.assertRaises(FileExistsError):
            installer.copy_skill(self.source, self.dest, False, True, self.backups)
        self.assertEqual((backup / "older.txt").read_text(), "older")
        self.assertEqual((self.target / "old.txt").read_text(), "original")

    def test_activation_failure_restores_existing_installation(self):
        original_rename = Path.rename
        def fail_activation(path, target):
            if path.parent.name.startswith(".skill-stage-"):
                raise OSError("fixture activation failure")
            return original_rename(path, target)
        with patch.object(Path, "rename", fail_activation):
            with self.assertRaises(OSError):
                installer.copy_skill(self.source, self.dest, False, True, self.backups)
        self.assertEqual((self.target / "old.txt").read_text(), "original")

    def test_symlink_target_is_not_replaced(self):
        other = self.dest / "other"
        self.target.rename(other)
        self.target.symlink_to(other, target_is_directory=True)
        with self.assertRaises(ValueError):
            installer.copy_skill(self.source, self.dest, False, True, self.backups)
        self.assertEqual((other / "old.txt").read_text(), "original")


if __name__ == "__main__":
    unittest.main()
