"""Client socket for money exchange protocol"""

__author__ = "Sahatsawat Kanpai 6210545629"
__email__ = "keyboard2543@gmail.com"

import socket
import time
import sys

server_ip = '192.168.1.1'  # Change to server ip before use this or cmd >python socket-client.py xxx.xxx.xxx.xxx
port = 8000  # To define port by command line cmd >python socket-client.py {ip} {port}
if len(sys.argv) >= 2:
    server_ip = sys.argv[1]
    if len(sys.argv) >= 3:
        try:
            port = int(sys.argv[2])
        except ValueError:
            print("Input port only an integer")
            exit()

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
try:
    s.connect((server_ip, port))
    s.send(input("Please specify amount of money and currency: ").encode())
    time.sleep(0.5)
    msg = s.recv(1024)
    print(msg.decode())
except socket.error:
    print(f"Server ip address: {server_ip}\nServer port: {port}\nServer ip/port not found")

s.close()
