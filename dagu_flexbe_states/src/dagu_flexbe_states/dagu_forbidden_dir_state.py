# -*- coding: utf-8 -*-
#!/usr/bin/env python

import rospy
import sys
from flexbe_core import EventState, Logger
sys.path.insert(1, '/home/isty/catkin_ws/src/dagu_behaviors/scripts')
import talker


class DaguForbiddenDirState(EventState):
    '''
    Etat du Dagu quand il détecte un panneau sens interdit.
    Envoi d'une chaîne de caractères dans un Publisher pour exécuter le script lié à cette chaîne.
        - Arrêt du véhicule
        - Désactivation de l'autopilote

    <= done		    On revient à l'état initial.

    '''

    def __init__(self):
        super(DaguForbiddenDirState, self).__init__(outcomes = ['done'])
        
    def execute(self, userdata):
        try:
            talker.talker("Stop")
            talker.talker("autoPilotOFFPressed")
            return 'done'
        except rospy.ROSInterruptException:
            pass
