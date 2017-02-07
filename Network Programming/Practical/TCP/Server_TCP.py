import socket
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)

host=""
port=6000

s.bind((host,port))
print("Listening at {}".format(s.getsockname()))
s.listen(1)

while True:
    #in tcp should server accept syn client (handshake)
    client,address=s.accept()
    data=client.recv(2048)
    if data:
        print("client send {}".format(data.decode("ascii")))
        client.send(data)
    client.close()