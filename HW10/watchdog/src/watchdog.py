#! /usr/bin/env python

import rospy
from std_msgs.msg import String
from geometry_msgs.msg import Twist
import time


# Global initial timestamp
time0 = time.time()


# Subscriber callback
def update_time(msg):
    # Update global initial timestamp
    global time0 = time.time()


# Global timebox constant, or as close as you can get to it in Python
def timebox():
    return 2.0


# Create node, publisher, and subscriber
rospy.init_node('watchdog_node')
pub = rospy.Publisher('/cmd_vel', Twist, queue_size=1)
sub = rospy.Subscriber('/keyboard', String, update_time)

# Coninuous loop
while(not rospy.is_shutdown()):
    # If the timebox is exceeded
    if (time.time() - time0) > timebox():
        # Publish the stop message
        pub.publish(Twist())
