#! /usr/bin/env python

import rospy
from std_srvs.srv import Empty
import sys

# Initialise a ROS node with the name service_client
rospy.init_node('ex42client')

# Create the connection to the service
bb8_circle_service = rospy.ServiceProxy('/move_bb8_in_circle', Empty)

# Send through the connection the name of the trajectory to be executed by the robot
result = bb8_circle_service()

# Print the result given by the service called
print result