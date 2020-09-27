#! /usr/bin/env python

import rospy                                          
from nav_msgs.msg import *

def callback(msg):                                    # Define a function called 'callback' that receives a parameter 
                                                      # named 'msg'
  
    print msg.pose.pose.position.x                                    # Print the value 'data' inside the 'msg' parameter

rospy.init_node('odom_subscriber')                   # Initiate a Node called 'topic_subscriber'

sub = rospy.Subscriber('/odom', Odometry, callback)   # Create a Subscriber object that will listen to the /counter
                                                      # topic and will cal the 'callback' function each time it reads
                                                      # something from the topic
rospy.spin()                                          # Create a loop that will keep the program in execution