
import socket

s= socket.socket()

s.bind(("localhost",9999))

s.listen(5)
print("socket is listening ")

while True:

    c,adrr = s.accept()
    print("sever and client is connected ")
    print(adrr)

    c.send(bytes("thank you for requesting to the server ","utf-8"))

    c.close()