from robot_control_class import RobotControl

rc = RobotControl()

d = rc.get_laser_full()

#The real way
max_val = max(rc.get_laser_full())

print("The max() result is", max_val)

#The student way
max_val = 0

for value in d:
    if value > max_val:
        max_val = value

print ("The for loop result is", max_val)
