import socket
import sys
import time

s=socket.socket()
host=socket.gethostname()
ip=socket.gethostbyname(host)

PORT =8081

s.bind((host,PORT))
print("binding port")

name=input("please enter your name: ")

s.listen(1)

clientsocket,incomingppl=s.accept()
print("incomming com from ",incomingppl[0])

incommingconnectiondetails = (clientsocket.recv(1024)).decode()

print(incommingconnectiondetails+'has connected')

clientsocket.send(name.encode())
while(True):
    msg=input('Me: ')
    clientsocket.send(msg.encode())
    msg=clientsocket.recv(1024)
    msg=msg.decode()
    print(incommingconnectiondetails,":", msg)




