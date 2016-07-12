import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((socket.gethostname(), 1234))  # привязак к адресу серверу и порта
s.listen(5)  # количество потоков которые может слушать сокет

conn, addr = s.accept()
"""Возвращает кортеж сокет который соед с клиентом и адр"""

result = conn.recv((1024))  # максчимальное количество байт
conn.send(result)
