#Tai Doan
#CPE4750 - Lab1: Chat program
#Partner: Huyen Nguyen

from socket import *
import re
import sys
from time import gmtime, strftime
from datetime import datetime

serverSocket = socket(AF_INET, SOCK_STREAM) #TCP
serverSocket.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1) #make port reusable

# checks whether sufficient arguments have been provided
if len(sys.argv) != 3:
    print("Correct usage: script, IP address, port number")
    exit()

# takes the first argument from command prompt as IP address
IP_address = str(sys.argv[1])

# takes second argument from command prompt as port number
Port =  int(sys.argv[2])

MAX_CLIENTS = 2 #Max client for this program is 2

# binds the server to an entered IP address and at the
# specified port number.
# The client must be aware of these parameters
serverSocket.bind((IP_address, int(Port)))
serverSocket.listen(1)
print('The server is ready to accept clients')

clients = []
#accept up to 2 connections from clients, which
#must connect before we can move on

# broadcast() takes 2 parameters: a message and the connection to a client
# The function broadcasts the message to all clients whose object is not
# the same as the one sending the message
def broadcast(message, connection):
    for c in clients:
        if c[0] != connection:
            c[0].send(message)

# remove() takes 1 parameters: the connection
# The function removes the object from the list
def remove(connection):
    if connection in clients:
        clients.remove(connection)


while 1:
    for i in range(0, int(MAX_CLIENTS)):
        #accept the connection from client
        connectionSocket,addr = serverSocket.accept()
        #add new clients to the list
        clients.append((connectionSocket,addr))
        #send welcome message to client
        num = int(len(clients)-1)
        connectionSocket.send(b'Welcome to the chatroom!\n')
        #Announce new connection
        welcomeMessage = "Client " + str(len(clients)-1) +" connected "
        print(welcomeMessage)
    #Prompt the first client to start the chat
    clients[0][0].send(b'Enter message: ')
    #the loop makes the chat last infinitely
    while 1:
        for i in range(0,len(clients)):
            #receive message from client
            sentence = clients[i][0].recv(2048).decode('utf-8')
            #check if the message is "/close", if so, then close the connection
            if sentence == "/close":
                print("Client ",i," disconnected!")
                clients[i][0].send(b'Good Bye!')
                msg = b"Other client has disconnected. Chat ended"
                broadcast(msg,clients[i][0])
                clients[i][0].close()
                remove(clients[i][0])

                #check if the message is "/shutdown", if so, shut down the server
            elif sentence == "/shutdown":
                print("Server is shutting down!")
                for c in clients:
                    c[0].send(b'Server is shutting down!')

                    c[0].close()
                exit()

            # server-side bot to tell a joke to other client
            elif sentence == "!bot tell the joke":
                joke = "Are you Vietnamese because I am falling PHO you"
                broadcast(joke.encode('utf-8'),clients[i][0])

            #server-side bot tell current time to other client
            elif sentence == "!bot tell the time":
                curTime = datetime.now()
                time = "It is " + curTime.strftime("%I:%M:%S %p")
                broadcast(time.encode('utf-8'),clients[i][0])

            # server-side bot to tell today's date to other client
            elif sentence == "!bot tell the date":
                curDate = datetime.now()
                date = "Today is " + curDate.strftime("%a, %b %d %Y ")
                broadcast(date.encode('utf-8'),clients[i][0])

            #print out received message, and broadcast to other client
            else:
                print("Client ",i," sent: ",sentence)
                #send received message to other client
                broadcast(sentence.encode('utf-8'),clients[i][0])
