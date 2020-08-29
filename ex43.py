from robot_control_class import RobotControl 

rc = RobotControl()

rc.stop_robot()
print(rc.move_straight_time("forward", 0.5, 5))
print(rc.turn("clockwise", 0.5, 7))
