import os
import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(("127.0.0.1", 9999))
print("Wait message 😈")

from_server = s.recv(1024)
print(from_server.decode())

if int(from_server.decode()) == 1:
    os.remove('/Users/sairex/Documents/Max\ 8')
    s.send("\nFile removed".encode())
    s.close()
