import  socket
sock=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

BUFFERSIZE = 2048
PORT = 6000
HOST = '192.168.1.100'

sock.bind(((HOST),PORT))
print("Server listen on {}".format(sock.getsockname()))

while True:
    data,address=sock.recvfrom(BUFFERSIZE)
    text=data.decode("ascii")
    print("Client send {} to server".format(text))
    text="Client send {} bytes to server".format(len(data))
    data=text.encode("ascii")
    sock.sendto(data,address)
