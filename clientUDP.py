import socket
IP_Address = "127.0.0.1"
serverPort = 43500
#message to send
Message = input("Enter message: ")

#create client socket using UDP protocol
clientSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
#send message to server
clientSocket.sendto(Message.encode('utf-8'), (IP_Address, serverPort))

#reveive the reply from server
fromServer, addr = clientSocket.recvfrom(1024)
sentence = fromServer.decode('utf-8')
#print received message
print('From Server:', sentence)
#close socket
clientSocket.close()
