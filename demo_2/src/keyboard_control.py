#!/usr/bin/env python

import curses
import traceback
import rospy
from std_msgs.msg import String

try:
    rospy.init_node('keyboard_control_node')
    robo_pub = rospy.Publisher('/key2ddr', String, queue_size=2)
    
    # -- Initialize --
    stdscr = curses.initscr()   # initialize curses screen
    curses.noecho()             # turn off auto echoing of keypress on to screen
    curses.cbreak()             # enter break mode where pressing Enter key
                                #  after keystroke is not required for it to register
    stdscr.keypad(1)            # enable special Key values such as curses.KEY_LEFT etc

    rospy.sleep(4.0)    # gives the ddr_control time to spawn the model before the GUI comes to life

    # -- Perform an action with Screen --
    stdscr.border(0)
    stdscr.addstr(5, 5, 'Control the robot with the keypad arrows or WASD.', curses.A_NORMAL)
    stdscr.addstr(6, 5, 'Press q to close this screen and the CNTL+C to exit.', curses.A_NORMAL)

    effort = 1.0
    t = 0.25

    while rospy.is_shutdown() is False:
        # stay in this loop till the user presses 'q'
        ch = stdscr.getch()
        if ch == ord('q'):
            # exit
            break
        elif ch == curses.KEY_LEFT or ch == ord('a') or ch == ord('A'):
            # turn left
            robo_msg = String()
            robo_msg.data = "port ahead " + str(effort) + " " + str(t)
            robo_pub.publish(robo_msg)
        elif ch == curses.KEY_UP or ch == ord('w') or ch == ord('W'):
            # speed up
            robo_msg = String()
            robo_msg.data = "all ahead " + str(effort) + " " + str(t)
            robo_pub.publish(robo_msg)
        elif ch == curses.KEY_DOWN or ch == ord('s') or ch == ord('S'):
            # slow down
            robo_msg = String()
            robo_msg.data = "all back " + str(effort) + " " + str(t)
            robo_pub.publish(robo_msg)
        elif ch == curses.KEY_RIGHT or ch == ord('d') or ch == ord('D'):
            # turn right
            robo_msg = String()
            robo_msg.data = "starboard ahead " + str(effort) + " " + str(t)
            robo_pub.publish(robo_msg)
    # -- End of user code --
except KeyboardInterrupt:
    pass
except:
    traceback.print_exc()     # print trace back log of the error
finally:
    # --- Cleanup on exit ---
    stdscr.keypad(0)
    curses.echo()
    curses.nocbreak()
    curses.endwin()
    rospy.signal_shutdown("Goodbye.")
