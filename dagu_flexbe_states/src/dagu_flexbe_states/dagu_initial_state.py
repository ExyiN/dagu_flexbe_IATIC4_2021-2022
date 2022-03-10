#!/usr/bin/env python
import rospy

from flexbe_core import EventState, Logger
import random
import time

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
        super(DaguInitialState, self).__init__(outcomes = ['default', 'stop', 'speed_50', 'yieldSign', 'forbidden', 'danger', 'failed'])
        self._detectedID = detectedID
        self._timeToWait = rospy.Duration(5)

        self.buffer = []

        for i in range(6):
            sign = SignInfo()
            self.buffer.append(sign)

    def execute(self, userdata):
        time.sleep(1)
        self._detectedID = random.randint(0, 5)

        if self._detectedID == 0:
            Logger.loginfo('DEFAULT')
            return 'default'

        if(self.buffer[self._detectedID].getTimer() != 0):
            if(rospy.Time.now() - self.buffer[self._detectedID].getTimer() >= self._timeToWait):
                self.buffer[self._detectedID].resetTimes()

        self.buffer[self._detectedID].setTimer()
        self.buffer[self._detectedID].incTimes()
        Logger.loginfo("Detected :" + str(self._detectedID) + " - " + str(self.buffer[self._detectedID].getTimes()))

        if self.buffer[self._detectedID].getTimes() >= 5:
            self.buffer[self._detectedID].resetTimes()
        
            if self._detectedID == 1:
                Logger.loginfo('STOP')
                return 'stop'
            elif self._detectedID == 2:
                Logger.loginfo('SPEED_50')
                return 'speed_50'
            elif self._detectedID == 3:
                Logger.loginfo('YIELD')
                return 'yieldSign'
            elif self._detectedID == 4:
                Logger.loginfo('FORBIDDEN')
                return 'forbidden'
            elif self._detectedID == 5:
                Logger.loginfo('DANGER')
                return 'danger'
            else:
                Logger.loginfo('ERROR')
                return 'failed'

class SignInfo():
    def __init__(self):
        self.timesDetected = 0
        self.timer = 0

    def getTimes(self):
        return self.timesDetected

    def incTimes(self):
        self.timesDetected += 1

    def resetTimes(self):
        self.timesDetected = 0

    def getTimer(self):
        return self.timer

    def setTimer(self):
        self.timer = rospy.Time.now()