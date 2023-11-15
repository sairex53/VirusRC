import socket
import os
import time

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
HOST = "localhost"
client.connect((HOST, 9999))
msg = client.recv(1024).decode()

if msg == "start":
    client.send("accept".encode('utf-8'))
    print("#Connected")

    while True:
        msg = client.recv(1024).decode('utf-8')

        if msg == "1":
            if open("/Users/sairex/Desktop/file.txt", mode="w+"):
                client.send(" ~/File exists".encode())
            else:
                client.send("$No file".encode())
        if msg == "2":
            print("#Connection close")
            connect = True 
            while True:
                client.connect(("localhost", 9999))
        else:
            if msg == "1":
                pass
            else:
                client.send("$No message".encode()) 
        
