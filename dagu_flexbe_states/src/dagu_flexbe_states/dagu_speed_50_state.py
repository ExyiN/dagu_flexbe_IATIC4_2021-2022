#!/usr/bin/env python
import rospy

from flexbe_core import EventState, Logger


class DaguSpeed50State(EventState):
    '''
    Etat du Dagu quand il détecte un panneau vitesse.

    <= changing			    Le Dagu change de vitesse.

    '''

    def __init__(self):
        super(DaguSpeed50State, self).__init__(outcomes = ['changing'])

    def execute(self, userdata):
        Logger.loginfo('Return changing')
        return 'changing'

    def on_enter(self, userdata):
        Logger.loginfo('Changement de la vitesse du véhicule...')

    def on_exit(self, userdata):
        Logger.loginfo('Vitesse modifiée...')