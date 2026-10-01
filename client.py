import socket
import threading

SERVER_IP = "192.168.1.53"
PORT = 5001


def receive_messages(client_socket):
    while True:
        try:
            message = client_socket.recv(1024).decode()

            if not message:
                print("\nServer disconnected.")
                break

            print(f"\nServer: {message}")
            print("Client: ", end="", flush=True)

        except:
            print("\nConnection closed.")
            break


# Create socket
client_socket = socket.socket(
    socket.AF_INET,
    socket.SOCK_STREAM
)

print("Connecting to server...")

# Connect to server
client_socket.connect((SERVER_IP, PORT))

print("Connected to server!")
print("You can now chat with the server.")
print("Type 'exit' to close.\n")


# Thread for receiving messages
receive_thread = threading.Thread(
    target=receive_messages,
    args=(client_socket,)
)

receive_thread.daemon = True
receive_thread.start()


# Main thread sends messages
while True:

    message = input("Client: ")

    client_socket.send(message.encode())

    if message.lower() == "exit":
        break


client_socket.close()