import socket

sk = socket.socket()

sk.bind(("127.0.0.1", 8001))
sk.listen(5)

while True:
    conn, addr = sk.accept()
    data = conn.recv(8096)
    conn.send(b"HTTP/1.1 200 ok\r\n\r\n")
    conn.send('test.html')
    conn.close()