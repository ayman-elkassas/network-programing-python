import socket
if __name__=="__main__":
    hostname="www.linkedin.com"
    ip=socket.gethostbyname(hostname)
    print('the ip of domain {} is {}'.format(hostname, ip))