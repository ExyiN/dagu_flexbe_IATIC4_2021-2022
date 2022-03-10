#!/usr/bin/env python
import rospy

from flexbe_core import EventState, Logger


class DaguSpeed50State(EventState):
    '''
    Etat du Dagu quand il détecte un panneau vitesse.
    Arrêt pendant 3 secondes, puis retour à l'état initial.

    ># speed         int        Vitesse à changer

    <= restarting			    Le Dagu change de vitesse.

    '''

    def __init__(self):
        super(DaguSpeed50State, self).__init__(outcomes = ['restarting'], input_keys = ['speed'])

    #def execute(self, userdata):
        #Quelque chose du genre Dagu.speed = userdata.speed

    def on_enter(self, userdata):
        Logger.loginfo('Changement de la vitesse du véhicule...')

    def on_exit(self, userdata):
        Logger.loginfo('Vitesse modifiée...')