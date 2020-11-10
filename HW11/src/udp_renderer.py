from socket import socket, AF_INET, SOCK_DGRAM
from udp import *
import time as t

sock = socket(AF_INET, SOCK_DGRAM)

i = 0
while True:
    buff = HEAD + SEP + MSG_TYPE[0] + SEP + DATA_TYPE[0] + SEP + str(i) + SEP
    tail = checksum(buff)
    buff += chr(tail)

    sock.sendto(buff, (UDP_IP, UDP_PORT))
    i += 1
    t.sleep(0.5)
