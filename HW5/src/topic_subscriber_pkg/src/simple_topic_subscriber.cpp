#include <ros/ros.h>
#include <std_msgs/Int32.h>

#include <nav_msgs/Odometry.h>

void counterCallback(const std_msgs::Int32::ConstPtr &msg) {
  ROS_INFO("%d", msg->data);
}

int main(int argc, char **argv) {

  ros::init(argc, argv, "topic_subscriber");
  ros::NodeHandle nh;

  ros::Subscriber sub = nh.subscribe("odom", 1000, counterCallback);

  nav_msgs::Odometry yep;
  long double a_thing = yep.twist.twist.linear.x;

  ROS_INFO("odom printout: twist.linear.x = ");
  ROS_INFO_STREAM(a_thing);

  ros::spin();

  return 0;
}