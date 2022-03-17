# -*- coding: utf-8 -*-
#!/usr/bin/env python

import rospy
import dagu_initial_state
from flexbe_core import EventState, Logger


class DaguForbiddenDirState(EventState):
    '''
    Etat du Dagu quand il détecte un panneau sens interdit.
    Arrêt de la machine tant qu'il n'y a pas d'intervention humaine.

    <= stop			    Le Dagu s'arrête et ne redémarre pas.

    '''

    def __init__(self):
        super(DaguForbiddenDirState, self).__init__(outcomes = ['idle'])

    def on_enter(self, userdata):
        Logger.loginfo('Sens interdit détecté.')
        Logger.loginfo('Arrêt de la machine...')
        
    def execute(self, userdata):
        return 'idle'
    
    def on_exit(self, userdata):
        close(dagu_initial_state.DaguInitialState._fifo)
