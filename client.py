import socket

sock = socket.socket()
sock.connect((socket.gethostname(), 1212))
sock.send(b'hello, world!\n')

data = sock.recv(1024)
sock.close()

print(data)