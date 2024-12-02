from pathlib import Path
from ftp_server.ftp_server import FTPServerApp
from custom_git.custom_git import CustomGit
import typer

app = typer.Typer()

@app.command()
def init(repo_path: str):
    """
    Initialize a Custom Git repository.
    """
    repo_path = Path(repo_path)
    git = CustomGit(repo_path)
    git.init()
@app.command()
def add(repo_path: str, file_path: str):
    """
    Stage a file for committing.
    """
    repo_path = Path(repo_path)
    git = CustomGit(repo_path)
    hash_val = git.add(file_path)
    if hash_val:
        typer.echo(f"File {file_path} staged with hash {hash_val}")

@app.command()
def commit(repo_path: str, message: str):
    """
    Commit staged files with a message.
    """
    repo_path = Path(repo_path)
    git = CustomGit(repo_path)
    log = git.log_file.read_text()
    staged_files = {file.name: git.hash_object(file.read_text()) for file in Path(repo_path).iterdir() if file.is_file()}
    git.commit(message, staged_files)

@app.command()
def log(repo_path: str):
    """
    Show the commit history.
    """
    repo_path = Path(repo_path)
    git = CustomGit(repo_path)
    git.log()

@app.command()
def checkout(repo_path: str, commit_index: int):
    """
    Restore files from a specific commit index.
    """
    repo_path = Path(repo_path)
    git = CustomGit(repo_path)
    git.checkout(commit_index)

@app.command()
def run_ftp(shared_folder: str, host: str = "0.0.0.0", port: int = 2121):
    """Run the FTP server."""
    shared_folder = Path(shared_folder)
    ftp = FTPServerApp(shared_folder, host, port)
    ftp.setup_server()
    ftp.start()

@app.command()
def run_combined(repo_path: str, shared_folder: str, host: str = "127.0.0.1", port: int = 2121):
    """Run both the Git system and the FTP server."""
    # Start the Git system
    repo_path = Path(repo_path)
    git = CustomGit(repo_path)
    git.init()

    # Start the FTP serve r
    shared_folder = Path(shared_folder)
    ftp = FTPServerApp(shared_folder, host, port)
    ftp.setup_server()
    ftp.start()

if __name__ == "__main__":
    app()
