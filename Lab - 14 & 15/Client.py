from socket import *

# Server IP address and port number
serverName = "127.0.0.1"  # Loopback address (localhost)
serverPort = 12000

# Create a TCP/IP socket
clientSocket = socket(AF_INET, SOCK_STREAM)

# Connect the socket to the server's IP address and port
clientSocket.connect((serverName, serverPort))

# Prompt the user to enter the file name
sentence = input("Enter file name: ")

# Send the file name to the server
clientSocket.send(sentence.encode())

# Receive the file contents from the server
filecontents = clientSocket.recv(1024).decode()

# Print the file contents received from the server
print('From Server:', filecontents)

# Close the socket connection
clientSocket.close()
