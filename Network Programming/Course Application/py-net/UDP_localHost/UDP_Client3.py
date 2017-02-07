import  socket
from datetime import datetime

PORT = 3000

sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

for i in range(5):
    text = 'the time is {}'.format(datetime.now())
    data = text.encode('ascii')
    sock.sendto(data,('127.0.0.1',PORT))
    print('Client assigned to address {}'.format(sock.getsockname()))
    data,address= sock.recvfrom(1024)
    text = data.decode('ascii')
    print('The Server {} replied {}'.format(address,data))



