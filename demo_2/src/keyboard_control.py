#!/usr/bin/env python

# https://pythonpedia.com/en/tutorial/5851/basic-curses-with-python curses stuff started with this code
import curses
import traceback
import rospy
from std_msgs.msg import String

try:
    rospy.init_node('keyboard_control_node')
    robo_pub = rospy.Publisher('/key2ddr', String, queue_size=2)
    robo_msg = String()
    box_pub = rospy.Publisher('/key2box', String, queue_size=2)
    box_msg = String()
    #ddrc = ddr_control.DD_Robot_Control(model="ddr_0")
    
    # -- Initialize --
    stdscr = curses.initscr()   # initialize curses screen
    curses.noecho()             # turn off auto echoing of keypress on to screen
    curses.cbreak()             # enter break mode where pressing Enter key
                                #  after keystroke is not required for it to register
    stdscr.keypad(1)            # enable special Key values such as curses.KEY_LEFT etc
    
    # -- Perform an action with Screen --
    stdscr.border(0)
    stdscr.addstr(5, 5, 'Control the robot with the keypad arrows or WASD', curses.A_NORMAL)
    stdscr.addstr(6, 5, 'Press q to close this screen', curses.A_NORMAL)

    tock = rospy.Time.now()
    effort = 0.5

    while rospy.is_shutdown() is False:
        # stay in this loop till the user presses 'q'
        ch = stdscr.getch()
        if ch == ord('q'):
            # exit
            break
        elif ch == curses.KEY_LEFT or ch == ord('a') or ch == ord('A'):
            # turn left
            tick = rospy.Time.now()
            #ddrc.setEffort(wheel="starboard", effort=effort_s, direction="ahead", duration=(tick.secs-tock.secs))
        elif ch == curses.KEY_UP or ch == ord('w') or ch == ord('W'):
            # speed up
            tick = rospy.Time.now()
            robo_msg.data = "all ahead " + str(effort) + " " + str(tick-tock)
            robo_pub.publish(robo_msg)
        elif ch == curses.KEY_DOWN or ch == ord('s') or ch == ord('S'):
            # slow down
            pass
        elif ch == curses.key_RIGHT or ch == ord('d') or ch == ord('D'):
            # turn right
            tick = rospy.Time.now()
            #ddrc.setEffort(wheel="port", effort=effort_p, direction="ahead", duration=(tick.secs-tock.secs))
        
        tock = rospy.Time.now()

    # -- End of user code --

except:
    traceback.print_exc()     # print trace back log of the error
    
finally:
    # --- Cleanup on exit ---
    stdscr.keypad(0)
    curses.echo()
    curses.nocbreak()
    curses.endwin()

