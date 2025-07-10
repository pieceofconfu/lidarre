#!/usr/bin/env python3
import rospy
from sensor_msgs.msg import Range

def callback(msg):
    # rospy.loginfo("Mesafe: %.2f m", msg.range)
    distance_from_lidar = msg.range
    rospy.loginfo(distance_from_lidar) 

def listener():
    rospy.init_node('range_listener', anonymous=True)
    rospy.Subscriber('/tfmini_ros_node/TFmini', Range, callback)
    rospy.spin()

if __name__ == '__main__':
    listener()
