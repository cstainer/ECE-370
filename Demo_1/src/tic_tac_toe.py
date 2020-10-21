#! /usr/bin/env python

import rospy
from tic_tac_toe_board import board_setup
from turtle_ttt import Turtle
from geometry_msgs.msg import Twist
from std_msgs.msg import String
import os

def win_checker(player=None):
    global board
    global winner

    # only 8 winning combos, so easy enough to just brute force it
    # horizontal wins
    if board[0][0] == player and board[0][1] == player and board[0][2] == player:
        winner = player
    elif board[1][0] == player and board[1][1] == player and board[1][2] == player:
        winner = player
    elif board[2][0] == player and board[2][1] == player and board [2][2] == player:
        winner = player
    # vertical wins
    elif board[0][0] == player and board[1][0] == player and board[2][0] == player:
        winner = player
    elif board[0][1] == player and board[1][1] == player and board[2][1] == player:
        winner = player
    elif board[0][2] == player and board[1][2] == player and board[2][2] == player:
        winner = player
    # diagonal wins
    elif board[0][0] == player and board[1][1] == player and board[2][2] == player:
        winner = player
    elif board[0][2] == player and board[1][1] == player and board[2][0] == player:
        winner = player

def turn_right():
    global ttt_cmd
    cmd = Twist()
    cmd.angular.z = -90
    cmd.linear.x = -0.2     # x=-0.2 is stop
    
    # have to do this because sometimes a single publish doesn't go through
    while True:
        connections = ttt_cmd.get_num_connections()
        if connections > 0:
            ttt_cmd.publish(cmd)
            break    
    
    rospy.wait_for_message("ttt_ret", String)

def turn_left():
    global ttt_cmd
    cmd = Twist()
    cmd.angular.z = 90
    cmd.linear.x = -0.2     # x=-0.2 is stop
    
    # have to do this because sometimes a single publish doesn't go through
    while True:
        connections = ttt_cmd.get_num_connections()
        if connections > 0:
            ttt_cmd.publish(cmd)
            break

    rospy.wait_for_message("ttt_ret", String)

# x=-0.1 is push
# x=-0.2 is stop
def fwd(x=0.0):
    global ttt_cmd
    cmd = Twist()
    cmd.linear.x = x

    # have to do this because sometimes a single publish doesn't go through
    while True:
        connections = ttt_cmd.get_num_connections()
        if connections > 0:
            ttt_cmd.publish(cmd)
            break

    rospy.wait_for_message("ttt_ret", String)

# moves turtle to his starting position
def turtle_init():
    turn_left()
    turn_left()

# q(), w(), e(), a(), s(), d(), z(), x(), and c() all do the same thing
# They move turtle to their respective box, push the game piece into the box
# and return turtle to his home position/orientation
def q():
    # TODO map out turns and distances to q box, push, return home
    pass

def w():
    # TODO map out turns and distances to w box, push, return home
    pass

def e():
    # TODO map out turns and distances to e box, push, return home
    pass

def a():
    # TODO map out turns and distances to a box, push, return home
    pass

def s():
    # TODO map out turns and distances to s box, push, return home
    pass

def d():
    # TODO map out turns and distances to d box, push, return home
    pass

def z():
    # TODO map out turns and distances to z box, push, return home
    pass

def x():
    fwd(-0.1)       # push block in
    turn_left()     # turn around
    turn_left()
    fwd(0.5)        # go home
    turn_left()
    turn_left()
                    # home

def c():
    # TODO map out turns and distances to c box, push, return home
    pass


