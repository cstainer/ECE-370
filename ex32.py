from robot_control_class import RobotControl

rc = RobotControl()

rc.stop_robot()
a = rc.get_laser(360)

if 1 < a:
    rc.move_straight()

while 1 < a:
    print("The distance measured is:", a)
    a = rc.get_laser(360)

rc.stop_robot()
print("The distance measured is:", a)
