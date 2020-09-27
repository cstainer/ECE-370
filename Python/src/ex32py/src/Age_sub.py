#! /usr/bin/env python

import rospy                                          
from ex32py import Age#.msg as Age

def callback(msg):                                    
    print msg.year                                    

rospy.init_node('age_subscriber')                   

sub = rospy.Subscriber('/age', Age, callback)   
rospy.spin()
