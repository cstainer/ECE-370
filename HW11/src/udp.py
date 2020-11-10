# UDP IP, PORT, and VERSION values
UDP_IP = '127.0.0.1'
UDP_PORT = 5005
VERSION = 1

# Standard message field definitions
SEP = " "
HEAD  = "RBT"
MSG_TYPE = ["SET", "GET", "ACK"]
DATA_TYPE = ["POS", "VEL"]

# Decode the message in the given buff, returns the correct English (string) version of the data in the message
def decode(buff):
    d = buff.split(SEP)
    if d[0] == HEAD:
        if d[1] == MSG_TYPE[0]:         # MSG_TYPE = SET
            if d[2] == DATA_TYPE[0]:    # DATA_TYPE = POS
                retval = "set pos = " + d[3]
            elif d[2] == DATA_TYPE[1]:  # DATA_TYPE = VEL
                retval = "set vel = " + d[3]
        elif d[1] == MSG_TYPE[1]:       # MSG_TYPE = GET
            if d[2] == DATA_TYPE[0]:    # DATA_TYPE = POS
                retval = "get pos"
            elif d[2] == DATA_TYPE[1]:  # DATA_TYPE = VEL
                retval = "get vel"
        elif d[1] == MSG_TYPE[2]:       # MSG_TYPE = ACK
            retval = "ack"
    else:
        retval = "error"
    
    return retval


# Generate a checksum for the given buff, returns a 8 bit unsigned integer
def checksum(buff):
    checksum = 0
    for i in range(len(buff) - 1):
        checksum = VERSION * (checksum + ord(buff[i]))
        
    return checksum & 0xff