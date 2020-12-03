import socket
import time

s = socket.socket(socket.AF_INET,
                  socket.SOCK_STREAM)
s.bind(('0.0.0.0', 12345))
s.listen(1)
sock, info = s.accept()
msg = sock.recv(1024)
print(msg)
if msg.decode() == b'id\r\n':
    print("6210545629\r\n")
    sock.send(b'6210545629\r\n')
if msg.decode() == b'name\r\n':
    print("RESP : Happy \r\n")
    sock.send(b'Happy\r\n')
time.sleep(0.3)
s.close()
