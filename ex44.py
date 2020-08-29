from robot_control_class import RobotControl 

rc = RobotControl()

rc.stop_robot()
print(rc.move_straight_time("forward", 0.5, 1))
print(rc.turn("counter-clockwise", 2, 1))
print(rc.move_straight_time("forward", 1, 2.3))
print(rc.turn("counter-clockwise", 2, 1))
print(rc.move_straight_time("forward", 2, 2))
