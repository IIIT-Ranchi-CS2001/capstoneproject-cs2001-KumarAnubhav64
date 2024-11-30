Here's an updated **README.md** to reflect the modular file structure with separate folders for `FTP` and `custom_git`, including their `__init__.py` files.

---

# **GitSync**  
*Your all-in-one solution for version control and file sharing in hackathons!*

---

## **Overview**  
GitSync combines the power of a custom Git implementation with an integrated FTP server to provide an efficient and lightweight solution for collaborative projects. Designed with hackathons in mind, GitSync simplifies file versioning, sharing, and syncing, enabling seamless teamwork.

---

## **Features**  

### **Custom Git**  
- **Version Control**: Add, commit, and track changes to your files.  
- **Commit History**: View a detailed log of all changes.  
- **Checkout**: Restore files from any previous commit.  

### **FTP Server**  
- **File Sharing**: Share project files over a local Wi-Fi network.  
- **Cross-Platform**: Access the server using any FTP client.  
- **Real-Time Updates**: Ensure all team members are in sync.

### **Unified Command-Line Interface**  
- User-friendly CLI powered by `Typer`.  
- Manage both Git and FTP functionalities from one tool.

---

## **Installation**  

1. Clone the repository:  
   ```bash
   git clone <repo_url>
   cd gitsync
   ```  

2. Install the required dependencies:  
   ```bash
   pip install -r requirements.txt
   ```  

3. Make `main.py` executable (optional):  
   ```bash
   chmod +x main.py
   ```  

---

## **Usage**  

### **Custom Git Commands**  

1. **Initialize a repository**:  
   ```bash
   ./main.py init <repo_path>
   ```  

2. **Add a file**:  
   ```bash
   ./main.py add <repo_path> <file_name>
   ```  

3. **Commit changes**:  
   ```bash
   ./main.py commit <repo_path> "commit message"
   ```  

4. **View commit log**:  
   ```bash
   ./main.py log <repo_path>
   ```  

5. **Checkout a commit**:  
   ```bash
   ./main.py checkout <repo_path> <commit_index>
   ```  

### **FTP Server Commands**  

1. **Start the FTP server**:  
   ```bash
   ./main.py start-ftp <shared_folder> --host <host_ip> --port <port>
   ```  

2. **Default Example**:  
   ```bash
   ./main.py start-ftp ./shared_folder
   ```  
   (Starts the server on `0.0.0.0:2121` with default credentials.)

---

## **Hackathon Use Case**  
- **Version Control**: Manage project files efficiently with GitSync’s lightweight Git implementation.  
- **File Sharing**: Share project files between devices over a local Wi-Fi or hotspot network.  
- **Real-Time Collaboration**: Sync your team’s changes and progress seamlessly.  
- **Offline Functionality**: Works without an internet connection, perfect for hackathon venues.  

---

## **Project Structure**  
```
gitsync/
├── main.py                # CLI Entry Point
├── custom_git/
│   │   ├── __init__.py    # Git Module Initialization
│   │   ├── custom_git.py  # Git Implementation
│   ├── ftp_server/
│       ├── __init__.py    # FTP Module Initialization
│       ├── ftp_server.py  # FTP Server Implementation
├── README.md              # Documentation
├── requirements.txt       # Dependencies
```

---

## **License**  
This project is licensed under the MIT License.  

---

**GitSync – The perfect companion for your hackathon journey!**  
