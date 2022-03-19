# -*- coding: utf-8 -*-
#!/usr/bin/env python

import rospy

from flexbe_core import EventState, Logger


class DaguPriorityState(EventState):
    '''
    Etat du Dagu quand il détecte un panneau "Priorité".
    Comportement à définir.

    <= out			    A définir

    '''
    
    def __init__(self):
        super(DaguPriorityState, self).__init__(outcomes = ['out'])

    def execute(self, userdata):
        Logger.loginfo('Le Dagu a la priorité !')
        return 'out'

    def on_enter(self, userdata):
        Logger.loginfo('Panneau "Priorité" détecté.')