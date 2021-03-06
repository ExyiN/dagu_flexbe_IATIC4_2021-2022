# -*- coding: utf-8 -*-
#!/usr/bin/env python
# Auteur : Jacques TEA (IATIC-4)

import rospy
import sys
from flexbe_core import EventState, Logger
sys.path.insert(1, '/home/isty/catkin_ws/src/dagu_behaviors/scripts')
import talker

class DaguYieldState(EventState):
    '''
    Etat du Dagu quand il détecte un panneau "Cédez le passage".
    Envoi d'une chaîne de caractères dans un Publisher pour exécuter le script lié à cette chaîne.
        - Redémarrage si aucun Dagu n'est détecté

    <= done			    On revient à l'état initial.

    '''
    
    def __init__(self):
        super(DaguYieldState, self).__init__(outcomes = ['done'])

    def execute(self, userdata):
        try:
            talker.talker("CedezPassageDetected")
            return 'done'
        except rospy.ROSInterruptException:
            pass
