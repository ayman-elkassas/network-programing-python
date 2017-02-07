#!/usr/bin/env python3

import socket
from urllib.parse import quote_plus

request_text = """\
GET /maps/api/geocode/json?address={}&sensor=false HTTP/1.1\r\n\
Host: maps.google.com:80\r\n\
User-Agent: coordinates4.py\r\n\
Connection: close\r\n\
\r\n\
"""

def geocode(address):
     sock = socket.socket()
     sock.connect(('maps.google.com',80))
     request = request_text.format(quote_plus(address))
     sock.sendall(request.encode('ascii'))
     reply =b''
     while True:
         data = sock.recv(4096)
         if not data:
             break
         reply +=data
     print(reply.decode('utf-8'))

if __name__=='__main__':
      address1 = '10 Downing St, London SW1A 2AB, UK'
      geocode(address1)