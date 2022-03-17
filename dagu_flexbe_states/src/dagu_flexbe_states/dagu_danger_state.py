#!/usr/bin/env python
import rospy

from flexbe_core import EventState, Logger


class DaguDangerState(EventState):
    '''
    Etat du Dagu quand il détecte un panneau "Danger".
    Comportement à définir.

    <= stop			    Le Dagu s'arrête.

    '''
    
    def __init__(self):
        super(DaguDangerState, self).__init__(outcomes = ['restarting'])
        self._timeToWait = rospy.Duration(3)

    def execute(self, userdata):
        if(rospy.Time.now() - self._startTime >= self._timeToWait):
            return 'restarting'

    def on_enter(self, userdata):
        self._startTime = rospy.Time.now()
        Logger.loginfo('Panneau "Danger" détecté.')
        Logger.loginfo('Arrêt de la machine...')

    def on_exit(self, userdata):
        Logger.loginfo('Redémarrage du véhicule...')