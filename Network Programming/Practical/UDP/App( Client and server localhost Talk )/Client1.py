import socket
from datetime import datetime
# print(datetime.now())

sock=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

for i in range(5):
    text="the time is {}".format(datetime.now())
    data=text.encode("ascii")
    sock.sendto(data,("127.0.0.1",3000))
    print("client assigned to address {}".format(sock.getsockname()))
    data,address= sock.recvfrom(1024)#recvfrom return with a tuple of tuple (data ,(address,port))
    # print(data)
    # print(address[0])
    text=data.decode("ascii")
    print('The Server {} replied {}'.format(address,data))