#!/usr/bin/env python3

import rospy
from std_msgs.msg import Bool
from sensor_msgs.msg import LaserScan
import math

min_angle_range_to_register = math.radians(10)
angle_min = math.radians(-30)
angle_max = math.radians(30)
min_distance_to_register = .3 #m


def convert_polar_dist_to_vertical_dist(dist, angle):
  return dist * math.sin(angle)

def check_data_forward(data, start, i):
  end = start + i

  while end < len(data):
    curr = end - i
    found_obstacle = True
    while curr < end:
      if data[curr] > min_distance_to_register:
        found_obstacle = False
        break
      curr += 1
    if found_obstacle:
      return True

    end += 1

  return False

def interpret_data(data):
  increment = data.angle_increment
  step_count = int(min_angle_range_to_register / increment)

  start = int(angle_min / increment)
  end = int(angle_max / increment)

  ranges = data.ranges[start:] + data.ranges[:end]

  # ranges = data.ranges[start:end]

  rospy.loginfo("Increment: " + str(increment))
  rospy.loginfo("Step count: " + str(step_count))
  rospy.loginfo("Start: " + str(start))
  rospy.loginfo("End: " + str(end))
  rospy.loginfo("Original len: " + str(len(data.ranges)))
  rospy.loginfo("New len: " + str(len(ranges)))

  if check_data_forward(ranges, 0, step_count):
    rospy.loginfo("DETECTED")
    on.data = True
    pub.publish(on)
  else:
    on.data = False
    pub.publish(on)

if __name__ == '__main__':
  on = Bool()
  on.data = False

  rospy.init_node('signaller')

  sub = rospy.Subscriber('scan', LaserScan, interpret_data)
  pub = rospy.Publisher('turn_on', Bool, queue_size=10)

  rospy.spin()



