# Programmer: Ashley Soderlund
# Program Description: Creating a server socket which can be connected to by three different clients at a given time.
# Date: 9/23/21
# Last Changed: 9/27/21

import socket

#  creating the server socket using default par (ipv4, TCP)
server = socket.socket()
print("Server socket created")

# blind ipaddress and port number
server.bind(('localhost', 9999))

# server connects to 3 clients at a given time
server.listen(3)
print("Server waiting for connections")

while True:
    client, ipaddress = server.accept()  # retrieving client and its ip
    name = client.recv(1024).decode()  # receiving and assigning data from client
    print("Server is now connected with ", ipaddress, name)
    client.send(bytes("You're now connected with the server", 'utf-8'))  # sending data to client
    client.close()  # close connection
