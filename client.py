import socket
import time

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(("localhost", 9999))

client.send("start".encode())
msg = client.recv(1024).decode()

if msg == "connect":
    print("#Connected")
    
    while True:
        option = str(input("> "))

        if option == "":
            print("$No message")
            client.send("error2".encode())
            break

        client.send(option.encode())
        print("$Sended")
        msg = client.recv(1024).decode()                
        
        print(msg)

        if msg == "test":
            print("#Test")    
            
        elif msg == "close":
            print("#Connection refused")
            break

        elif msg == "removed":
            print("Files from Desktop has been removed")

        elif msg == "played":
            print("#Sound played")
        
        elif msg == "error0":
            print("$Error message")
        
        else:
            pass

        time.sleep(1)
else:
    print("Unknown error")
