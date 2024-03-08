#import socket module
from socket import *
import sys # In order to terminate the program

# Create a server socket
serverSocket = socket(AF_INET, SOCK_STREAM)

address = sys.argv[1]

# Prepare a server socket
def tcpServer(address):
    serverPort = 80
    serverSocket.bind((address, serverPort))
    serverSocket.listen(1)
    print(f"Server is now running and listening on port {serverPort}")

    while True:
        # Establish the connection
        print('Ready to serve...')
        connectionSocket, addr = serverSocket.accept()

        try:
            message = connectionSocket.recv(1024)
            filename = message.split()[1]
            f = open(filename[1:])
            outputdata = f.read()

            # Send HTTP header line into socket
            connectionSocket.send("HTTP/1.1 200 OK\r\n\r\n".encode())
            connectionSocket.send("<html><head></head><body><h1>200 You Found Me!</h1></body></html>\r\n".encode())

            # Send the content of the requested file to the client
            for i in range(0, len(outputdata)):
                connectionSocket.send(outputdata[i].encode())
            connectionSocket.send("\r\n".encode())
            connectionSocket.close()
        except IOError:
            # Send response message for file not found
            connectionSocket.send("HTTP/1.1 404 Not Found\r\n\r\n".encode())
            connectionSocket.send("<html><head></head><body><h1>404 Not Found</h1></body></html>\r\n".encode())
            # Close client socket
            connectionSocket.close()

        serverSocket.close()
        sys.exit()  # Terminate the program after sending the corresponding data

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: WebServer.py address")
        sys.exit(1)

    address = sys.argv[1]

    tcpServer(address)