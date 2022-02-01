#!/usr/bin/env python
import rospy

from flexbe_core import EventState, Logger


class DaguInitialState(EventState):
    '''
    Etat initial du Dagu.
    Il avance.

    -- detectedID           int     id de l'élément détecté.

    ># detectedIDInput      int     id de l'élément détecté.
    #> linkedState          int     Etat lié à l'élément détecté.

    <= default		                Le Dagu n'a rien détecté.
    <= stop                         Le Dagu a détecté un STOP.
    <= failed                       Erreur.

    '''

    def __init__(self, detectedID):
        super(DaguInitialState, self).__init__(outcomes = ['default', 'stop', 'failed'])
        self._detectedID = detectedID

    def execute(self, userdata):
        if self._detectedID == 1:
            Logger.loginfo('STOP')
            return 'stop'
        elif self._detectedID == 0:
            Logger.loginfo('DEFAULT')
            return 'default'
        else:
            return 'failed'
