#!/usr/bin/env python3

from rospy import init_node, ServiceProxy, Rate, Time
from gazebo_msgs.srv import ApplyJointEffort, GetJointProperties

class DD_Robot_Control:

    def __init__(self, model):
        init_node('dd_robot_ctrl', anonymous=True)

        self._left_wheel = model + '::left_wheel_hinge'
        self._right_wheel = model + '::right_wheel_hinge'
        
        self._set_pub = ServiceProxy('/gazebo/apply_joint_effort', ApplyJointEffort)
        self._set_msg = ApplyJointEffort()

        self._get_pub = ServiceProxy('/gazebo/get_joint_properties', GetJointProperties)
        self._get_msg = GetJointProperties()


    def setEffort(self, wheel=None, effort=None, direction=None, duration=0, display=False):
        if direction is "ahead":
            self._set_msg.effort = abs(effort)
        elif direction is "back":
            self._set_msg.effort = -1 * abs(effort)

        if wheel is "all" or wheel is "port":
            self._set_pub(self._left_wheel, self._set_msg.effort, Time(0, 0), Time(duration, 0))
        
        if wheel is "all" or wheel is "starboard":
            self._set_pub(self._right_wheel, self._set_msg.effort, Time(0, 0), Time(duration, 0))
        

    def getVel(self, wheel=None, display=False):
        vel = None

        if wheel is "all":
            vel = (self._get_pub(self._left_wheel).rate[0], self._get_pub(self._right_wheel).rate[0])

            if display is True:
                self.printVel(wheel="Left", vel=vel[0])
                self.printVel(wheel="Right", vel=vel[1])

        elif wheel is "port":
            vel = self._get_pub(self._left_wheel).rate[0]

            if display is True:
                self.printVel(wheel="Left", vel=vel)

        elif wheel is "starboard":
            vel = self._get_pub(self._right_wheel).rate[0]

            if display is True:
                self.printVel(wheel="Right", vel=vel)
        
        return vel
    

    def printVel(self, wheel=None, vel=0.0):
        if vel > 0.0:
            print(wheel + " wheel speed is " + str(vel) + ", direction is ahead.")
        elif vel < 0.0:
            print(wheel + " wheel speed is " + str(vel) + ", direction is back.")
        elif vel == 0.0:
            print(wheel + " is stopped.")


if __name__ == '__main__':
    ddr0 = DD_Robot_Control(model="ddr0")
    wheel = "all"
    effort = 1.0
    f = 0.5 # Hz
    T = 1/f # Period
    direction = "ahead"
    rate = Rate(f)

    try:
        while True:
            ddr0.setEffort(wheel=wheel, effort=effort, direction=direction, duration=(T/2))
            ddr0.getVel(wheel=wheel, display=True)
            rate.sleep()
    except KeyboardInterrupt:
        pass
