# -*- coding: utf-8 -*-
#!/usr/bin/env python
# Auteur : Jacques TEA (IATIC-4)

import rospy
import sys
from flexbe_core import EventState, Logger
sys.path.insert(1, '/home/isty/catkin_ws/src/dagu_behaviors/scripts')
import talker

class DaguSpeed50State(EventState):
    '''
    Etat du Dagu quand il détecte un panneau vitesse.
    Envoi d'une chaîne de caractères dans un Publisher pour exécuter le script lié à cette chaîne.
        - Changement de vitesse

    <= done			    On revient à l'état initial.

    '''

    def __init__(self):
        super(DaguSpeed50State, self).__init__(outcomes = ['done'])

    def execute(self, userdata):
        try:
            talker.talker("Panel50Detected")
            return 'done'
        except rospy.ROSInterruptException:
            pass