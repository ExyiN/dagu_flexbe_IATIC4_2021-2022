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
        super(DaguInitialState, self).__init__(outcomes = ['restarting'])

    def execute(self, userdata):

    def on_enter(self, userdata):
        self.