import socket
import sys
import time

s=socket.socket()
host=socket.gethostname()
ip=socket.gethostbyname(host)

PORT =8080

s.bind((host,PORT))
print("binding port")

name=input("please enter your name")

s.listen(1)

conn,incomingppl=s.accept()
print("incomming com from ",incomingppl[0])