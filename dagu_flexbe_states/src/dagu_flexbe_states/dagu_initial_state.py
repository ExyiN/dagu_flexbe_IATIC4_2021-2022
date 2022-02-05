#!/usr/bin/env python
import rospy

from flexbe_core import EventState, Logger
from ....signs_states import *

class DaguInitialState(EventState):
    '''
    Etat initial du Dagu.
    Il avance.

    -- detectedID           int     id de l'élément détecté.

    ># detectedIDInput      int     id de l'élément détecté.
    #> linkedState          int     Etat lié à l'élément détecté.

    <= default		                Le Dagu n'a rien détecté.
    <= stop                         Le Dagu a détecté un panneau STOP.
    <= speed_50                     Le Dagu a détecté un panneau 50.
    <= yield                        Le Dagu a détecté un panneau "Céder le passage".
    <= forbidden                    Le Dagu a détecté un panneau "Interdit".
    <= danger                       Le Dagu a détecté un panneau "Danger".
    <= failed                       Erreur.

    '''

    def __init__(self, detectedID):
        super(DaguInitialState, self).__init__(outcomes = ['default', 'stop', 'failed'])
        self._detectedID = detectedID

    def execute(self, userdata):
        if self._detectedID == signs.GN_DEFAULT:
            Logger.loginfo('DEFAULT')
            return 'default'
        elif self._detectedID == signs.GN_STOP:
            Logger.loginfo('STOP')
            return 'stop'
        elif self._detectedID == signs.GN_SPEED_50:
            Logger.loginfo('SPEED_50')
            return 'speed_50'
        elif self._detectedID == signs.GN_YIELD:
            Logger.loginfo('YIELD')
            return 'yieldSign'
        elif self._detectedID == signs.GN_FORBIDDEN:
            Logger.loginfo('FORBIDDEN')
            return 'forbidden'
        elif self._detectedID == signs.GN_DANGER:
            Logger.loginfo('DANGER')
            return 'danger'
        else:
            return 'failed'
