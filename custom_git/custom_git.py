# import os
# import hashlib
# import json
# from datetime import datetime
# from pathlib import Path




# class CustomGit:
#   def __init__(self, repo_path:Path):
#     self.repo_path = repo_path
#     self.git_dir =  repo_path / ".custom_git"
#     self.objects_dir = self.git_dir / "objects"
#     self.log_file =  self.git_dir / "log.json"

#   def init(self):
#     if self.git_dir.exists():
#       print(f"Repository already initilised in  {self.repo_path}")
#       return
#     os.makedirs(self.objects_dir)
#     self.log_file.write_text(json.dumps([]))
#     print(f"Initilized empty custom git repository in {self.repo_path}")

#   def hash_object(self, content:  str):
#       return hashlib.sha1(content.encode()).hexdigest()

#   def add(self, file_path : str):
#     abs_path  =  self.repo_path / file_path
#     if not abs_path.exists():
#       print(f"File {abs_path} does not exist.")
#       return
#     content  =  abs_path.read_bytes()
#     object_hash =  self.hash_object(content)
#     (self.objects_dir / object_hash).write_text(content)
#     print(f"File {file_path} added with hash {object_hash}")
#     return object_hash

#   def commit(self, message : str , staged_files : str):
#     commit = {
#       "message" : message,
#       "timestamp" : str(datetime.now()),
#       "files" : staged_files,
#     }
#     log =  json.loads(self.log_file.read_text())
#     log.append(commit)
#     self.log_file.write_text(json.dumps(log,indent= 4))
#     print(f"Commit created {message}")

#   def log(self):
#     if not  self.log_file.exists():
#       print("No commits yet.")
#       return
#     log = json.loads(self.log_file.read_text())
#     for entry in log:
#       print(f"Commit: {entry["message"]} at {entry["timestamp"]}")
#       for file,hash_val in entry["files"].items():
#         print(f"     -{file} : {hash_val}")

#   def checkout(self, commit_index : int):
#     log =  json.loads(self.log_file.read_text())
#     if commit_index >=  len(log):
#       print(f"No such commit index : {commit_index}")
#       return
#     commit =  log[commit_index]
#     for file, hash_val in commit["files"].items():
#       content  = (self.objects_dir / hash_val).read_text()
#       (self.repo_path /  file).write_text(content)
#     print(f"Checked out commit:  {commit['message']}")
import os
import hashlib
import json
from datetime import datetime
from pathlib import Path


class CustomGit:
    def __init__(self, repo_path: Path):
        self.repo_path = repo_path
        self.git_dir = repo_path / ".custom_git"
        self.objects_dir = self.git_dir / "objects"
        self.log_file = self.git_dir / "log.json"

    def init(self):
        """Initialize the custom Git repository."""
        if self.git_dir.exists():
            print(f"Repository already initialized in {self.repo_path}")
            return
        os.makedirs(self.objects_dir)
        self.log_file.write_text(json.dumps([]))
        print(f"Initialized empty custom Git repository in {self.repo_path}")

    def hash_object(self, content: str):
        """Generate a SHA-1 hash for the given content."""
        return hashlib.sha1(content.encode()).hexdigest()

    def add(self, file_path: str):
        """Stage a file by saving its content as an object."""
        abs_path = self.repo_path / file_path
        if not abs_path.exists():
            print(f"File {file_path} does not exist.")
            return None
        content = abs_path.read_text()
        object_hash = self.hash_object(content)
        (self.objects_dir / object_hash).write_text(content)
        print(f"File {file_path} added with hash {object_hash}")
        return object_hash

    def commit(self, message: str, staged_files: dict):
        """Create a commit with a message and staged files."""
        commit = {
            "message": message,
            "timestamp": str(datetime.now()),
            "files": staged_files,
        }
        log = json.loads(self.log_file.read_text())
        log.append(commit)
        self.log_file.write_text(json.dumps(log, indent=4))
        print(f"Commit created: {message}")

    def log(self):
        """Display the commit history."""
        if not self.log_file.exists():
            print("No commits yet.")
            return
        log = json.loads(self.log_file.read_text())
        for index, entry in enumerate(log):
            print(f"Commit {index}: {entry['message']} at {entry['timestamp']}")
            for file, hash_val in entry["files"].items():
                print(f"     - {file}: {hash_val}")

    def checkout(self, commit_index: int):
        """Restore files from a specific commit."""
        log = json.loads(self.log_file.read_text())
        if commit_index >= len(log):
            print(f"No such commit index: {commit_index}")
            return
        commit = log[commit_index]
        for file, hash_val in commit["files"].items():
            content = (self.objects_dir / hash_val).read_text()
            (self.repo_path / file).write_text(content)
        print(f"Checked out commit: {commit['message']}")
