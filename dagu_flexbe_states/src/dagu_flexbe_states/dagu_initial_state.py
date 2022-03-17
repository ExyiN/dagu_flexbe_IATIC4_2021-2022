# -*- coding: utf-8 -*-
#!/usr/bin/env python

import rospy
import sys

from flexbe_core import EventState, Logger
sys.path.insert(1, '/home/isty/Documents/Dagu/YOLOv5-Lite')
import pipe

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

    def __init__(self):
        super(DaguInitialState, self).__init__(outcomes = ['default', 'stop', 'speed_50', 'yieldSign', 'forbidden', 'danger', 'failed'])
        self._detectedID = 0
        self._timeToWait = rospy.Duration(5)
        self._path_fifo = pipe.path

        self._buffer = []
        self._detectedTab= []

        for i in range(6):
            sign = SignInfo()
            self._buffer.append(sign)
            self._detectedTab.append(0)

    def on_enter(self, userdata):
        self.resetDTab()

    def execute(self, userdata):
        Logger.loginfo("Avant open")
        with open(self._path_fifo, 'r') as fifo:
            self._detectedID = pipe.listener(fifo)
            Logger.loginfo("Somme : " + str(self._detectedID))

        self.decompose()

        for i in range(1, 6):
            if self._detectedTab[i] == 1:
                if(self._buffer[i].getTimer() != 0):
                    if(rospy.Time.now() - self._buffer[i].getTimer() >= self._timeToWait):
                        self._buffer[i].resetTimes()

                self._buffer[i].setTimer()
                self._buffer[i].incTimes()
                Logger.loginfo("Detected :" + str(i) + " - " + str(self._buffer[i].getTimes()))

                if self._buffer[i].getTimes() >= 5:
                    self._buffer[i].resetTimes()
                
                    if i == 1:
                        return 'speed_50'
                    elif i == 2:
                        return 'danger'
                    elif i == 3:
                        return 'yieldSign'
                    elif i == 4:
                        return 'stop'
                    elif i == 5:
                        return 'forbidden'
                    else:
                        return 'failed'

    def resetDTab(self):
        for i in range(6):
            self._detectedTab[i] = 0

    def decompose(self):
        for i in range(5, 0, -1):
            power = pow(2, i)
            if self._detectedID >= power:
                self._detectedID -= power
                self._detectedTab[i] = 1
            

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