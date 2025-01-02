from socket import *

serverPort = 12000
serverSocket = socket(AF_INET, SOCK_DGRAM)
serverSocket.bind(("127.0.0.1", serverPort))
print("The server is ready to receive")

while True:
    sentence, clientAddress = serverSocket.recvfrom(2048)
    try:
        file = open(sentence.decode(), "r")
        fileContents = file.read(2048)
        file.close()
        serverSocket.sendto(bytes(fileContents, "utf-8"), clientAddress)
    except FileNotFoundError:
        serverSocket.sendto(b"File not found.", clientAddress)
    print("Sent back to client:", fileContents)
