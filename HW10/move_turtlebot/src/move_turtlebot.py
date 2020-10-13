#! /usr/bin/env python

import rospy
from std_msgs.msg import String
from geometry_msgs.msg import Twist


# Subscriber callback
def move_robot(msg):
    # Create the message to be published
    move = Twist()
    flag = True

    # Decode the incoming message
    if msg.data == "w":
        move.linear.x = 1.0
    elif msg.data == "d":
        move.angular.z = -1.0
    elif msg.data == "s":
        move.linear.x = -1.0
    elif msg.data == "a":
        move.angular.z = 1.0
    else:
        # Error case, this should not be reached if keyboard_input.py does its job correctly
        flag = False
        print "Error, unassigned key detected!"
    
    # If the input was valid, publish the decoded move command
    if flag == True:
        pub.publish(move)


# Create the node, publisher, and subscriber
rospy.init_node('move_robot_node')
pub = rospy.Publisher('/cmd_vel', Twist, queue_size=1)
sub = rospy.Subscriber('/keyboard', String, move_robot)

# Keep the node spinning until shutdown
rospy.spin()
