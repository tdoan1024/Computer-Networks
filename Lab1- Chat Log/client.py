#Tai Doan
#CPE4750 - Lab1: Chat Program
#Partner: Huyen Nguyen

from socket import *
import sys


clientSocket = socket(AF_INET, SOCK_STREAM) #TCP socket

# checks whether sufficient arguments have been provided
if len(sys.argv) != 3:
    print("Correct usage: script, IP address/host name, port number")
    exit()

# takes the first argument from command prompt as IP address
IP_address = str(sys.argv[1])

# takes second argument from command prompt as port number
Port = int(sys.argv[2])

# connect to the server
connection = clientSocket.connect((IP_address,Port))

#After connected, client is welcomed by the server
welcomeMessage = clientSocket.recv(2048).decode('utf-8')
print(welcomeMessage)

#Get the message to start the chat
start = clientSocket.recv(2048).decode('utf-8')
print(start)

while 1:
    try:
        #send message to the server
        sentence = input('> ')
        clientSocket.send(sentence.encode('utf-8'))

        #if input is "close", close connection
        if sentence == "/close":
            closeMsg = clientSocket.recv(2048).decode('utf-8')
            print(closeMsg)
            clientSocket.close()
            exit()
        else:
            #receive message from server, print it
            fromServer = clientSocket.recv(2048).decode('utf-8')
            print(fromServer)

    #If cannot connect to server, close the connection
    except IOError:
        print("Server is shutting down!")
        clientSocket.close()
        exit()
clientSocket.close() #close connection
