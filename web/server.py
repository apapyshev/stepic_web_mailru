import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('0.0.0.0', 2222))
s.listen(1)

while True:
    client, addr = s.accept()
    data = client.recv(1024)
    if len(data) > 1024 or data == b'close':
        print("close")
        client.close()
        break
    else:
        if len(data) > 0:
            client.send(data)
            print(data)
