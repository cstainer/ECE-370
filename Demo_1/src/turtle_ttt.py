#!/usr/bin/env python

import rospy
from geometry_msgs.msg import Twist
from nav_msgs.msg import Odometry
from std_msgs.msg import String
import math
from tf.transformations import euler_from_quaternion
from sensor_msgs.msg import LaserScan


class Turtle():

    def __init__(self):
        self.tur_cmd = rospy.Publisher("/cmd_vel", Twist, queue_size=1)
        self.move = Twist()
        self.desired_x = 0.0
        self.desired_z = 0.0
        self.expected_x = 0.0
        self.expected_y = 0.0
        self.ttt_cmd = rospy.Subscriber("/ttt_cmd", Twist, self.update_desired)
        self.ttt_ret = rospy.Publisher("/ttt_ret", String, queue_size=1)
        self.ret = String()
        self.ret.data = "done"


    def move_turtle(self):
        # turn turtle
        msg = rospy.wait_for_message("/odom", Odometry)
        roll, pitch, yaw = euler_from_quaternion([msg.pose.pose.orientation.x, msg.pose.pose.orientation.y, msg.pose.pose.orientation.z, msg.pose.pose.orientation.w])
        target_rad = self.desired_z * math.pi / 180

        while ((target_rad - yaw) > 0.01):
            self.move.angular.z = target_rad - yaw

            if self.move.angular.z > 0.3:
                self.move.angular.z = 0.3
            
            if self.move.angular.z < -0.3:
                self.move.angular.z = -0.3

            self.tur_cmd.publish(self.move)
            msg = rospy.wait_for_message("/odom", Odometry)
            roll, pitch, yaw = euler_from_quaternion([msg.pose.pose.orientation.x, msg.pose.pose.orientation.y, msg.pose.pose.orientation.z, msg.pose.pose.orientation.w])
            target_rad = self.desired_z * math.pi / 180

        # done turning
        self.move.angular.z = 0.0
        self.tur_cmd.publish(self.move)

        # forward/backward move turtle
        # -0.1 is code for "push the block", so we do it by time/speed rather than with the laser
        if self.desired_x == -0.1:
            self.move.linear.x = 0.5
            self.tur_cmd.publish(self.move)
            rospy.sleep(1.7)
            self.move.linear.x = 0.0
            self.tur_cmd.publish(self.move)
            self.ttt_ret.publish(self.ret)
            return
        # -0.2 is code for "do not move forward/backward", so we publish a stop message (just to be sure) and return
        elif self.desired_x == -0.2:
            self.move.linear.x = 0.0
            self.tur_cmd.publish(self.move)
            self.ttt_ret.publish(self.ret)
            return

        # else turtle moves until he is self.desired_x away from the wall directly in front of himself
        las = rospy.wait_for_message("/kobuki/laser/scan", LaserScan)
        
        while ((las.ranges[360] - self.desired_x) > 0.01):
            self.move.linear.x = las.ranges[360] - self.desired_x
            
            if self.move.linear.x > 0.6:
                self.move.linear.x = 0.6
            
            if self.move.linear.x < -0.6:
                self.move.linear.x = -0.6
            
            self.tur_cmd.publish(self.move)
            las = rospy.wait_for_message("/kobuki/laser/scan", LaserScan)

        # done moving, publish a stop message and the return message so that tic_tac_toe knows he's stopped wandering about
        self.move.linear.x = 0.0
        self.tur_cmd.publish(self.move)
        self.ttt_ret.publish(self.ret)

    
    # callback for new cmd message
    def update_desired(self, msg):
        # update the current desired position
        self.desired_x = msg.linear.x    # distance to wall in front
        self.desired_z += msg.angular.z  # heading
        
        if abs(self.desired_z) > 180.0:
            self.desired_z = msg.angular.z * -1   

        if self.desired_z == 0.0:
            self.expected_x += self.desired_x
        elif abs(self.desired_z) == 180.0:
            self.expected_x -= self.desired_x
        elif self.desired_z == 90.0:
            self.expected_y += self.desired_x
        elif self.desired_z == -90.0:
            self.expected_y -= self.desired_x
        
        self.move_turtle()


# this is mostly here for standalone testing
if __name__ == '__main__':
    rospy.init_node('turtle_ttt')
    turtle = Turtle()
    rospy.spin()
