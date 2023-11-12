import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(("localhost", 9999))
s.listen(5)

print("Wait your connections 😈")

while True:
    conn, addr = s.accept()
    from_client = ""

    msg = str(input("> "))
    conn.send(msg.encode())

    while True:
        data = conn.recv(1024)
        if not data:
            break
        from_client += data.decode('utf-8')
        print(from_client)
    print("Wait client...")
    conn.close()
