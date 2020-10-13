#! /usr/bin/env python

import rospy
from std_msgs.msg import String

# Create the node, publisher, and message to be published
rospy.init_node('keyboard_input_node')
pub = rospy.Publisher('/keyboard', String, queue_size=1)
keyboard = String()

# User niceties
prompt = "Move turtlebot:"
help_message = "Move turtlebot with:\n\tw = forward\na = rotate left\td = rotate right\n\td = backwards"
print(help_message)

# Continuous loop
while(not rospy.is_shutdown()):
    # Get keyboard input
    keyboard.data = raw_input(prompt)

    # Error check the input
    if (keyboard.data == "w") or (keyboard.data == "a") or (keyboard.data == "s") or (keyboard.data == "d"):
        # Publish if the input is valid
        pub.publish(keyboard)
    elif (not rospy.is_shutdown()):
        # Print the help message (and do not publish) if the input is not valid
        print(help_message)
