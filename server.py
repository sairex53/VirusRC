import socket
import pygame
import time
import shutil
import os

while True:
    serv = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    serv.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    serv.bind(("localhost", 9999))
    print("#Wait message...")
    serv.listen(1)
    time.sleep(3)
    client, addr = serv.accept()
    msg = client.recv(1024).decode()

    if msg == "start":
        client.send("connect".encode())
        print("$Connected")
        
        while True:
            error = True

            msg = client.recv(1024).decode()
            
            if msg == "0":
                client.send("test".encode())

            elif msg == "1":
                pygame.mixer.init()
                pygame.mixer.music.load("sound.mp3")
                pygame.mixer.music.play()
                client.send("played".encode())

            elif msg == "2":
                print("$Client disconnect")
                client.send("close".encode())
                time.sleep(1)
                client.close()
                serv.close()
                break
            
            elif msg == "3":
                directory = "/Users/sairex/Desktop" 
                files = os.listdir(directory) 
                listToString = str(files)
                sendList = "Removed: ",listToString 

                dir = '/Users/sairex/Desktop/'
                for files in os.listdir(dir):
                    path = os.path.join(dir, files)
                    try:
                        shutil.rmtree(path)
                    except OSError:
                        os.remove(path) 

                client.send(str(sendList).encode())
                error = False
            
            elif msg == "error2":
                print("$Client disconnect")
                client.close()
                serv.close()
                break

            else:
                if error == True:
                    client.send("error0".encode())
                    #Error 0 this is error message
                else:
                    pass
                                   

