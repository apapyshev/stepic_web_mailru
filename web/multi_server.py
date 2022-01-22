import socket
import os
import sys

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('0.0.0.0', 2222))
s.listen(10)

while True:
    client, addr = s.accept()
    child_pid = os.fork()
    if child_pid == 0:
        data = client.recv(1024)
        if len(data) > 1024 or data == b'close':
            print("Connection close")
            client.close()
            break
        else:
            if len(data) > 0:
                client.send(data)
                print(data)
        sys.exit()
    else:
        client.close()

s.close()
