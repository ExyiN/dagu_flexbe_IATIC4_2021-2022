#!/usr/bin/env python

import rospy
from std_msgs.msg import String

def talker(message):
    pub = rospy.Publisher('iapub', String, queue_size=10)
    rospy.init_node('talker', anonymous=True)
    rospy.loginfo(message)
    pub.publish(message)

