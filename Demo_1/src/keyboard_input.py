#! /usr/bin/env python

import rospy
from std_msgs.msg import String

# Create the node, publisher, and message to be published
rospy.init_node("ttt_key")
pub = rospy.Publisher("/keyboard", String, queue_size=1)
temp = String()
keyboard = String()
current_player = "Blue"

# User niceties
prompt = " player, select your square:"
help_message = "Select square with the following keys corresponding to their positions:\nQ W E\nA S D\nZ X C\nMake sure caps lock is off!"
print(help_message)

# Continuous loop
while(not rospy.is_shutdown()):
    # Get keyboard input
    temp.data = raw_input(current_player + prompt)

    # Error check the input
    if (temp.data == "q") or (temp.data == "w") or (temp.data == "e") or (temp.data == "a") or \
       (temp.data == "s") or (temp.data == "d") or (temp.data == "z") or (temp.data == "x") or \
       (temp.data == "c"):
        # Publish if the input is valid
        # append player
        keyboard.data = temp.data + current_player
        pub.publish(keyboard)

        # wait for response
        response = rospy.wait_for_message("/ttt_ctl", String)
        
        # if response == success
        if response.data == "success":
            # switch player
            if current_player == "Blue":
                current_player = "Red"
            else:
                current_player = "Blue"
        # elif resopnse == win
        elif response.data == "win":
            # print win message and shut down
            print(current_player + " has won!!!")
            rospy.signal_shutdown(0)
    elif (not rospy.is_shutdown()):
        # Print the help message (and do not publish) if the input is not valid
        print(help_message)
