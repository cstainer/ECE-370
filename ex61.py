from robot_control_class import RobotControl 

rc = RobotControl()

def pos_check(debug = False):
    d = rc.get_laser_full()
    
    if (debug):
        print("Left", d[719])
        print("Forward", d[360])
        print("Right", d[0])
        print()
    
    return [d[719], d[360], d[0]]

#Begin
debug = False
rc.stop_robot()
print("Initial position")
p = pos_check(debug)

rc.move_straight_time("forward", 1, p[1] - 0.75)
print("First corner")
p = pos_check(debug)

rc.rotate(-81)
print("First turn")
p = pos_check(debug)
rc.move_straight_time("forward", 1, p[1] - 0.75)
print("Second corner")
p = pos_check(debug)

rc.rotate(-81)
print("Second turn")
p = pos_check(debug)
rc.move_straight_time("forward", 1, p[1] - 0.75)
print("Third corner")
p = pos_check(debug)

rc.rotate(90)
print("Third turn")
p = pos_check(debug)
rc.move_straight_time("forward", 1, 5)
print("I'm out, bitches")
p = pos_check(debug)
print("[drops mic on stage]")
