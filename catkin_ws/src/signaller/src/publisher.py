#!/usr/bin/env python3

import rospy
from std_msgs.msg import Bool


if __name__ == '__main__':
  on = False

  rospy.init_node('signaller')

  pub = rospy.Publisher('turn_on', Bool, queue_size=10)
  rate = rospy.Rate(10)

  while not rospy.is_shutdown():
      turn_on_msg = Bool()
      turn_on_msg.data = on
      on = not on

      pub.publish(turn_on_msg)
      rate.sleep()




