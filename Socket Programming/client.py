import socket

# Create socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Server address
host = "127.0.0.1"
port = 5000

# Connect to server
client_socket.connect((host, port))

print("Connected to server.")

# Send message
message = "Hello Server!"

client_socket.send(message.encode())

# Receive response
response = client_socket.recv(1024).decode()

print("Response from server:", response)

# Close socket
client_socket.close()