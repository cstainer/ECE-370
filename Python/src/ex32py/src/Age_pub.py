#! /usr/bin/env python

import rospy
from ex32py import Age#.msg as Age

def age():
    pub = rospy.Publisher('age', Age, queue_size=10)
    rospy.init_node('ex33py')                   
    rate = rospy.Rate(2)
    while not rospy.is_shutdown:
        Age.year = 2020
        Age.month = 9
        Age.day = 26
        pub.publish(Age)
        rate.sleep()

if __name__ == '__main__':
    try:
        age()
    except rospy.ROSInterruptException:
        pass
