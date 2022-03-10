#!/usr/bin/env python
import rospy

from flexbe_core import EventState, Logger


class DaguStopState(EventState):
    '''
    Etat du Dagu quand il détecte un panneau stop.
    Arrêt pendant 3 secondes, puis retour à l'état initial.

    <= restarting			    Le Dagu redémarre.

    '''

    def __init__(self):
        super(DaguStopState, self).__init__(outcomes = ['restarting'])
        self._timeToWait = rospy.Duration(3)

    def execute(self, userdata):
        

    def on_enter(self, userdata):
        Logger.loginfo('Arrêt du véhicule...')

    def on_exit(self, userdata):
        Logger.loginfo('Véhicule arrêté...')