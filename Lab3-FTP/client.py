'''
    CSC/CPE 4750 - Lab 3: FTP
    Tai Doan && Hung Nguyen
'''

from socket import *
import sys
import getpass


clientSocket = socket(AF_INET, SOCK_STREAM) #TCP socket

IP_address = '72.233.138.35' #Server IP Address

Port = 24601 #Server port number

#Connect client to the server
clientSocket.connect((IP_address,Port))
print("Connected to FTP server")

#Print connection response
message = clientSocket.recv(1024).decode('utf-8')
print(message)

#Function user() sends command USER and user name to the server to log in
def user():
    #Send FTP command USER to login and print response from server
    userCmd = 'USER tdoan1\r\n'
    clientSocket.send(userCmd.encode('utf-8'))
    response = clientSocket.recv(1024).decode('utf-8')
    print(response)

#Function password() sends command PASS and password to the server to log in
def password():
    #Send FTP command PASS to send password and print response
    passCmd = 'PASS hello\r\n'
    clientSocket.send(passCmd.encode('utf-8'))
    response = clientSocket.recv(1024).decode('utf-8')
    print(response)

#Function enterPasv() sends command PASV to the server,so the client enters passive mode
def enterPasv():
    clientSocket.send('PASV\r\n'.encode('utf-8'))
    response = clientSocket.recv(1024).decode('utf-8')
    print(response)

    #Isolate the last integer of the reply
    #calculate and return the new port number for data connection
    p2 = response[-7:-4]
    dataPort = (169*256) + int(p2)
    return dataPort

#Function list() lists all the files in current directory
def list():
    #Enter passive mode and open data socket
    dataSocket = socket(AF_INET, SOCK_STREAM)
    dataSocket.connect((IP_address, enterPasv()))
    
    #send LIST command, print out list of files
    clientSocket.send('LIST\r\n'.encode('utf-8'))
    dataresponse = clientSocket.recv(1024).decode('utf-8')
    print(dataresponse)
    
    #response to data socket, print
    print(dataSocket.recv(1024).decode('utf-8'))
    
    #print second response to client socket
    dataresponse1 = clientSocket.recv(1024).decode('utf-8')
    print(dataresponse1)
    #close data socket
    dataSocket.close()

#Function retrive() gets access to the file and sees the file's content
def retrive(fileName):

    #Enter passive mode and open data socket
    dataSocket = socket(AF_INET, SOCK_STREAM)
    dataSocket.connect((IP_address, enterPasv()))
    
    #send RETR command, print response from server
    command = "RETR "+fileName+"\r\n"
    clientSocket.send(command.encode('utf-8'))
    dataresponse = clientSocket.recv(1024).decode('utf-8')
    print(dataresponse)
    
    #Print response from server (i.e the data of the file)
    print('Data: ',dataSocket.recv(1024).decode('utf-8'))
    
    #print second response to client socket
    dataresponse1 = clientSocket.recv(1024).decode('utf-8')
    print(dataresponse1)
    
    #close data socket
    dataSocket.close()

#Function store() create a new file (if does not exist)
#modify content of the file and push it back to the server
def store(fileName):
    
    #Enter passive mode and Open data socket for transfering file
    dataSocket = socket(AF_INET, SOCK_STREAM)
    dataSocket.connect((IP_address, enterPasv()))
    
    #send STOR command, print response from server
    command = "STOR "+fileName+"\r\n"
    clientSocket.send(command.encode('utf-8'))
    dataresponse = clientSocket.recv(1024).decode('utf-8')
    print(dataresponse)
    
    #Input data for the file, send to server through data connection
    newData = input("file data: ") + "\r\n"
    dataSocket.send(newData.encode('utf-8'))
    #Close data socket
    dataSocket.close()
    
    #print second response to client socket
    dataresponse1 = clientSocket.recv(1024).decode('utf-8')
    print(dataresponse1)

#Function cd change current directory
#take 1 parameter as new directory
def cd(directory):
    #Send CWD command and new directory, print response from server
    command = "CWD "+directory+"\r\n"
    clientSocket.send(command.encode('utf-8'))
    dataresponse = clientSocket.recv(1024).decode('utf-8')
    print(dataresponse)

#Login into the server
user()
password()
while 1:
    #Client inputs FTP Command
    code = input("Command Input: ")
    #Split user's input into command code and other parts (file name, directory, etc.)
    code_tokens = code.split()
    #Capitalize the command code
    code_tokens[0] = code_tokens[0].upper()
    command = code_tokens[0] + '\r\n'
    
    #Send appropriate command according to client's input
    if code_tokens[0] =='LIST':
        list()
    elif code_tokens[0] == 'CWD':
        cd(code_tokens[1])
    elif code_tokens[0] == 'RETR' :
        retrive(code_tokens[1])
    elif code_tokens[0] == 'STOR':
        store(code_tokens[1])

    #If command is 'QUIT', print response and quit the program
    elif code_tokens[0] == 'QUIT':
        clientSocket.send(command.encode('utf-8'))
        print(clientSocket.recv(1024).decode('utf-8'))
        break

    #send command and print reponse from server
    #If Timeout, quit the program
    else:
        clientSocket.send(command.encode('utf-8'))
        response = clientSocket.recv(1024).decode('utf-8')
        if '421' in response:
            print(response)
            break
        print(response)

#Close the client socket after
clientSocket.close()
