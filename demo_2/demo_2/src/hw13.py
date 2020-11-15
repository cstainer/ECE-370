#!/usr/bin/env python

from subprocess import check_call

i = 0
x = 0
y = 0

# left side of square
print "left side of square"
y = 25
for x in range(-25, 25, 2):
    check_call("./hw13.sh '%s' '%s' '%s'" % (str(x), str(y), str("box_" + str(i))), shell=True)
    i += 1

# top of square
print "top of square"
x = 25
for y in range(-25, 25, 2):
    check_call("./hw13.sh '%s' '%s' '%s'" % (str(x), str(-1 * y), str("box_" + str(i))), shell=True)
    i += 1

# right side of square
print "right side of square"
y = -25
for x in range(-25, 25, 2):
    check_call("./hw13.sh '%s' '%s' '%s'" % (str(-1 * x), str(y), str("box_" + str(i))), shell=True)
    i += 1

# bottom of square
print "bottom of square"
x = -25
for y in range(-25, 25, 2):
    check_call("./hw13.sh '%s' '%s' '%s'" % (str(x), str(y), str("box_" + str(i))), shell=True)
    i += 1
