#Tai Doan
#CPE4750
#Lab1 - Chat Program
#Partner: Huyen Nguyen

Tested platform: Terminal on Mac
1. Run server: Change directory to the folder contains the file server.py
	Command line: python3   server.py   IP-address   Port
	Program tested  with:
		IP-address: 127.0.0.1
		Port number: 43500
2. Run clients: Change directory to the folder contains the file client.py
	Command line: python3   client.py   IP-address/hostname   Port 
	Program tested  with:
		IP-address: 127.0.0.1 / Host name: localhost
		Port number: 43500
	Repeat the process for another client
3. When server and 2 clients program is ran, program is ready for chatting. Start the conversation with the first client (client 0), each client can send only 1 message each turn
4. Additional features: 
	a. Process server IP, port, etc. using command line arguments
	b. Allow clients the option of specifying a server hostname instead 	of an IP address
	(See 1 and 2)
	c. Side-Bots:
	To call a side-bot, type:
	"!bot tell the joke" to send a joke to other client
	"!bot tell the time" to send the current time to other client
	"!bot tell the date" to send today's date to other client
	d. / commands
	"/close" to disconnect to the server
	"/shutdown" to shutdown the server
	*Welcome message is automatically sent when a new client is connected to server 

