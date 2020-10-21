#! /usr/bin/env python

import os

def board_setup():
    
    left_vert_piece = "rosrun gazebo_ros spawn_model -file /home/user/catkin_ws/src/tic_tac_toe/src/ttt_board_v.urdf -urdf -x -3.7 -y -3.75 -model vert_0"
    right_vert_piece = "rosrun gazebo_ros spawn_model -file /home/user/catkin_ws/src/tic_tac_toe/src/ttt_board_v.urdf -urdf -x -3.7 -y 3.75 -model vert_1"

    top_horz_piece = "rosrun gazebo_ros spawn_model -file /home/user/catkin_ws/src/tic_tac_toe/src/ttt_board_h.urdf -urdf -x 0.85 -model horz_0"
    bot_horz_piece = "rosrun gazebo_ros spawn_model -file /home/user/catkin_ws/src/tic_tac_toe/src/ttt_board_h.urdf -urdf -x -8.2 -model horz_1"

    q_l_side = "rosrun gazebo_ros spawn_model -file /home/user/catkin_ws/src/tic_tac_toe/src/ttt_bucket_side.urdf -urdf -x -5.7 -y -2.375 -model qls"
    q_bottom_bucket = "rosrun gazebo_ros spawn_model -file /home/user/catkin_ws/src/tic_tac_toe/src/ttt_bucket_bottom.urdf -urdf -x -6.025 -y -2.0 -model bb_q"
    q_r_side = "rosrun gazebo_ros spawn_model -file /home/user/catkin_ws/src/tic_tac_toe/src/ttt_bucket_side.urdf -urdf -x -5.7 -y -1.625 -model qrs"
 
    w_l_side = "rosrun gazebo_ros spawn_model -file /home/user/catkin_ws/src/tic_tac_toe/src/ttt_bucket_side.urdf -urdf -x -5.7 -y -0.375 -model wls"
    w_bottom_bucket = "rosrun gazebo_ros spawn_model -file /home/user/catkin_ws/src/tic_tac_toe/src/ttt_bucket_bottom.urdf -urdf -x -6.025 -y 0.0 -model bb_w"
    w_r_side = "rosrun gazebo_ros spawn_model -file /home/user/catkin_ws/src/tic_tac_toe/src/ttt_bucket_side.urdf -urdf -x -5.7 -y 0.375 -model wrs"

    e_l_side = "rosrun gazebo_ros spawn_model -file /home/user/catkin_ws/src/tic_tac_toe/src/ttt_bucket_side.urdf -urdf -x -5.7 -y 1.675 -model els"
    e_bottom_bucket = "rosrun gazebo_ros spawn_model -file /home/user/catkin_ws/src/tic_tac_toe/src/ttt_bucket_bottom.urdf -urdf -x -6.025 -y 2.0 -model bb_e"
    e_r_side = "rosrun gazebo_ros spawn_model -file /home/user/catkin_ws/src/tic_tac_toe/src/ttt_bucket_side.urdf -urdf -x -5.7 -y 2.375 -model ers"
    
    a_l_side = "rosrun gazebo_ros spawn_model -file /home/user/catkin_ws/src/tic_tac_toe/src/ttt_bucket_side.urdf -urdf -x -3.45 -y -2.375 -model als"
    a_bottom_bucket = "rosrun gazebo_ros spawn_model -file /home/user/catkin_ws/src/tic_tac_toe/src/ttt_bucket_bottom.urdf -urdf -x -3.775 -y -2.0 -model ab_s"
    a_r_side = "rosrun gazebo_ros spawn_model -file /home/user/catkin_ws/src/tic_tac_toe/src/ttt_bucket_side.urdf -urdf -x -3.45 -y -1.625 -model ars"
    
    s_l_side = "rosrun gazebo_ros spawn_model -file /home/user/catkin_ws/src/tic_tac_toe/src/ttt_bucket_side.urdf -urdf -x -3.45 -y -0.375 -model sls"
    s_bottom_bucket = "rosrun gazebo_ros spawn_model -file /home/user/catkin_ws/src/tic_tac_toe/src/ttt_bucket_bottom.urdf -urdf -x -3.775 -y 0.0 -model bb_s"
    s_r_side = "rosrun gazebo_ros spawn_model -file /home/user/catkin_ws/src/tic_tac_toe/src/ttt_bucket_side.urdf -urdf -x -3.45 -y 0.375 -model srs"

    d_l_side = "rosrun gazebo_ros spawn_model -file /home/user/catkin_ws/src/tic_tac_toe/src/ttt_bucket_side.urdf -urdf -x -3.45 -y 1.625 -model dls"
    d_bottom_bucket = "rosrun gazebo_ros spawn_model -file /home/user/catkin_ws/src/tic_tac_toe/src/ttt_bucket_bottom.urdf -urdf -x -3.775 -y 2.0 -model bb_d"
    d_r_side = "rosrun gazebo_ros spawn_model -file /home/user/catkin_ws/src/tic_tac_toe/src/ttt_bucket_side.urdf -urdf -x -3.45 -y 2.375 -model drs"

    z_l_side = "rosrun gazebo_ros spawn_model -file /home/user/catkin_ws/src/tic_tac_toe/src/ttt_bucket_side.urdf -urdf -x -1.2 -y -2.375 -model zls"
    z_bottom_bucket = "rosrun gazebo_ros spawn_model -file /home/user/catkin_ws/src/tic_tac_toe/src/ttt_bucket_bottom.urdf -urdf -x -1.525 -y -2.0 -model bb_z"
    z_r_side = "rosrun gazebo_ros spawn_model -file /home/user/catkin_ws/src/tic_tac_toe/src/ttt_bucket_side.urdf -urdf -x -1.2 -y -1.625 -model zrs"

    x_l_side = "rosrun gazebo_ros spawn_model -file /home/user/catkin_ws/src/tic_tac_toe/src/ttt_bucket_side.urdf -urdf -x -1.2 -y -0.375 -model xls"
    x_bottom_bucket = "rosrun gazebo_ros spawn_model -file /home/user/catkin_ws/src/tic_tac_toe/src/ttt_bucket_bottom.urdf -urdf -x -1.525 -y 0.0 -model bb_x"
    x_r_side = "rosrun gazebo_ros spawn_model -file /home/user/catkin_ws/src/tic_tac_toe/src/ttt_bucket_side.urdf -urdf -x -1.2 -y 0.375 -model xrs"

    c_l_side = "rosrun gazebo_ros spawn_model -file /home/user/catkin_ws/src/tic_tac_toe/src/ttt_bucket_side.urdf -urdf -x -1.2 -y 1.625 -model cls"
    c_bottom_bucket = "rosrun gazebo_ros spawn_model -file /home/user/catkin_ws/src/tic_tac_toe/src/ttt_bucket_bottom.urdf -urdf -x -1.525 -y 2.0 -model bb_c"
    c_r_side = "rosrun gazebo_ros spawn_model -file /home/user/catkin_ws/src/tic_tac_toe/src/ttt_bucket_side.urdf -urdf -x -1.2 -y 2.375 -model crs"

    os.system(top_horz_piece)
    os.system(bot_horz_piece)
    os.system(left_vert_piece)
    os.system(right_vert_piece)

    os.system(q_l_side)
    os.system(q_bottom_bucket)
    os.system(q_r_side)

    os.system(w_l_side)
    os.system(w_bottom_bucket)
    os.system(w_r_side)

    os.system(e_l_side)
    os.system(e_bottom_bucket)
    os.system(e_r_side)

    os.system(a_l_side)
    os.system(a_bottom_bucket)
    os.system(a_r_side)

    os.system(s_l_side)
    os.system(s_bottom_bucket)
    os.system(s_r_side)

    os.system(d_l_side)
    os.system(d_bottom_bucket)
    os.system(d_r_side)

    os.system(z_l_side)
    os.system(z_bottom_bucket)
    os.system(z_r_side)

    os.system(x_l_side)
    os.system(x_bottom_bucket)
    os.system(x_r_side)

    os.system(c_l_side)
    os.system(c_bottom_bucket)
    os.system(c_r_side)


if __name__ == '__main__':
    board_setup()
