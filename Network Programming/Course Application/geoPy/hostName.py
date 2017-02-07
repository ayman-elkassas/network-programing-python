#!/usr/bin/env python3
import socket

if __name__=='__main__':
    hostname = 'www.facebook.com'
    addr = socket.gethostbyname(hostname)
    print('the IP {} address is: {}'.format(hostname,addr))