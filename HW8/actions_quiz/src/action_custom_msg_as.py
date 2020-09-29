#! /usr/bin/env python
import rospy
import actionlib
from action_custom_msg.msg import CustomActionMsgAction, CustomActionMsgFeedback, CustomActionMsgResult
from std_msgs.msg import Empty

# goal = TAKEOFF or LAND
# feedback = publishes once per second what action is taking place
# result = nothing

class QuizServer(object):
  
  feedback = CustomActionMsgFeedback()
  result = CustomActionMsgResult()

  def __init__(self):
    self.server = actionlib.SimpleActionServer('action_custom_msg_as', CustomActionMsgAction, self.callback, False)
    self.server.start()
    print('ready')  #debug

  def callback(self, goal):
    
    self.tomsg = Empty()
    self.lmsg = Empty()
    success = False
    r = rospy.Rate(1)
    self.topub = rospy.Publisher('/drone/takeoff', Empty, queue_size=1)
    self.lpub = rospy.Publisher('/drone/land', Empty, queue_size=1)
    print('goal = ', goal.goal) #debug

    # if the goal is to land the drone
    # publish an Empty message to /drone/land
    # publish feedback that the drone is landing at 1 Hz
    if goal.goal == 'LAND':
        print('landing')    #debug
        self.feedback.feedback = 'landing'
        for i in range(0, 4):
            self.lpub.publish(self.lmsg)
            self.server.publish_feedback(self.feedback)
            print('landing feedback published') #debug
            r.sleep()
        success = True
    # else if the goal is for the drone to take off
    # publish an Empty message to /drone/takeoff
    # publish feedback that the drone is taking off at 1 hz
    elif goal.goal == 'TAKEOFF':
        print('taking off') #debug
        self.feedback.feedback = 'taking off'
        for i in range(0, 4):
            self.topub.publish(self.tomsg)
            self.server.publish_feedback(self.feedback)
            print('taking off feedback published') #debug
            r.sleep()
        success = True

    # if we have successfully done the goal
    if success:
        print('success')    #debug
        self.result = Empty()
        self.server.set_succeeded(self.result)
    else:
        print('failed or aborted')  #debug
        self.result = Empty()
        self.server.set_aborted(self.result)


if __name__ == '__main__':
  rospy.init_node('action_custom_msg')
  server = QuizServer()
  rospy.spin()
