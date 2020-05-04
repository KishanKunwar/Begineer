
import socket

c = socket.socket()
print("socket is created")

c.connect(("localhost",9999))

print(c.recv(1024).decode())