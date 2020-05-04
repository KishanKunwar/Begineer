
import socket

s = socket.socket()
print("socket created")

s.bind(('localhost', 9999))

s.listen(5)
print("waiting for the connection")

while True:
    # connection with the client

    c,addr = s.accept()
    print("connected to the client", addr)

    c.send("Welcome to the server")
    c.close()
