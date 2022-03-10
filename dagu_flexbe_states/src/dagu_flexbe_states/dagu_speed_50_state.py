#!/usr/bin/env python
import rospy

from flexbe_core import EventState, Logger


class DaguSpeed50State(EventState):
    '''
    Etat du Dagu quand il détecte un panneau vitesse.
<<<<<<< HEAD

    <= changing			    Le Dagu change de vitesse.
=======
    Arrêt pendant 3 secondes, puis retour à l'état initial.

    ># speed         int        Vitesse à changer

    <= restarting			    Le Dagu change de vitesse.
>>>>>>> c6a525feb1e50a0197bafc2a8961f85c36f585c1

    '''

    def __init__(self):
<<<<<<< HEAD
        super(DaguSpeed50State, self).__init__(outcomes = ['changing'])

    def execute(self, userdata):
        Logger.loginfo('Return changing')
        return 'changing'
=======
        super(DaguSpeed50State, self).__init__(outcomes = ['restarting'], input_keys = ['speed'])

    #def execute(self, userdata):
        #Quelque chose du genre Dagu.speed = userdata.speed
>>>>>>> c6a525feb1e50a0197bafc2a8961f85c36f585c1

    def on_enter(self, userdata):
        Logger.loginfo('Changement de la vitesse du véhicule...')

    def on_exit(self, userdata):
        Logger.loginfo('Vitesse modifiée...')