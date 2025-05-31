from socket import *
import socket
import threading

def handle_client(client_socket):
    try:
        message = connectionSocket.recv(1024).decode()
        #if not message:
        #    connectionSocket.close()
        #    continue
        filename = message.split()[1]
        print('Filename requested is ', filename)
        f = open(filename[1:])
        outputdata = f.read()
        # Send one HTTP header line into socket
        sendMessage = 'HTTP/1.1 200 OK \r\n\r\n'
        connectionSocket.send(sendMessage.encode())
        #connectionSocket.sendAll(outputdata.encode())
        # Send the content of the requested file to the client
        for i in range(0, len(outputdata)):
            connectionSocket.send(outputdata[i].encode())
        connectionSocket.send("\r\n".encode())
        print('Success File sent !')
        connectionSocket.close()

    except IOError:
        # Send response message for file not found
        sendMessage = 'HTTP/1.1 404 Not Found\r\n\r\n'
        connectionSocket.send(sendMessage.encode())
        print('Requested File not available.')

        # Close client socket
        connectionSocket.close()

if __name__ == '__main__':
    serverSocket = socket.socket(AF_INET, SOCK_STREAM)
    #Prepare a sever socket
    serverPort = 65000
    #serverName = ("192.168.0.165")
    serverSocket.bind(('192.168.0.106', serverPort))
    serverSocket.listen()
    while True:
        # Establish the connection
        print('The Server ' + socket.gethostname() + ' is running ...')
        connectionSocket, addr = serverSocket.accept()
        trd = threading.Thread(target=handle_client, args=(connectionSocket, ))
        print('Request from client {} on port {} ...'.format(addr, trd.name))
        trd.start()
    #serverSocket.close()
    #sys.exit()