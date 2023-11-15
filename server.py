import socket

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(("localhost", 9999))
print("#Wait connections")
server.listen(1)

client, addr = server.accept()
client.send("start".encode())
msg = client.recv(1024).decode()

if msg == "accept":
    print("$Connected")      
        
    while True:
        msgServer = input("> ")
        if msgServer == "2":
            print("#Connection close")
            break
        if msgServer == "":
            print("#Error message")
        else:
            client.send(msgServer.encode())
            msg = client.recv(1024).decode()
            print(msg)
else:
    print("$UNKNOWN ERROR")
