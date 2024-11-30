from pyftpdlib.authorizers import DummyAuthorizer
from pyftpdlib.handlers import FTPHandler
from pyftpdlib.servers import FTPServer
from pathlib import Path


class FTPServerApp:
    def __init__(self,user: str,password : str,shared_folder: Path, host: str = "0.0.0.0", port: int = 2121):
        self.shared_folder = shared_folder
        self.host = host
        self.port = port
        self.server = None
        self.user =  user
        self.password =  password


    def setup_server(self):
        # Create shared folder if it doesn't exist
        self.shared_folder.mkdir(parents=True, exist_ok=True)



        # Set up FTP server
        authorizer = DummyAuthorizer()
        # Add a user with full access
        authorizer.add_user("user","password", str(self.shared_folder), perm="elradfmw")

        # Use FTPHandler to handle requests
        handler = FTPHandler
        handler.authorizer = authorizer

        # Instantiate FTP server
        self.server = FTPServer((self.host, self.port), handler)

    def start(self):
        print(f"Starting FTP server on {self.host}:{self.port}")
        self.server.serve_forever()

    def stop(self):
        print("Stopping FTP server...")
        if self.server:
            self.server.close_all()
