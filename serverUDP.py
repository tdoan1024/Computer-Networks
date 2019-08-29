import socket
IP_Address = "127.0.0.1"
serverPort = 43500

#create server socket using UDP protocol
serverSocket = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
serverSocket.bind((IP_Address, serverPort))
print('The server is ready to receive')

while True:
    #receive message from client
    data, addr = serverSocket.recvfrom(1024)
    #print the message
    print("Message: ", data.decode('utf-8'))

    #if message is "close", close socket and exit
    if data.decode("utf-8") == "close":
        print("Server is shutting down!")
        serverSocket.sendto(b"Server is shutting down!", addr)
        serverSocket.close() #close connection to client
        exit()

    #capitalize message from client, send back
    reply = data.upper()
    serverSocket.sendto(reply, addr)
