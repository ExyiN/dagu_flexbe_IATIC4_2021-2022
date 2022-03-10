#!/usr/bin/env python
import rospy

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
<<<<<<< HEAD
        
    def execute(self, userdata):
        return 'idle'
=======
        #Trouver comment arrêter le Dagu
        
>>>>>>> c6a525feb1e50a0197bafc2a8961f85c36f585c1
