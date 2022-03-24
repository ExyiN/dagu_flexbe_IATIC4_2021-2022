# -*- coding: utf-8 -*-
#!/usr/bin/env python

import rospy
import sys
from flexbe_core import EventState, Logger
sys.path.insert(1, '/home/isty/catkin_ws/src/dagu_behaviors/scripts')
import talker


class DaguPriorityState(EventState):
    '''
    Etat du Dagu quand il détecte un panneau "Priorité".
    Envoi d'une chaîne de caractères dans un Publisher pour exécuter le script lié à cette chaîne.
        -

    <= done			    On revient à l'état initial.

    '''
    
    def __init__(self):
        super(DaguPriorityState, self).__init__(outcomes = ['done'])

    def execute(self, userdata):
        try:
            talker.talker("PriorityDetected")
            return 'done'
        except rospy.ROSInterruptException:
            pass
