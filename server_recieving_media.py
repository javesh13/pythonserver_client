#!/usr/bin/python

#Python server to recieve media

import socket
from datetime import datetime as dt

HOST = '0.0.0.0'
PORT = 12345

print("Waiting for client on "+str(HOST)+":"+str(PORT))

ADDR = (HOST,PORT)
BUFSIZE = 4096

serv = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

serv.bind(ADDR)
serv.listen(5)

print 'listening ...'

(conn, (ip ,port ))= serv.accept()
print 'client connected ... ' + str(ip)+":"+str(port)

temp_recv=conn.recv(13) # 3 letter extension
#temp_recv=conn.recv(14) # 4 letter extension
if temp_recv.startswith('EXTENSION'):
    extension = temp_recv.split(' ')[1]
  
filename=str(dt.now()).split(".")[-2]+"-"+ip+"." + extension

print("Filename : "+ filename) 
myfile = open(filename, 'w')

while True:
    data = conn.recv(BUFSIZE)
    if not data: break
    myfile.write(data)
    print 'writing file ....'

myfile.close()
print 'finished writing file'
conn.close()
print 'client disconnected'
