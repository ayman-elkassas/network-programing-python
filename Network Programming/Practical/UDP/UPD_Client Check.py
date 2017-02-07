import socket

sock=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
sock.connect(("192.168.1.101",6000))
print("Client connected at {}".format(sock.getsockname()))

text="Hi I am Ayman your Client!"
data=text.encode("ascii")

delay=0.1
while True:
    sock.send(data)
    print("wating to {} seconds for reply".format(delay))
    sock.settimeout(delay)
    try:
        data=sock.recv(2048)
    except:
        delay*=2
        if delay>3.0:
            raise RuntimeError("Maybe server beafya")
    else:
        break
print("the server reply {}".format(data.decode("ascii")))
