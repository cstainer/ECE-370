from socket import socket, AF_INET, SOCK_DGRAM
from udp import *
import time as t

sock = socket(AF_INET, SOCK_DGRAM)      # Create the socket

i = 0       # Sample data
while True:
    buff = HEAD + SEP + MSG_TYPE[0] + SEP + DATA_TYPE[0] + SEP + str(i) + SEP   # concatenate the message
    tail = checksum(buff)       # generate the checksum
    buff += chr(tail)           # append the checksum to the message

    sock.sendto(buff, (UDP_IP, UDP_PORT))   # feed the message into the socket
    i += 1                      # update the sample data
    t.sleep(0.5)                # sleep for 1/2 second
