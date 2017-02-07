#!/usr/bin/env python
import rospy
from std_msgs.msg import Int32

if __name__ == '__main__': 
    rospy.init_node('count')
    pub = rospy.Publisher('count', Int32, queue_size=1)
    rate = rospy.Rate(1)
    n = -70
    i = 10
    while not rospy.is_shutdown():
        if n >= 70:
            i = -10
        if n <= -70:
            i = 10
        n += i
        pub.publish(n)
        rate.sleep()
