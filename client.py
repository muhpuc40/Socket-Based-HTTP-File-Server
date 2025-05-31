import socket
import sys

def main():
    if len(sys.argv) != 4:
        print("Usage: client.py server_host server_port filename")
        return

    server_host = sys.argv[1]
    server_port = int(sys.argv[2])
    filename = sys.argv[3]

    request = f"GET /{filename} HTTP/1.1\r\nHost: {server_host}\r\n\r\n"

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((server_host, server_port))
    client_socket.send(request.encode('utf-8'))

    response = client_socket.recv(1024)
    print(response.decode('utf-8'))

    client_socket.close()

if __name__ == '__main__':
    main()