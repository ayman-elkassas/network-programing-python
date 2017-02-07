import  socket

host = '127.0.0.1'
port = 6000
BUFSIZE=2048

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect((host,port))

text = 'Muhammed Essa'
s.send(text.encode('ascii'))


data = s.recv(BUFSIZE)
s.close()
print('Recieved: ', data.decode('ascii'))