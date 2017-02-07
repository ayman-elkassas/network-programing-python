import  socket

host = 'localhost'
port = 6000
# BUFSIZE=2048

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect((host,port))

text = 'Ayman Elkassas'
s.send(text.encode('ascii'))

data = s.recv(2048)
# s.close()
print('Recieved: ', data.decode('ascii'))

#example for syn