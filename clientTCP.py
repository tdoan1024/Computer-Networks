from socket import *

#setup socket to connect to server
serverName = 'localhost'
serverPort = 43500
clientSocket = socket(AF_INET, SOCK_STREAM) #TCP socket
clientSocket.connect((serverName, serverPort))

#gather and send message to server
sentence = input('Input lowercase sentence: ')
clientSocket.send(sentence.encode('utf-8')) 

#receive message from server, print it, close connection
modifiedSentence = clientSocket.recv(1024).decode('utf-8')
print('From Server:', modifiedSentence)
clientSocket.close()
