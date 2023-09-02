import socket

sock = socket.socket()
sock.connect(('127.0.0.1', 30303))
print('Connected to server!\n')

while True:
    msg = input('Message >> ')
    sock.send(msg.encode())
    if msg == 'exit':
        break
    data = sock.recv(8192)
    print('Answer >> ', data)
