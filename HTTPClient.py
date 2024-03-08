import sys
from socket import *

def http_get_request(server_host, server_port, filename):
    # Create a client socket
    clientSocket = socket(AF_INET, SOCK_STREAM)
    
    try:
        # Connect to the server
        clientSocket.connect((server_host, server_port))

        # Construct the HTTP GET request
        request = f"GET /{filename} HTTP/1.1\r\nHost: {server_host}\r\nConnection: close\r\n\r\n"

        # Send the request to the server
        clientSocket.send(request.encode())

        # Receive and display the server's response
        response = ""
        while True:
            data = clientSocket.recv(1024)
            if not data:
                break
            response += data.decode()

        print(response)
    except Exception as e:
        print("Error:", e)
    finally:
        # Close the socket
        clientSocket.close()

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: HTTPClient.py server_host server_port filename")
        sys.exit(1)

    server_host = sys.argv[1]
    server_port = int(sys.argv[2])
    filename = sys.argv[3]

    http_get_request(server_host, server_port, filename)