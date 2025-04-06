from socket import *
import sys

serverName = sys.argv[1]
serverPort = int(sys.argv[2])
filename = sys.argv[3]

clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverName, serverPort))

clientSocket.send(f"GET /{filename} HTTP/1.1\r\n\r\n".encode())

response = ""
while True:
    chunk = clientSocket.recv(1024).decode()
    if not chunk:
        break
    response += chunk

print('From Server: ', response)
clientSocket.close()