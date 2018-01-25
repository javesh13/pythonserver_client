#!/usr/bin/python

import socket

#Python client for sending media

HOST = 'localhost'
PORT = 12345

print("Connecting to "+str(HOST)+":"+ str(PORT))

ADDR = (HOST,PORT)
BUFSIZE = 4096
file_to_send = raw_input("Enter the file (with extension) : ")
format_of_file = file_to_send.split(".")[1]


bytes = open(file_to_send).read()

print len(bytes)

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)
client.send("EXTENSION "+format_of_file)

client.send(bytes)

client.close()
