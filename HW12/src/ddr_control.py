#!/usr/bin/env python3

from rospy import init_node, ServiceProxy, Rate, Time
from gazebo_msgs.srv import ApplyJointEffort, GetJointProperties

# API for controlling a differential drive robot
class DD_Robot_Control:

    def __init__(self, model):
        # do the rospy thing
        init_node('dd_robot_ctrl', anonymous=True)

        # define the left and right wheel addresses(?)
        self._left_wheel = model + '::left_wheel_hinge'
        self._right_wheel = model + '::right_wheel_hinge'
        
        # create the set publisher and set message
        self._set_pub = ServiceProxy('/gazebo/apply_joint_effort', ApplyJointEffort)
        self._set_msg = ApplyJointEffort()

        # create the get publisher and get message
        self._get_pub = ServiceProxy('/gazebo/get_joint_properties', GetJointProperties)
        self._get_msg = GetJointProperties()


    # Creates and sends a message to apply effort to a wheel (or wheels) for a given duration
    # wheel, either "port" for the left wheel, "starboard" for the right wheel, or "all" for both wheels
    # effort, the float representation of the amount of effort to apply
    # direction, either "ahead" for forward, or "back" for reverse
    # duration, the float number of seconds to apply the effort to the wheel
    def setEffort(self, wheel=None, effort=0.0, direction=None, duration=0.0):
        # set the message effort value to the absolute value of the effort argument for moving ahead
        if direction is "ahead":
            self._set_msg.effort = abs(effort)
        # set the message effort value to the negative of the absolute value of the effort argument for moving back
        elif direction is "back":
            self._set_msg.effort = -1 * abs(effort)

        # for all or port, send the message to apply effort to the left wheel
        if wheel is "all" or wheel is "port":
            self._set_pub(self._left_wheel, self._set_msg.effort, Time(0, 0), Time(duration, 0))
        
        # for all or starboard, send the message to apply effort to the right wheel
        if wheel is "all" or wheel is "starboard":
            self._set_pub(self._right_wheel, self._set_msg.effort, Time(0, 0), Time(duration, 0))
        

    # returns the rotation value of wheel, optionally printing it
    # wheel, either "port" for the left wheel, "starboard" for the right wheel, or "all" for both wheels
    # display, either True for printing or False for not printing
    # returns a float for "port" or "starboard", tuple of 2 floats for "all", None for error
    def getVel(self, wheel=None, display=False):
        vel = None

        # if we want both wheel speeds (wheel="all")
        if wheel is "all":
            # send messages for both wheels, saving only the rate value for each wheel in vel
            vel = (self._get_pub(self._left_wheel).rate[0], self._get_pub(self._right_wheel).rate[0])

            # if display is True, print each wheel
            if display is True:
                self.printVel(wheel="Left", vel=vel[0])
                self.printVel(wheel="Right", vel=vel[1])

        elif wheel is "port":
            # send messages for left wheel, saving only the rate value in vel
            vel = self._get_pub(self._left_wheel).rate[0]

            # if display is True, print left wheel
            if display is True:
                self.printVel(wheel="Left", vel=vel)

        elif wheel is "starboard":
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


# Test program for the class
if __name__ == '__main__':
    ddr0 = DD_Robot_Control(model="ddr0")
    wheel = "all"
    effort = 1.0
    f = 0.5 # Hz
    T = 1/f # Period
    direction = "ahead"
    rate = Rate(f)

    try:
        # Sends a sample message to the robot every 2 seconds
        while True:
            # Sends a message to apply effort of 1.0 to both wheels for 1.0 second
            # "All ahead full" = both wheels move forward with effort 1.0
            ddr0.setEffort(wheel=wheel, effort=effort, direction=direction, duration=(T/2))
            ddr0.getVel(wheel=wheel, display=True)
            rate.sleep()
    except KeyboardInterrupt:
        pass
