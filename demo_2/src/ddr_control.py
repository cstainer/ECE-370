#!/usr/bin/env python

import rospy
from std_msgs.msg import String
from gazebo_msgs.srv import ApplyJointEffort
from gazebo_msgs.msg import ModelState, ModelStates
from os import system

# define the left and right wheel names and model name
model = "ddr_0"
left_wheel = model + '::left_wheel_hinge'
right_wheel = model + '::right_wheel_hinge'


# API for controlling a differential drive robot

# Creates and sends a message to apply effort to a wheel (or wheels) for a given duration
# wheel, either "port" for the left wheel, "starboard" for the right wheel, or "all" for both wheels
# effort, the float representation of the amount of effort to apply
# direction, either "ahead" for forward, or "back" for reverse
# duration, the float number of seconds to apply the effort to the wheel
def setEffort(self, wheel=None, effort=0.0, direction=None, duration=0.0):
    # create the set publisher and set message
    pub = rospy.ServiceProxy('/gazebo/apply_joint_effort', ApplyJointEffort)
    msg = ApplyJointEffort()

    # set the message effort value to the absolute value of the effort argument for moving ahead
    if direction is "ahead":
        msg.effort = abs(effort)
    # set the message effort value to the negative of the absolute value of the effort argument for moving back
    elif direction is "back":
        msg.effort = -1 * abs(effort)

    # for all or port, send the message to apply effort to the left wheel
    if wheel is "all" or wheel is "port":
        pub(left_wheel, set_msg.effort, rospy.Time(0, 0), rospy.Time(duration, 0))
    
    # for all or starboard, send the message to apply effort to the right wheel
    if wheel is "all" or wheel is "starboard":
        pub(right_wheel, set_msg.effort, rospy.Time(0, 0), rospy.Time(duration, 0))
    

def setVel(self, lin={"x":0.0, "y":0.0, "z":0.0}, ang={"x":0.0, "y":0.0, "z":0.0}):
    pub = rospy.Publisher('/gazebo/set_model_state', ModelState, queue_size=1)
    msg = ModelState()
    msg.model_name = model
    msg.reference_frame = model
    
    current = rospy.wait_for_message("/gazebo/model_states", ModelStates)

    msg.pose = current.pose[1]
    msg.twist = current.twist[1]

    if lin.get("x") is not None:
        msg.twist.linear.x = lin.get("x")
    if lin.get("y") is not None:
        msg.twist.linear.y = lin.get("y")
    if lin.get("z") is not None:
        msg.twist.linear.z = lin.get("z")

    if ang.get("x") is not None:
        msg.twist.angular.x = ang.get("x")
    if ang.get("y") is not None:
        msg.twist.angular.y = ang.get("y")
    if ang.get("z") is not None:
        msg.twist.angular.z = ang.get("z")

    pub.publish(msg)


def parse(msg):
    l = msg.data.split(" ")

    if l[0] is "stop":
        setVel()
    else:
        setEffort(wheel=l[0], effort=float(l[2]), direction=l[1], duration=float(l[3]))


# init node
rospy.init_node('ddr_control_node')

# create the model of the robot
try:
    system("./del_robot.sh ddr_0")
except:
    pass
finally:
    system("./robot.sh ddr_0")

sub = rospy.Subscriber('/key2ddr', String, parse)
rospy.spin()
