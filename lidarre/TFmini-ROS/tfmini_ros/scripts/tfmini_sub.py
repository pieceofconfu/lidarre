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

            if previous_distance is not None:
                # rospy.loginfo(current_distance)
                fark = abs(current_distance - previous_distance)
                if fark > 0.15:
                    rospy.loginfo("Balon vuruldu! Mesafe farkı: %.2f m" % fark)

            previous_distance = current_distance
            rate.sleep()
        except rospy.ROSException:
            rospy.logwarn("Veri alınamadı (timeout).")

if __name__ == '__main__':
    listener()

