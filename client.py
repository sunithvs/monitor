import socket

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect(('localhost', 65432))
    while True:
        data = s.recv(1024)
        if not data:
            break
        print(data.decode())
