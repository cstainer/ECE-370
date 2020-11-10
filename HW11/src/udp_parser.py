from socket import socket, AF_INET, SOCK_DGRAM
from udp import *

sock = socket(AF_INET, SOCK_DGRAM)
sock.bind((UDP_IP, UDP_PORT))

while True:
    data, addr = sock.recvfrom(1024)
    valid = checksum(data)

    if valid == ord(data[len(data) - 1]):
        print "valid"
        print decode(data)
    else:
        print "error"
