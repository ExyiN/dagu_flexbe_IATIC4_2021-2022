# -*- coding: utf-8 -*-
#!/usr/bin/env python

import rospy
from std_msgs.msg import String

def talker(message):
    pub = rospy.Publisher('flexbePub', String, queue_size=10)
    rospy.loginfo(message)
    pub.publish(message)

