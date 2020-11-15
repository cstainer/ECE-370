#!/bin/bash

rosrun gazebo_ros spawn_model -file /home/user/catkin_ws/src/demo_2/models/box.urdf -urdf -x $1 -y $2 -model $3