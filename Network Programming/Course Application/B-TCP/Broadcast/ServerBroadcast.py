import socket


# BUFFERSIZE = 2048

def server(HOST,PORT):
    sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
    sock.bind((HOST,PORT))

    print("Listening to {}".format(sock.getsockname()))

    while True:
        data , address = sock.recvfrom(2048)
        text = data.decode("ascii")
        print('the Client {} says : {}'.format(address,text))


server('',6000)