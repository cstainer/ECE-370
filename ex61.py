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
rc.stop_robot()
print("Initial position")

while(1):
    p = pos_check()
    
    if (p[1] > 6):
        print("Go straight 6")
        rc.move_straight_time("forward", 1, 6)
    else:
        print("Go straight", p[1] - 0.75)
        rc.move_straight_time("forward", 1, p[1] - 0.75)
    
    p = pos_check()

    if (p[2] == p[0]):
        break
    elif (p[2] > p[0]):
        print("Turn right")
        rc.rotate(-80)
    else: #if (p[2] < p[0])
        print("Turn left")
        rc.rotate(90)
