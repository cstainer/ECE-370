UDP_IP = '127.0.0.1'
UDP_PORT = 5005
VERSION = 1

SEP = " "
HEAD  = "RBT"
MSG_TYPE = ["SET", "GET", "ACK"]
DATA_TYPE = ["POS", "VEL"]

def decode(buff):
    d = buff.split(SEP)
    if d[0] == HEAD:
        if d[1] == MSG_TYPE[0]:
            if d[2] == DATA_TYPE[0]:
                retval = "set pos = " + d[3]
            elif d[2] == DATA_TYPE[1]:
                retval = "set vel = " + d[3]
        elif d[1] == MSG_TYPE[1]:
            if d[2] == DATA_TYPE[0]:
                retval = "get pos"
            elif d[2] == DATA_TYPE[1]:
                print "get vel"
        elif d[1] == MSG_TYPE[2]:
            pass
    
    return retval

def checksum(buff):
    checksum = 0
    for i in range(len(buff) - 1):
        checksum = VERSION * (checksum + ord(buff[i]))
        
    return checksum & 0xff