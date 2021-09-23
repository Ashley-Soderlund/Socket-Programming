import socket

# creating the client socket using default par (ipv4, TCP)
client = socket.socket()

# connecting to the server with given IP and port number
client.connect(('localhost', 9999))

name = input("Enter your host name")
client.send(bytes(name, 'utf-8'))  # sending the data to server

print(client.recv(1024).decode())  # receiving the data from server
