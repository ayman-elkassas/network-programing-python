import socket

def client(host,port):
    sock=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
    # option to the socket that enable to generate braodcast message
    sock.setsockopt(socket.SOL_SOCKET,socket.SO_BROADCAST,1)
    text="this is Broadcast message !"
    data=text.encode("ascii")
    sock.sendto(data,(host,port))

client("<broadcast>",6000)
