#! /usr/bin/env python

import rospy
from srv_msg_pkg.srv import MyCustomServiceMessage
import sys

# Initialise a ROS node with the name service_client
rospy.init_node('ex43client')

# Create the connection to the service
custom_bb8_circle_service = rospy.ServiceProxy('/move_bb8_in_circle_custom', MyCustomServiceMessage)

custom_bb8_circle_service.duration = 1

# Send through the connection the name of the trajectory to be executed by the robot
result = custom_bb8_circle_service()

# Print the result given by the service called
print result