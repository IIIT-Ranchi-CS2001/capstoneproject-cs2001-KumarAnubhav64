import unittest
from custom_git.custom_git import CustomGit
from pathlib import Path
import shutil
import json

class TestCustomGit(unittest.TestCase):
    def setUp(self):
        self.test_repo_path = Path("./test_repo")
        self.git_system = CustomGit(self.test_repo_path)

    def tearDown(self):
        if self.test_repo_path.exists():
            shutil.rmtree(self.test_repo_path)

    def test_init(self):
        self.git_system.init()
        self.assertTrue((self.test_repo_path / ".custom_git").exists())
        self.assertTrue((self.test_repo_path / ".custom_git/objects").exists())
        self.assertTrue((self.test_repo_path / ".custom_git/log.json").exists())

    def test_add(self):
        self.git_system.init()
        test_file = self.test_repo_path / "test_file.txt"
        test_file.write_text("Hello, Custom Git!")

        object_hash = self.git_system.add("test_file.txt")
        self.assertTrue(object_hash)
        self.assertTrue((self.test_repo_path / ".custom_git/objects" / object_hash).exists())

    def test_commit(self):
        self.git_system.init()
        test_file = self.test_repo_path / "test_file.txt"
        test_file.write_text("Hello, Commit!")
        file_hash = self.git_system.add("test_file.txt")

        self.git_system.commit("Initial commit", {"test_file.txt": file_hash})
        log = json.loads((self.test_repo_path / ".custom_git/log.json").read_text())
        self.assertEqual(len(log), 1)
        self.assertEqual(log[0]["message"], "Initial commit")

    def test_log_and_checkout(self):
        self.git_system.init()
        test_file = self.test_repo_path / "test_file.txt"
        test_file.write_text("Version 1")
        file_hash_v1 = self.git_system.add("test_file.txt")
        self.git_system.commit("Version 1 commit", {"test_file.txt": file_hash_v1})

        test_file.write_text("Version 2")
        file_hash_v2 = self.git_system.add("test_file.txt")
        self.git_system.commit("Version 2 commit", {"test_file.txt": file_hash_v2})

        self.git_system.checkout(0)
        self.assertEqual(test_file.read_text(), "Version 1")

if __name__ == "__main__":
    unittest.main()
