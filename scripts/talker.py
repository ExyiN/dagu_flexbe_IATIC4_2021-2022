# -*- coding: utf-8 -*-
#!/usr/bin/env python
# Auteur : Jacques TEA (IATIC-4)

import rospy
from std_msgs.msg import String

def talker(message):
    pub = rospy.Publisher('/Resultats_Algo', String, queue_size=1000)
    rospy.loginfo(message)
    pub.publish(message)

