#!/usr/bin/env python
import rospy

from flexbe_core import EventState, Logger


class DaguInitialState(EventState):
    '''
    Etat initial du Dagu.
    Il avance.

    -- defaultID            int     id par défaut (aucun élément détecté).
    -- detectedID           int     id de l'élément détecté.

    ># detectedIDInput      int     id de l'élément détecté.
    #> linkedState          int     Etat lié à l'élément détecté.

    <= changingState 			    Dagu has detected something.
    <= notChanging                  Dagu stay in this state.

    '''

    def __init__(self, defaultID, detectedID):
        # Declare outcomes, input_keys, and output_keys by calling the super constructor with the corresponding arguments.
        super(DaguInitialState, self).__init__(outcomes = ['changingState', 'notChanging'])
        self._defaultID = defaultID
        self._detectedID = detectedID

    def execute(self, userdata):
        # This method is called periodically while the state is active.
        # Main purpose is to check state conditions and trigger a corresponding outcome.
        # If no outcome is returned, the state will stay active.
        if self._detectedID > self._defaultID:
            return 'changingState'
        else:
            return 'notChanging'
