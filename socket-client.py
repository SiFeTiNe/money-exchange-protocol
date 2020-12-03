"""Client socket for money exchange protocol"""

__author__ = "Sahatsawat Kanpai 6210545629"
__email__ = "keyboard2543@gmail.com"

import socket
import time
import sys

server_ip = '192.168.1.1'  # Change to server ip before use this or cmd >python socket-client.py xxx.xxx.xxx.xxx
if len(sys.argv) != 0:
    server_ip = sys.argv[0]
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((server_ip, 8000))
s.send(input("Please specify amount of money and currency: ").encode())
time.sleep(0.5)
msg = s.recv(1024)
print(msg.decode())
s.close()
