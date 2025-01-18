<<<<<<< HEAD
# Distributed File Orchestration and Synchronization

## Overview
This project implements a simple client-server application to manage file operations like **upload**, **download**, **preview**, **delete**, and **directory listing**. It supports secure user authentication and allows multiple clients to interact with the server for file management.

## Table of Contents
- [Introduction](#introduction)
- [Features](#features)
- [Architecture](#architecture)
- [Usage](#usage)
- [File Descriptions](#file-descriptions)
- [Error Handling](#error-handling)
- [Future Enhancements](#future-enhancements)

## Introduction
This file management system allows clients to connect to the server, authenticate themselves, and perform file operations in their individual directories. The server supports multiple client connections simultaneously. Each client interacts with the server to **upload**, **download**, **preview**, **delete**, and **list** files. There is **no timeout mechanism** in this version.

## Features
- **User Authentication:** Users authenticate themselves with a unique username and password stored in a credentials file (`id_passwd.txt`).
- **File Operations:**
  - **Upload:** Upload a file to the server.
  - **Download:** Download a file from the server.
  - **Preview:** View the first 1024 bytes of a file.
  - **Delete:** Remove a file from the server.
  - **List Directory:** View files in the user's directory.
  - **Quit:** Disconnect from the server.
- **Concurrency:** The server can handle multiple clients simultaneously, allowing more than two clients to connect at the same time.

## Architecture
### Client:
- Connects to the server and authenticates the user.
- Allows the user to perform various file operations such as **upload**, **download**, **preview**, **delete**, and **list** files.

### Server:
- Authenticates users and manages their individual directories.
- Handles file operations such as **upload**, **download**, **preview**, and **deletion**.
- Supports concurrent connections, allowing multiple clients to interact with the server simultaneously.

## Usage
### Running the Server
1. Start the server by running the following command:
   ```bash
   python server.py

### Running the Client
1. Start the client by running:
   ```bash
   python client.py

2. Follow the prompts for user authentication and file operations.

### **Authentication**
Add user credentials in the `id_passwd.txt` file in the format:
```plaintext
user1:password1
user2:password2
user3:password3

## **Concurrent Execution**:  
- To test multiple client connections, open multiple terminal windows and start the client program in each terminal:
- The server can handle more than 2 clients simultaneously, so clients can interact with the server without having to wait.

## **File Descriptions**
### **Client File**
- **client.py:** Manages client-side operations, including connecting to the server, authenticating the user, and performing file operations.

### **Server File**
- **server.py:** Manages server-side operations such as handling client connections, user authentication, and managing file operations.

## **Error Handling**
- **Connection Errors:** Connection issues such as timeouts are handled gracefully with error messages.
- **Unauthorized Access:** Ensures users only access their own files by validating file paths and user credentials.
- **Invalid Commands:** The system prompts users for valid input if they enter incorrect commands.

## **Future Enhancements**
- **Web Interface:** Develop a simple web-based graphical user interface (GUI) to make file management easier for users.
- **Access Control:** Introduce user roles and permissions to control access to specific files or directories.
- **Backup and Recovery:** Implement a backup system to periodically back up user files and provide a recovery mechanism in case of system failure.


=======
**Distributed File Orchestration and Synchronization**
_**Overview**_
This project implements a simple client-server application to manage file operations like upload, download, preview, delete, and directory listing. It supports secure user authentication and allows multiple clients to interact with the server for file management.

Table of Contents
Introduction
Features
Architecture
Usage
File Descriptions
Error Handling
Future Enhancements
Introduction
This file management system allows clients to connect to the server, authenticate, and perform file operations in their individual directories. The server is capable of handling multiple client connections simultaneously. Each client interacts with the server to upload, download, preview, delete, and list files. There is no timeout mechanism in this version.

Features
User Authentication: Users authenticate themselves with a unique username and password stored in a credentials file (id_passwd.txt).
File Operations:
Upload: Upload a file to the server.
Download: Download a file from the server.
Preview: View the first 1024 bytes of a file.
Delete: Remove a file from the server.
List Directory: View files in the user's directory.
Quit: Disconnect from the server.
Concurrency: The server can handle multiple clients simultaneously, allowing more than two clients to connect at the same time.
Architecture
Client:
Connects to the server and authenticates the user.
Allows the user to perform various file operations such as upload, download, preview, delete, and list files.
Server:
Authenticates users and manages their individual directories.
Handles file operations such as upload, download, preview, and deletion.
Supports concurrent connections, allowing multiple clients to interact with the server simultaneously.
Usage
Running the Server
Start the server by running the following command:
bash
Copy
Edit
python server.py
The server listens on IP address 192.168.161.114 and port 5000.
Running the Client
Start the client by running:
bash
Copy
Edit
python client.py
Follow the prompts for user authentication and file operations.
Authentication
Add user credentials in the id_passwd.txt file in the format:
plaintext
Copy
Edit
user1:password1
user2:password2
user3:password3
Concurrent Execution
To test multiple client connections, open multiple terminal windows and start the client program in each terminal:
bash
Copy
Edit
python client.py
The server can handle more than 2 clients simultaneously, so clients can interact with the server without having to wait.
File Descriptions
Client File
client.py: Manages client-side operations, including connecting to the server, authenticating the user, and performing file operations.
Server File
server.py: Manages server-side operations such as handling client connections, user authentication, and managing file operations.
Error Handling
Connection Errors: Connection issues such as timeouts are handled gracefully with error messages.
Unauthorized Access: Ensures users only access their own files by validating file paths and user credentials.
Invalid Commands: The system prompts users for valid input if they enter incorrect commands.
>>>>>>> b48617d7fd7c34fa4cedef8d975b40ec545af0fb
