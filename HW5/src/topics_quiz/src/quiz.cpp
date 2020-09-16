#include <geometry_msgs/Twist.h>
#include <ros/ros.h>
#include <sensor_msgs/LaserScan.h>
#include <std_msgs/Int32.h>

sensor_msgs::LaserScan::ConstPtr gmsg;

void laserCallback(const sensor_msgs::LaserScan::ConstPtr &msg) { gmsg = msg; }

int main(int argc, char **argv) {
  ros::init(argc, argv, "topics_quiz_node");
  ros::NodeHandle nh;
  ros::Rate loop_rate(4);
  ros::Subscriber sub = nh.subscribe("/kobuki/laser/scan", 1000, laserCallback);
  ros::Publisher pub = nh.advertise<geometry_msgs::Twist>("cmd_vel", 1000);
  geometry_msgs::Twist move;

  while (ros::ok()) {
    ros::Subscriber sub =
        nh.subscribe("/kobuki/laser/scan", 1000, laserCallback);

    // If the laser reading in front of the robot is higher than 1 meter (there
    // is no obstacle closer than 1 meter in front of the robot), the robot will
    // move forward.
    if (gmsg->ranges[360] >= 1) {
      move.linear.x = 0.5;
    } else {
      move.linear.x = 0;
    }

    // If the laser reading in front of the robot is lower than 1 meter (there
    // is an obstacle closer than 1 meter in front of the robot), the robot will
    // turn left. OR If the laser reading at the right side of the robot is
    // lower than 1 meter (there is an obstacle closer than 1 meter at the right
    // side of the robot), the robot will turn left.
    if ((gmsg->ranges[360] < 1) || (gmsg->ranges[0] < 1)) {
      move.angular.z = 0.5;
    }
    // If the laser reading at the left side of the robot is lower than 1 meter
    // (there is an obstacle closer than 1 meter at the left side of the robot),
    // the robot will turn right.
    else if (gmsg->ranges[719] < 1) {
      move.angular.z = -0.5;
    }

    pub.publish(move);
    sub.shutdown();
    ros::spinOnce();
    loop_rate.sleep();
  }

  return 0;
}