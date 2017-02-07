import  socket

BUFFERSIZE = 2048

def client(HOST,PORT):
    sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
    sock.setsockopt(socket.SOL_SOCKET,socket.SO_BROADCAST,1)
    text = "this is Broadcast message !"
    sock.sendto(text.encode('ascii'),(HOST,PORT))


client('<broadcast>',6000)