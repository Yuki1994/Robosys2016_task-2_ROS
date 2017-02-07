#!/usr/bin/env python
import rospy
from std_msgs.msg import Int32

def cb(message):
    set_servo(message.data)

def set_servo(angle):
    try:
        with open('/dev/pwmservo0', 'w') as f:
            print >> f, angle
    except:
        rospy.logerr("cannot open servo ")

if __name__ == '__main__': 
    rospy.init_node('servo')
    sub = rospy.Subscriber('count', Int32, cb) 
    rospy.spin()
