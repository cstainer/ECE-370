#!/usr/bin/env python3

import rospy
from gazebo_msgs.srv import ApplyJointEffort, GetJointProperties
from gazebo_msgs.msg import ModelState, ModelStates
from std_msgs.msg import String
from os import system

# API for controlling a differential drive robot
class DD_Robot_Control:

    def __init__(self, model):

        # define the left and right wheel addresses(?)
        self._left_front_wheel = model + '::left_front_wheel_hinge'
        self._right_front_wheel = model + '::right_front_wheel_hinge'
        self._left_rear_wheel = model + '::left_rear_wheel_hinge'
        self._right_rear_wheel = model + '::right_rear_wheel_hinge'

        # create the set publisher and set message
        self._set_pub = rospy.ServiceProxy('/gazebo/apply_joint_effort', ApplyJointEffort)
        self._set_msg = ApplyJointEffort()

        # create the get publisher and get message
        self._get_pub = rospy.ServiceProxy('/gazebo/get_joint_properties', GetJointProperties)
        self._get_msg = GetJointProperties()


    # Creates and sends a message to apply effort to a wheel (or wheels) for a given duration
    # wheel, either "port" for the left wheel, "starboard" for the right wheel, or "all" for both wheels
    # effort, the float representation of the amount of effort to apply
    # direction, either "ahead" for forward, or "back" for reverse
    # duration, the float number of seconds to apply the effort to the wheel
    def setEffort(self, wheel=None, effort=0.0, direction=None, duration=0.0):        
        if wheel == "all":
            if direction == "ahead":
                self._set_msg.effort = 1.5 * abs(effort)
                self._set_pub(self._left_front_wheel, self._set_msg.effort, rospy.Time(0, 0), rospy.Time(duration, 0))
                self._set_pub(self._right_front_wheel, self._set_msg.effort, rospy.Time(0, 0), rospy.Time(duration, 0))
                self._set_pub(self._left_rear_wheel, self._set_msg.effort, rospy.Time(0, 0), rospy.Time(duration, 0))
                self._set_pub(self._right_rear_wheel, self._set_msg.effort, rospy.Time(0, 0), rospy.Time(duration, 0))
            elif direction == "back":
                self._set_msg.effort = -1 * abs(effort)
                self._set_pub(self._left_front_wheel, self._set_msg.effort, rospy.Time(0, 0), rospy.Time(duration, 0))
                self._set_pub(self._right_front_wheel, self._set_msg.effort, rospy.Time(0, 0), rospy.Time(duration, 0))
                self._set_pub(self._left_rear_wheel, self._set_msg.effort, rospy.Time(0, 0), rospy.Time(duration, 0))
                self._set_pub(self._right_rear_wheel, self._set_msg.effort, rospy.Time(0, 0), rospy.Time(duration, 0))
        elif wheel == "port":
            self._set_msg.effort = 5 * abs(effort)
            self._set_pub(self._left_front_wheel, self._set_msg.effort, rospy.Time(0, 0), rospy.Time(duration, 0))
            self._set_msg.effort = -5 * abs(effort)
            self._set_pub(self._right_front_wheel, self._set_msg.effort, rospy.Time(0, 0), rospy.Time(duration, 0))
        elif wheel == "starboard":
            self._set_msg.effort = -5 * abs(effort)
            self._set_pub(self._left_front_wheel, self._set_msg.effort, rospy.Time(0, 0), rospy.Time(duration, 0))
            self._set_msg.effort = 5 * abs(effort)
            self._set_pub(self._right_front_wheel, self._set_msg.effort, rospy.Time(0, 0), rospy.Time(duration, 0))


# init ROS node
rospy.init_node('final_robot_ctrl', anonymous=True)

# parse an incoming message, create an instance of the robot, and call the robot's setEffort with the message's information
def parse(msg):
    ddr0 = DD_Robot_Control(model="4x4_0")
    l = msg.data.split(" ")
    ddr0.setEffort(wheel=l[0], effort=float(l[2]), direction=l[1], duration=float(l[3]))

# create the model of the robot
try:
    # reset the gazebo environment
    system("/home/user/catkin_ws/src/final/src/del_robot.sh 4x4_0")
    system("/home/user/catkin_ws/src/final/src/del_robot.sh final_setup_test")
    system("/home/user/catkin_ws/src/final/src/del_robot.sh final_setup")
except:
    pass
finally:
    # load the final model and the robot
    system("/home/user/catkin_ws/src/final/src/final.sh")
    system("/home/user/catkin_ws/src/final/src/spawn_robot.sh 4x4_0")

sub = rospy.Subscriber('/key2ddr', String, parse)
rospy.spin()
