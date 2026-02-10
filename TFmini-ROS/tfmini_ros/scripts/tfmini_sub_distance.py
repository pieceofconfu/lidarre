#!/usr/bin/env python3
import rospy
from sensor_msgs.msg import Range

def listener():
    rospy.init_node('range_listener', anonymous=True)

    previous_distance = None
    rate = rospy.Rate(1000)  # 10 Hz = 0.1 saniyede bir

    while not rospy.is_shutdown():
        try:
            msg = rospy.wait_for_message('/tfmini_ros_node/TFmini', Range, timeout=1.0)
            current_distance = msg.range
            print(current_distance)
            rate.sleep()
        except rospy.ROSException:
            rospy.logwarn("Veri alınamadı (timeout).")

if __name__ == '__main__':
    listener()

