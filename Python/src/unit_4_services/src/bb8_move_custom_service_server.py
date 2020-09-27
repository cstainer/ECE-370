#! /usr/bin/env python

import rospy
from srv_msg_pkg.srv import MyCustomServiceMessage, MyCustomServiceMessageResponse


def my_callback(request):
    print "Activate custom circle movement!"
    response = MyCustomServiceMessageResponse()
    response.success = True
    return response

rospy.init_node('ex43server') 
my_service = rospy.Service('/move_bb8_in_circle_custom', MyCustomServiceMessage , my_callback) # create the Service called my_service with the defined callback
rospy.spin() # maintain the service open.