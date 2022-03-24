# -*- coding: utf-8 -*-
#!/usr/bin/env python

import rospy
import sys

from flexbe_core import EventState, Logger
sys.path.insert(1, '/home/isty/catkin_ws/src/dagu_behaviors/scripts')
import talker

class DaguStopState(EventState):
    '''
    Etat du Dagu quand il détecte un panneau stop.
    Envoi d'une chaîne de caractères dans un Publisher pour exécuter le script lié à cette chaîne.

    <= restarting			    Le Dagu redémarre.

    '''

    def __init__(self):
        super(DaguStopState, self).__init__(outcomes = ['restarting'])
    
    def execute(self, userdata):
        try:
            talker("stop")
            return 'restarting'
        except rospy.ROSInterruptException:
            pass