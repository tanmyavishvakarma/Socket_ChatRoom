import socket 
import sys 
import time

serversocket=socket.socket()
serverhost=socket.gethostname()
serverip=socket.gethostbyname(serverhost)

SPORT=8081

print("your ip is :" ,serverip)

host=input("server address : ") 
name=input("enter your name : ")
print("trying to connect to ",host )
serversocket.connect((host,SPORT))

print("connected")

serversocket.send(name.encode())
s_name=serversocket.recv(1024)
s_name=s_name.decode()
print(s_name, " has joined")

while(True):
    msg=serversocket.recv(1024)
    msg=msg.decode()
    print(s_name,":",msg)
    msg=input("Me : ")
    if(msg=="[e]"):
        msg="left chat"
        serversocket.send(msg.encode())
        break
    serversocket.send(msg.encode())

