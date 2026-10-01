import socket

# Create socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# IP address and port
host = "127.0.0.1"
port = 5000

# Bind socket to address and port
server_socket.bind((host, port))

# Start listening
server_socket.listen(1)

print("Server is waiting for connection...")

# Accept client connection
client_socket, client_address = server_socket.accept()

print("Client connected:", client_address)

# Receive message from client
message = client_socket.recv(1024).decode()

print("Message from client:", message)

# Send response to client
response = "Hello Client! Message received."

client_socket.send(response.encode())

# Close sockets
client_socket.close()
server_socket.close()

print("Server closed.")