## Programmed by Sahatsawat Kanpai 6210545629
I have tested server and client with a friend from Computer Engineering in Thai-Nichi Institute of Technology.<br>

### Requirements
- python version more than or equal 3<br>

### To use this protocol
Run socket-server.py on server side first<br>

For server side:<br>
in project directory<br>
`>python socket-server.py`<br>
And wait for client side to communicate with you...<br>

For client side with port:<br>
in project directory<br>
`>python socket-server.py {port}`<br>
such as:<br>
in project directory<br>
`>python socket-server.py 8000`<br>


For client side:<br>
in project directory<br>
`>python socket-client.py {server_ip}`<br>
such as:<br>
in project directory<br>
`>python socket-client.py 192.168.1.35`<br>

For client side with port:<br>
in project directory<br>
`>python socket-client.py {server_ip} {port}`<br>
such as:<br>
in project directory<br>
`>python socket-client.py 192.168.1.35 8000`