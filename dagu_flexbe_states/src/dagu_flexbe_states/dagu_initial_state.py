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

    <= default		                Le Dagu n'a rien détecté.
    <= stop                         Le Dagu a détecté un panneau STOP.
    <= speed_50                     Le Dagu a détecté un panneau 50.
    <= yield                        Le Dagu a détecté un panneau "Céder le passage".
    <= forbidden                    Le Dagu a détecté un panneau "Interdit".
    <= danger                       Le Dagu a détecté un panneau "Danger".
    <= failed                       Erreur.

    '''

    def __init__(self):
        super(DaguInitialState, self).__init__(outcomes = ['default', 'stop', 'speed_50', 'yieldSign', 'forbidden', 'danger', 'priority', 'failed'])
        self._detectedID = 0
        self._timeToWait = rospy.Duration(5)
        self._path_fifo = pipe.path

        self._buffer = []

        for i in range(7):
            sign = SignInfo()
            self._buffer.append(sign)

        self._fifo = open(self._path_fifo, 'r')
    def on_enter(self, userdata):
        self.resetDTab()

    def execute(self, userdata):
        Logger.loginfo("Avant open")
        self._detectedID = pipe.listener(self._fifo)
        if self._detectedID == -1:
            return 'default'
        Logger.loginfo("Somme : " + str(self._detectedID))

        self.decompose()

        for i in range(1, 7):
            if(self._buffer[i].getTimer() != 0):
                if(rospy.Time.now() - self._buffer[i].getTimer() >= self._timeToWait):
                    self._buffer[i].resetTimes()

            if self._buffer[i].getTimes() >= 5:
                self._buffer[i].resetTimes()
            
                if i == 1:
                    return 'speed_50'
                elif i == 2:
                    return 'priority'
                elif i == 3:
                    return 'yieldSign'
                elif i == 4:
                    return 'stop'
                elif i == 5:
                    close(self._fifo)
                    return 'forbidden'
                elif i == 6:
                    return 'danger'
                else:
                    close(self._fifo)
                    return 'failed'

    def resetDTab(self):
        for i in range(6):
            self._detectedTab[i] = 0

    def decompose(self):
        for i in range(6, 0, -1):
            power = pow(2, i)
            if self._detectedID >= power:
                self._detectedID -= power
                self._buffer[i].setTimer()
                self._buffer[i].incTimes()
                Logger.loginfo("Detected :" + str(i) + " - " + str(self._buffer[i].getTimes()))
            

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