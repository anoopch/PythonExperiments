# first import the socket library
import socket

# next create a socket object
s = socket.socket()
print("Server Socket successfully created")
# reserve a port on your computer, it can be anything
port = 24248
# NEXT BIND TO THE PORT
# we have not typed any ip in the field, instead we have inputted an empty string
# this makes the server listen to requests coming from other computers on the network
s.bind(('', port))
print("socket bound to ", port)
# put the socket into listening mode
s.listen()
# a forever loop until we interrupt it or an error occurs
while True:  # SERVER SHOULD ALWAYS RUN
    # establish connection with client
    print("socket is listening")
    c, addr = s.accept()
    print("Got connection from", addr)
    # send a thank you message to the client
    out = "Thank you for connecting"
    c.sendall(out.encode('utf-8'))
    # close the connection with the client
    c.close()
