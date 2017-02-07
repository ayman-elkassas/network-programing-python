#import modules
import socket

#code functions
def server(host,port):
    sock=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
    sock.bind((host,port))
    print("Listening at {}".format(sock.getsockname()))

    while True:
        data,address=sock.recvfrom(2048)
        text=data.decode("ascii")
        print("Client {} send : {}".format(address,data))

server("",6000)