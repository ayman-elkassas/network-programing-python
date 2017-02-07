import  socket

sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
sock.connect(('192.168.1.100',6000))
print('Client connected at {}'.format(sock.getsockname()))


delay = 0.1
text = 'Hi am Muhammed Essa your Client!'
data = text.encode('ascii')

while(True):
    sock.send(data)
    print('waiting to {} seconds for reply'.format(delay))
    sock.settimeout(delay)
    # print(sock.settimeout.__str__())
    try:
        data = sock.recv(2048)
    except socket.timeout:
          delay *=2
          if delay >3.0:
               raise RuntimeError('Maybe the Server is down!')
    else:
         break

print('The SERVER says: {}'.format(data.decode('ascii')))

