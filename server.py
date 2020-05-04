
import socket

s = socket.socket()
print(" A server is created")

s.bind(("localhost",9999))

s.listen(5)
print("socket is listening")

while True:

    c,addr = s.accept()
    print("conncetion establish")

    s.send("hello , welcome to the server")

    s.close()