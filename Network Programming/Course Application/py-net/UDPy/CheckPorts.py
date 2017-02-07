import socket

muhammed = socket.getservbyname('telnet')
print(muhammed)
essa = socket.getservbyport(21)
print(essa)