# Keyboard callback
def callback(msg=None):
    # parse the incoming message
    position = msg.data[:1]
    player = msg.data[1:]
    
    # local variables (and access to necessary globals) 
    response = String()
    global board
    global ttt_pub

    # decode the message position component
    if position == "q":
        # check if the position has already been claimed
        if board[0][0] == " ":    
        # if no, spawn the piece and have turtle push it in the box
            os.system("rosrun gazebo_ros spawn_model -file /home/user/catkin_ws/src/tic_tac_toe/src/" + player.lower() + "_piece.urdf -urdf -x -5.1 -y -2 -model q")
            q()
            board[0][0] = player
        else:
        # else publish fail response
            response.data = "failure"
            ttt_pub.publish(response)
    elif position == "w":
        # check if the position has already been claimed
        if board[0][1] == " ":    
        # if no, spawn the piece and have turtle push it in the box
            os.system("rosrun gazebo_ros spawn_model -file /home/user/catkin_ws/src/tic_tac_toe/src/" + player.lower() + "_piece.urdf -urdf -x -5.1 -y 0 -model w")
            w()
            board[0][1] = player
        else:
        # else publish fail response
            response.data = "failure"
            ttt_pub.publish(response)
    elif position == "e":
        # check if the position has already been claimed
        if board[0][2] == " ":    
        # if no, spawn the piece and have turtle push it in the box
            os.system("rosrun gazebo_ros spawn_model -file /home/user/catkin_ws/src/tic_tac_toe/src/" + player.lower() + "_piece.urdf -urdf -x -5.1 -y 2 -model e")
            e()
            board[0][2] = player
        else:
        # else publish fail response
            response.data = "failure"
            ttt_pub.publish(response)
    elif position == "a":
        # check if the position has already been claimed
        if board[1][0] == " ":    
        # if no, spawn the piece and have turtle push it in the box
            os.system("rosrun gazebo_ros spawn_model -file /home/user/catkin_ws/src/tic_tac_toe/src/" + player.lower() + "_piece.urdf -urdf -x -2.85 -y -2 -model a")
            a()
            board[1][0] = player
        else:
        # else publish fail response
            response.data = "failure"
            ttt_pub.publish(response)
    elif position == "s":
        # check if the position has already been claimed
        if board[1][1] == " ":    
        # if no, spawn the piece and have turtle push it in the box
            os.system("rosrun gazebo_ros spawn_model -file /home/user/catkin_ws/src/tic_tac_toe/src/" + player.lower() + "_piece.urdf -urdf -x -2.85 -y 0 -model s")
            s()
            board[1][1] = player
        else:
        # else publish fail response
            response.data = "failure"
            ttt_pub.publish(response)
    elif position == "d":
        # check if the position has already been claimed
        if board[1][2] == " ":    
        # if no, spawn the piece and have turtle push it in the box
            os.system("rosrun gazebo_ros spawn_model -file /home/user/catkin_ws/src/tic_tac_toe/src/" + player.lower() + "_piece.urdf -urdf -x -2.85 -y 2 -model d")
            d()
            board[1][2] = player
        else:
        # else publish fail response
            response.data = "failure"
            ttt_pub.publish(response)
    elif position == "z":
        # check if the position has already been claimed
        if board[2][0] == " ":    
        # if no, spawn the piece and have turtle push it in the box
            os.system("rosrun gazebo_ros spawn_model -file /home/user/catkin_ws/src/tic_tac_toe/src/" + player.lower() + "_piece.urdf -urdf -x -0.6 -y -2 -model z")
            z()
            board[2][0] = player
        else:
        # else publish fail response
            response.data = "failure"
            ttt_pub.publish(response)
    elif position == "x":
        # check if the position has already been claimed
        if board[2][1] == " ":    
        # if no, spawn the piece and have turtle push it in the box
            os.system("rosrun gazebo_ros spawn_model -file /home/user/catkin_ws/src/tic_tac_toe/src/" + player.lower() + "_piece.urdf -urdf -x -0.6 -y 0 -model x")
            x()
            board[2][1] = player
        else:
        # else publish fail response
            response.data = "failure"
            ttt_pub.publish(response)
    elif position == "c":
        # check if the position has already been claimed
        if board[2][2] == " ":    
        # if no, spawn the piece and have turtle push it in the box
            os.system("rosrun gazebo_ros spawn_model -file /home/user/catkin_ws/src/tic_tac_toe/src/" + player.lower() + "_piece.urdf -urdf -x -0.6 -y 2 -model c")
            c()
            board[2][2] = player
        else:
        # else publish fail response
            response.data = "failure"
            ttt_pub.publish(response)
    else:
    # else publish fail response
        response.data = "failure"
        ttt_pub.publish(response)
    
    # check for the win
    win_checker(player)

    # if win publish win response
    if winner != None:
        response.data = "win"
        ttt_pub.publish(response)
    # else publish success response
    else:
        response.data = "success"
        ttt_pub.publish(response)


rospy.init_node("ttt")      # generate the node for ros
board_setup()               # generate the board

# create the publishers for ttt_cmd (talking to turtle) and
# ttt_ctl (talking to keyboard_input)
ttt_cmd = rospy.Publisher("/ttt_cmd", Twist, queue_size=1)
ttt_pub = rospy.Publisher("/ttt_ctl", String, queue_size=1)

turtle_init()               # set turtle in his initial orientation/position

# gameplay variables
#          Q    W    E      A    S    D      Z    X    C
board = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]
winner = None

# create the subscriber to keyboard_input's output
key_sub = rospy.Subscriber("/keyboard", String, callback)

# keep game going until it's done
rospy.spin()
