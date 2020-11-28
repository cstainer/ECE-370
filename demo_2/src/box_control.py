#!/usr/bin/env python

import rospy
from os import system, devnull
from gazebo_msgs.msg import ModelStates
from subprocess import call

flag = False
x_pos_boxes = [] # x = 26.25
x_neg_boxes = [] # x = -26.25
y_pos_boxes = [] # y = 26.25
y_neg_boxes = [] # y = -26.25
dropped_boxes = []
step = 1.25
box_serial_number = 0
error_correct = 0.1

def calc_all_boxes(msg):
    # starting point is along the x positive wall
    if msg.pose[1].position.x >= 25:
        temp = msg.pose[1].position.y

        # x positive wall
        while temp < 26.25:
            x_pos_boxes.append(temp)
            temp += step

        # y positive wall
        temp -= step
        offset = 26.25 - temp
        temp = 26.25 - (offset + error_correct)

        while temp > -26.25:
            y_pos_boxes.append(temp)
            temp -= step

        # x negative wall
        temp += step
        offset = 26.25 + temp
        temp = 26.25 - (offset + error_correct)

        while temp > -26.25:
            x_neg_boxes.append(temp)
            temp -= step
        
        # y negative wall
        temp += step
        offset = -26.25 - temp
        temp = -26.25 - (offset - error_correct)

        while temp < 26.25:
            y_neg_boxes.append(temp)
            temp += step

        # x positive wall
        temp -= step
        offset = -26.25 + temp
        temp = -26.25 - (offset - error_correct)

        while temp < (x_pos_boxes[0] - 1):
            x_pos_boxes.append(temp)
            temp += step

    # starting point is along x negative wall
    elif msg.pose[1].position.x <= -25:
        temp = msg.pose[1].position.y

        # x negative wall
        while temp > -26.25:
            x_neg_boxes.append(temp)
            temp -= step

        # y negative wall
        temp += step
        offset = -26.25 - temp
        temp = -26.25 - (offset - error_correct)

        while temp < 26.25:
            y_neg_boxes.append(temp)
            temp += step
        
        # x positive wall
        temp -= step
        offset = -26.25 + temp
        temp = -26.25 - (offset - error_correct)

        while temp < 26.25:
            x_pos_boxes.append(temp)
            temp += step

        # y positive wall
        temp -= step
        offset = 26.25 - temp
        temp = 26.25 - (offset + error_correct)

        while temp > -26.25:
            y_pos_boxes.append(temp)
            temp -= step

        # x negative wall
        temp += step
        offset = 26.25 + temp
        temp = 26.25 - (offset + error_correct)

        while temp > (x_neg_boxes[0] + 1):
            x_neg_boxes.append(temp)
            temp -= step

    # starting point is along the y positive wall
    elif msg.pose[1].position.y >= 25:
        temp = msg.pose[1].position.x

        # y positive wall
        while temp > -26.25:
            y_pos_boxes.append(temp)
            temp -= step
        
        # x negative wall
        temp += step
        offset = 26.25 + temp
        temp = 26.25 - (offset + error_correct)

        while temp > -26.25:
            x_neg_boxes.append(temp)
            temp -= step

        # y negative wall
        temp += step
        offset = -26.25 - temp
        temp = -26.25 - (offset - error_correct)

        while temp < 26.25:
            y_neg_boxes.append(temp)
            temp += step
        
        # x positive wall
        temp -= step
        offset = -26.25 + temp
        temp = -26.25 - (offset - error_correct)

        while temp < 26.25:
            x_pos_boxes.append(temp)
            temp += step

        # y positive wall
        temp -= step
        offset = 26.25 - temp
        temp = 26.25 - (offset + error_correct)

        while temp > (y_pos_boxes[0] + 1):
            y_pos.append(temp)
            temp -= step

    # starting point is along the y negative wall
    elif msg.pose[1].position.y <= -25:
        temp = msg.pose[1].position.x

        # y negative wall
        while temp < 26.25:
            y_neg_boxes.append(temp)
            temp += step
        
        # x positive wall
        temp -= step
        offset = -26.25 + temp
        temp = -26.25 - (offset - error_correct)

        while temp < 26.25:
            x_pos_boxes.append(temp)
            temp += step

        # y positive wall
        temp -= step
        offset = 26.25 - temp
        temp = 26.25 - (offset + error_correct)

        while temp > -26.25:
            y_pos_boxes.append(temp)
            temp -= step

        # x negative wall
        temp += step
        offset = 26.25 + temp
        temp = 26.25 - (offset + error_correct)

        while temp > -26.25:
            x_neg_boxes.append(temp)
            temp -= step

        # y negative wall
        temp += step
        offset = -26.25 - temp
        temp = -26.25 - (offset - error_correct)

        while temp < (y_neg_boxes[0] - 1):
            y_neg_boxes.append(temp)
            temp += step
    
    x_pos_boxes.sort()
    x_neg_boxes.sort()
    y_pos_boxes.sort()
    y_neg_boxes.sort()

