from robot_control_class import RobotControl 
import time

rc = RobotControl()

def move_for_time(t):
    rc.stop_robot()
    rc.move_straight()
    time.sleep(5)
    rc.stop_robot()

def get_multiple_ranges(a, b, c):
    return (rc.get_laser_summit(a), rc.get_laser_summit(b), rc.get_laser_summit(c))

rc.stop_robot()
move_for_time(5)
print(get_multiple_ranges(200, 400, 600)
