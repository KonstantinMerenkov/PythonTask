import socket

sock = socket.socket()

sock.bind(('', 30303))
print("Connecting port 30303")

sock.listen(5)
conn, addr = sock.accept()
print("Connected >> ", addr)
while True:
    data = conn.recv(8192)
    msg = data.decode()
    print('Message >>  ', msg)
    if msg == 'exit':
        break
    resp = input('Answer >> ')
    conn.send(resp.encode())
