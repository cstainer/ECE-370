#include <geometry_msgs/Twist.h>
#include <ros/ros.h>
#include <std_msgs/Int32.h>

int main(int argc, char **argv) {

  ros::init(argc, argv, "topic_publisher");
  ros::NodeHandle nh;

  ros::Publisher pub = nh.advertise<geometry_msgs::Twist>("cmd_vel", 1000);
  ros::Rate loop_rate(2);

  //std_msgs::Int32 count;
  //count.data = 0;

  geometry_msgs::Twist var;
  var.linear.x = 0.5;
  var.angular.z = 0.5;

  while (ros::ok()) {
    // pub.publish(count);
    // ros::spinOnce();
    // loop_rate.sleep();
    //++count.data;

    pub.publish(var);
    ros::spinOnce();
    loop_rate.sleep();
  }

  return 0;
}