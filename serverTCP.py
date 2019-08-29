from socket import *

#setup socket to wait for connections
serverPort = 43500
serverSocket = socket(AF_INET, SOCK_STREAM) #TCP (reliable)
serverSocket.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1) #make port reusable
serverSocket.bind(('', serverPort))
serverSocket.listen(1)
print('The server is ready to receive')

#omitting while loop means the server will run once!
while 1:
    #accept connection from client
    connectionSocket, addr = serverSocket.accept()

    #receive message from client, print it, close socket
    sentence = connectionSocket.recv(1024)

    if sentence.decode("utf-8") == "close":
        print("Server is shutting down!")
        connectionSocket.send(b"Server is shutting down!")
        connectionSocket.close() #close connection to client
        exit()

    #capitalize message from client, send back, close connection
    capitalizedSentence = sentence.upper()
    connectionSocket.send(capitalizedSentence)
    connectionSocket.close()
