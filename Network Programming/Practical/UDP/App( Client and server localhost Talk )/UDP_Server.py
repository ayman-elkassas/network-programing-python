import socket
#determine ip type ( IPv4,IPv6 ) and transimision protocol type ( TCP OR UDP )
sock=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
sock.bind(("127.0.0.1",3000)) #bind means join or connect and listen
print("Listening to {}".format(sock.getsockname()))

while True:#because the server in looping all the time
    data1,address=sock.recvfrom(1024)
    text=data.decode("ascii")
    print('Client at {} date : {}'.format(address, text))
    text = 'the client data was {} bytes long'.format(len(data))
    data=text.encode("ascii")
    sock.sendto(data,address)

#the server in loop cycle all of the time
#1-recevie data
#2-decode
#3-read
#4-prepare reply
#5-encode
#6-send reply to sender of request