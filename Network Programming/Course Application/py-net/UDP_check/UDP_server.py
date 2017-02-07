import  socket


BUFFERSIZE = 2048
PORT = 6000
HOST = '192.168.1.100'

sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
sock.bind((HOST,PORT))

print('Listening at',sock.getsockname())

while(True):
    data,address = sock.recvfrom(BUFFERSIZE)
    text = data.decode('ascii')
    print('The client at {} says {}'.format(address,text))
    message = 'Muhammed data was {} bytes long'.format(len(data))

    sock.sendto(message.encode('ascii'),address)