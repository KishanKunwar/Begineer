
import socket

c = socket.socket()


#if doesnt know the hostname or addr
#host_ip = socket.gethostbyname("www.google.com")
#print(host_ip)
#c.connect((host_id,80))


c.connect(("localhost",9999))
print("client is connected to the google")

print(c.recv(1024).decode())

