import  socket

host = ''
port = 60000


s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.bind((host,port))
print('Listening to {}'.format(s.getsockname()))
s.listen(1)


while True:
    client , address = s.accept()
    data = client.recv(2048)

    if data:
        print('Client: ', data.decode('ascii'))
        client.send(data)
    client.close()