import socket
import os

# Client Configuration
SERVER_HOST = '192.168.161.114'
SERVER_PORT = 5000
BUFFER_SIZE = 1024

def main():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((SERVER_HOST, SERVER_PORT))

    # Initial welcome message from the server
    print(client_socket.recv(BUFFER_SIZE).decode())

    # Authentication
    username = input("Username : ")
    client_socket.send(username.encode())
    print(client_socket.recv(BUFFER_SIZE).decode())  # Prompt for password

    password = input("Password : ")
    client_socket.send(password.encode())
    
    auth_response = client_socket.recv(BUFFER_SIZE).decode()
    print(auth_response)
    if "Authentication Successful" not in auth_response:
        client_socket.close()
        return

    # Main command loop
    while True:
        command = input("Enter command (UPLOAD, DOWNLOAD, LIST, VIEW, DELETE, QUIT) : ").strip().upper()
        
        if command == "UPLOAD":
            client_socket.send(command.encode())
            filename = input("Enter the file path to upload : ").strip()
            if not os.path.isfile(filename):
                print("File does not exist.")
                continue

            # Send filename to server
            client_socket.send(os.path.basename(filename).encode())
            # Send file size
            file_size = os.path.getsize(filename)
            client_socket.send(str(file_size).encode())

            # Send file content
            with open(filename, "rb") as f:
                while True:
                    bytes_read = f.read(BUFFER_SIZE)
                    if not bytes_read:
                        break
                    client_socket.sendall(bytes_read)
            print(client_socket.recv(BUFFER_SIZE).decode())  # Acknowledge upload completion

        elif command == "DOWNLOAD":
            client_socket.send(command.encode())
            filename = input("Enter the filename to download : ").strip()
            client_socket.send(filename.encode())

            # Check if file exists on the server
            response = client_socket.recv(BUFFER_SIZE).decode()
            if response.startswith("FILE FOUND"):
                file_size = int(response.split(":")[1])
                with open(f"downloaded_{filename}", "wb") as f:
                    received_size = 0
                    while received_size < file_size:
                        bytes_read = client_socket.recv(BUFFER_SIZE)
                        if not bytes_read:
                            break
                        f.write(bytes_read)
                        received_size += len(bytes_read)
                print(f"{filename} downloaded successfully as downloaded_{filename}.")
            else:
                print("File Not Found on the server.")

        elif command == "LIST":
            client_socket.send(command.encode())
            response = client_socket.recv(BUFFER_SIZE).decode()
            if response == "Empty":
                print("No files available in your storage.")
            else:
                print("Files on server:", response)

        elif command == "DELETE":
            client_socket.send(command.encode())
            filename = input("Enter the filename to delete: ").strip()
            client_socket.send(filename.encode())
            print(client_socket.recv(BUFFER_SIZE).decode())

        elif command == "VIEW":
            client_socket.send(command.encode())
            filename = input("Enter the filename to view: ").strip()
            client_socket.send(filename.encode())

            # Receive response from server
            response = client_socket.recv(BUFFER_SIZE).decode()
            if response.startswith("FILE FOUND"):
                file_preview = client_socket.recv(BUFFER_SIZE)
                print("\n--- First 1024 bytes of the file ---")
                print(file_preview.decode(errors="replace"))  # Replace errors for binary-safe display
                print("\n--- End of Preview ---")
            else:
                print("File not found on the server.")


        elif command == "QUIT":
            client_socket.send(command.encode())
            print("Goodbye!")
            break

        else:
            print("Invalid command. Please enter UPLOAD, DOWNLOAD, LIST, DELETE, or QUIT.")

    client_socket.close()

if __name__ == "__main__":
    main()
