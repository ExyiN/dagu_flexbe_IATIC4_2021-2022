# -*- coding: utf-8 -*-
#!/usr/bin/env python
# Auteur : Jacques TEA (IATIC-4)

import rospy
import sys
from flexbe_core import EventState, Logger
sys.path.insert(1, '/home/isty/catkin_ws/src/dagu_behaviors/scripts')
import talker

class DaguStopState(EventState):
    '''
    Etat du Dagu quand il détecte un panneau stop.
    Envoi d'une chaîne de caractères dans un Publisher pour exécuter le script lié à cette chaîne.
        - Arrêt du véhicule pendant 3 secondes
        - Redémarrage si aucun Dagu n'est détecté

    <= done			    On revient à l'état initial.

    '''

    def __init__(self):
        super(DaguStopState, self).__init__(outcomes = ['done'])
    
    def execute(self, userdata):
        try:
            talker.talker("PanelStopDetected")
            return 'done'
        except rospy.ROSInterruptException:
            pass
