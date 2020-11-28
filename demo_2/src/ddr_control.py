#!/usr/bin/env python3

import rospy
from gazebo_msgs.srv import ApplyJointEffort, GetJointProperties
from gazebo_msgs.msg import ModelState, ModelStates
from std_msgs.msg import String
from os import system, devnull
from subprocess import call

# API for controlling a differential drive robot
class DD_Robot_Control:

    def __init__(self, model):

        # define the left and right wheel addresses(?)
        self._left_wheel = model + '::left_wheel_hinge'
        self._right_wheel = model + '::right_wheel_hinge'
        
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
        # set the message effort value to the absolute value of the effort argument for moving ahead
        if direction == "ahead":
            self._set_msg.effort = abs(effort)
        # set the message effort value to the negative of the absolute value of the effort argument for moving back
        elif direction == "back":
            self._set_msg.effort = -1 * abs(effort)

        # for all or port, send the message to apply effort to the left wheel
        if wheel == "all" or wheel == "port":
            self._set_pub(self._left_wheel, self._set_msg.effort, rospy.Time(0, 0), rospy.Time(duration, 0))
        
        # for all or starboard, send the message to apply effort to the right wheel
        if wheel == "all" or wheel == "starboard":
            self._set_pub(self._right_wheel, self._set_msg.effort, rospy.Time(0, 0), rospy.Time(duration, 0))
        

    # returns the rotation value of wheel, optionally printing it
    # wheel, either "port" for the left wheel, "starboard" for the right wheel, or "all" for both wheels
    # display, either True for printing or False for not printing
    # returns a float for "port" or "starboard", tuple of 2 floats for "all", None for error
    def getVel(self, wheel=None, display=False):
        vel = None

        # if we want both wheel speeds (wheel="all")
        if wheel == "all":
            # send messages for both wheels, saving only the rate value for each wheel in vel
            vel = (self._get_pub(self._left_wheel).rate[0], self._get_pub(self._right_wheel).rate[0])

            # if display is True, print each wheel
            if display is True:
                self.printVel(wheel="Left", vel=vel[0])
                self.printVel(wheel="Right", vel=vel[1])

        elif wheel == "port":
            # send messages for left wheel, saving only the rate value in vel
            vel = self._get_pub(self._left_wheel).rate[0]

            # if display is True, print left wheel
            if display is True:
                self.printVel(wheel="Left", vel=vel)

        elif wheel == "starboard":
            # send messages for right wheel, saving only the rate value in vel
            vel = self._get_pub(self._right_wheel).rate[0]

            # if display is True, print right wheel
            if display is True:
                self.printVel(wheel="Right", vel=vel)
        
        return vel

    
    # prints a nicely formatted output for the given wheel and vel information, including direction
    # returns nothing
    def printVel(self, wheel=None, vel=0.0):
        if vel > 0.0:
            print(wheel + " wheel speed is " + str(vel) + ", direction is ahead.")
        elif vel < 0.0:
            print(wheel + " wheel speed is " + str(vel) + ", direction is back.")
        elif vel == 0.0:
            print(wheel + " is stopped.")


# init ROS node
rospy.init_node('dd_robot_ctrl', anonymous=True)

def parse(msg):
    ddr0 = DD_Robot_Control(model="ddr_0")
    l = msg.data.split(" ")
    ddr0.setEffort(wheel=l[0], effort=float(l[2]), direction=l[1], duration=float(l[3]))

# create the model of the robot
#with open(devnull, 'w') as FNULL:
# TODO fix indent!
try:
    #call("./del_robot.h ddr_0", stdout=FNULL)
    system("rosservice call gazebo/delete_model ddr_0")
except:
    pass
finally:
    #call("./robot.h ddr_0", stdout=FNULL)
    system("rosrun gazebo_ros spawn_model -file /home/user/catkin_ws/src/demo_2/models/ddr.sdf -sdf -model ddr_0")
    #close(FNULL) # TODO is this necessary? or even legal?  I kinda don't think so

sub = rospy.Subscriber('/key2ddr', String, parse)
rospy.spin()
