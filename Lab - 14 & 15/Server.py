from socket import *

# Server IP address and port number
serverName = "127.0.0.1"  # Loopback address (localhost)
serverPort = 12000

# Create a TCP/IP socket
serverSocket = socket(AF_INET, SOCK_STREAM)

# Bind the socket to the server's IP address and port
serverSocket.bind((serverName, serverPort))

# Listen for incoming connection requests
serverSocket.listen(1)

print("The server is ready to receive")

while True:
    # Accept a connection from a client
    connectionSocket, addr = serverSocket.accept()
    
    # Receive the file name from the client
    sentence = connectionSocket.recv(1024).decode()
    
    try:
        # Open and read the file
        file = open(sentence, "r")
        fileContents = file.read(1024)
        file.close()
    except FileNotFoundError:
        # If file is not found, send an error message
        fileContents = "File not found."
    
    # Send the file contents back to the client
    connectionSocket.send(fileContents.encode())
    
    # Close the connection
    connectionSocket.close()
