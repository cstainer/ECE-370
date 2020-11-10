from socket import socket, AF_INET, SOCK_DGRAM
from udp import *

# Create the socket and bind it to the port
sock = socket(AF_INET, SOCK_DGRAM)
sock.bind((UDP_IP, UDP_PORT))

while True:
    data, addr = sock.recvfrom(1024)        # Blocking listen on the port
    valid = checksum(data)                  # Check that the incoming message is correct

    if valid == ord(data[len(data) - 1]):   # If the incoming message is verified correct
        print "valid"                       # Print the message
        print decode(data)
    else:                                   # else, print that there has been an error
        print "error"