# find the closest box in the list of possible boxes
# https://www.geeksforgeeks.org/python-find-closest-number-to-k-in-given-list/ 
def find_closest(r, b_list):
    return b_list[min(range(len(b_list)), key = lambda i: abs(b_list[i]-r))] 

# check the position of the robot
def check(msg):
    try:
        # if the robot is at or outside of the limit of the field
        if abs(msg.pose[1].position.x) >= 25 or abs(msg.pose[1].position.y) >= 25:
            global flag
            global box_serial_number
            
            # if this is the first time the robot has exceeded field limits
            if flag is False:
                # calculate the positions of all boxes
                calc_all_boxes(msg)
                flag = True
            
            # find the closest box 
            # the robot is approaching the x positive wall
            if msg.pose[1].position.x >= 25:
                # find the closest box to the robot
                closest = find_closest(msg.pose[1].position.y, x_pos_boxes)

                # if the closest box has already been dropped
                if ((26.25, closest) in dropped_boxes):
                    # do nothing
                    pass
                # else the closet box has not yet been dropped
                else:
                    # drop box at (26.25, closest)
                    #with open(devnull, 'w') as FNULL:      # TODO finish this!
                    #    call("./drop_box.sh " + str(26.25) + " " + str(closest) + " box" + str(box_serial_number), stdout=FNULL)
                    system("rosrun gazebo_ros spawn_model -file /home/user/catkin_ws/src/demo_2/models/box.urdf -urdf -x " + str(26.25) + " -y " + str(closest) + " -model box" + str(box_serial_number))
                    box_serial_number += 1
                    dropped_boxes.append((26.25, closest))

            # the robot is approaching the x negative wall
            elif msg.pose[1].position.x <= -25:
                # find the closest box to the robot
                closest = find_closest(msg.pose[1].position.y, x_neg_boxes)

                # if the closest box has already been dropped
                if ((-26.25, closest) in dropped_boxes):
                    # do nothing
                    pass
                # else the closest box has not yet been dropped
                else:
                    # drop box at (-26.25, closest)
                    #with open(devnull, 'w') as FNULL:      # TODO finish this!
                    #    call("./drop_box.sh " + str(-26.25) + " " + str(closest) + " box" + str(box_serial_number), stdout=FNULL)
                    system("rosrun gazebo_ros spawn_model -file /home/user/catkin_ws/src/demo_2/models/box.urdf -urdf -x " + str(-26.25) + " -y " + str(closest) + " -model box" + str(box_serial_number))
                    box_serial_number += 1
                    dropped_boxes.append((-26.25, closest))

            # the robot is approaching the y positive wall
            elif msg.pose[1].position.y >= 25:
                # find the closest box to the robot
                closest = find_closest(msg.pose[1].position.x, y_pos_boxes)

                # if the closest box has already been dropped
                if ((closest, 26.25) in dropped_boxes):
                    # do nothing
                    pass
                # else the closest box has not yet been dropped
                else:
                    # drop box at (closest, 26.25)
                    #with open(devnull, 'w') as FNULL:      # TODO finish this!
                    #    call("./drop_box.sh " + str(closest) + " " + str(26.25) + " box" + str(box_serial_number), stdout=FNULL)
                    system("rosrun gazebo_ros spawn_model -file /home/user/catkin_ws/src/demo_2/models/box.urdf -urdf -x " + str(closest) + " -y " + str(26.25) + " -model box" + str(box_serial_number))
                    box_serial_number += 1
                    dropped_boxes.append((closest, 26.25))

            # the robot is approaching the y negative wall
            elif msg.pose[1].position.y <= -25:
                # find the closest box to the robot
                closest = find_closest(msg.pose[1].position.x, y_neg_boxes)

                # if the closest box has already been dropped
                if ((closest, -26.25) in dropped_boxes):
                    # do nothing
                    pass
                else:
                    # drop box at (closest, -26.25)
                    #with open(devnull, 'w') as FNULL:      # TODO finish this!
                    #    call("./drop_box.sh " + str(closest) + " " + str(-26.25) + " box" + str(box_serial_number), stdout=FNULL)
                    system("rosrun gazebo_ros spawn_model -file /home/user/catkin_ws/src/demo_2/models/box.urdf -urdf -x " + str(closest) + " -y " + str(-26.25) + " -model box" + str(box_serial_number))
                    box_serial_number += 1
                    dropped_boxes.append((closest, -26.25))
    except IndexError:
        # This is a workaround because the box_control node runs and gets here before the model has finished spawning
        pass
        

rospy.init_node('box_control_node')
sub = rospy.Subscriber('/gazebo/model_states', ModelStates, check)
m = ModelStates()
rospy.spin()
