"""Server socket for money exchange protocol"""

__author__ = "Sahatsawat Kanpai 6210545629"
__email__ = "keyboard2543@gmail.com"

import socket
import time
import datetime
from currency import Currency
import sys

port = 8000
if len(sys.argv) >= 2:
    try:
        port = int(sys.argv[1])
    except ValueError:
        print("Input port only an integer")
        exit()

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('0.0.0.0', port))
s.listen(1)
sock, info = s.accept()
msg = sock.recv(1024)
decoded_msg = msg.decode()
print(decoded_msg)
decoded_msg_list = decoded_msg.split(' ')

amount = float(decoded_msg_list[0])
currency = decoded_msg_list[1]
converted = 'Non Currency'
chosen_curr = Currency.BAHT

for itr_curr in Currency:
    if itr_curr.value['currency'] == currency:
        chosen_curr = itr_curr
        break

time_in_string = datetime.datetime.now().strftime("%d %b %Y, %I:%M %p\n")
sent_msg = time_in_string + chosen_curr.convert_to_all_in_string(amount)
sock.send(sent_msg.encode())

time.sleep(0.3)
s.close()
