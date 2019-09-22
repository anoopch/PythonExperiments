# CLIENT CODING

# import socket module
import socket

# create a socket object
s = socket.socket()

# define the port on which you want to connect
port = 24248

# connect to the server on local computer (localhost or 127.0.0.1 both represents the current device)
s.connect(('localhost', port))

# receive data from the server
print("The message received from server is: ", s.recv(1024))

# close the connection
s.close()
