# -*- coding: utf-8 -*-
#!/usr/bin/env python
# Auteur : Jacques TEA (IATIC-4)

from email import message
import rospy
import sys
import random
from flexbe_core import EventState, Logger
############################################################### Pipe
sys.path.insert(1, '/home/isty/Documents/Dagu/YOLOv5-Lite')
import pipe
###############################################################
sys.path.insert(1, '/home/isty/catkin_ws/src/dagu_behaviors/scripts')
import talker

class DaguInitialState(EventState):
    '''
    Etat initial du Dagu.
    Partie qui gère toutes les redirections vers les autres états.
    Dès qu'un panneau est détecté 5 fois, on passe à l'état correspondant pour exécuter les actions qu'il faut.
    Si le panneau n'est pas détecté pendant 5 secondes, on réinitialise le nombre de fois qu'il a été détecté.

    <= default		                Le Dagu n'a rien détecté.
    <= stop                         Le Dagu a détecté un panneau STOP.
    <= speed_50                     Le Dagu a détecté un panneau 50.
    <= yieldSign                    Le Dagu a détecté un panneau "Céder le passage".
    <= forbidden                    Le Dagu a détecté un panneau "Interdit".
    <= danger                       Le Dagu a détecté un panneau "Danger".
    <= priority                     Le Dagu a détecté un panneau "Priorité".
    <= failed                       Erreur.

    '''

    def __init__(self):
        super(DaguInitialState, self).__init__(outcomes = ['default', 'stop', 'speed_50', 'yieldSign', 'forbidden', 'danger', 'priority', 'failed'])
        self._detectedID = 0
        self._timeToWait = rospy.Duration(4)
        self._timeReset = rospy.Duration(5)
        self._lastTimeExecute = -1
        self._isDaguDetected = False
        # Chemin du fifo
        self._path_fifo = pipe.path

        # Tableau des panneaux
        self._buffer = []

        # Initialisation du tableau
        for i in range(7):
            sign = SignInfo()
            self._buffer.append(sign)

        # Tube pour récupérer les données de l'IA
        self._fifo = open(self._path_fifo, 'r')

        try:
            talker.talker("Start")
        except rospy.ROSInterruptException:
            pass

    def execute(self, userdata):
        # Lecture dans le tube
        self._detectedID = pipe.listener(self._fifo)

        # Tester sans le tube (commenter les lignes avec le tube)
        # self._detectedID = random.randint(1, 6)
        # self._detectedID = pow(2, self._detectedID)

        # On a exécuté une action qui arrête le Dagu pendant 3 secondes
        # On redémarre les actions après 4 secondes et s'il n'y a pas de Dagu détecté
        if self._lastTimeExecute != -1:
            # self._detectedID = random.randint(0, 1)
            if self._detectedID == 0:
                try:
                    talker.talker("DaguDetected")
                except rospy.ROSInterruptException:
                    pass
            elif rospy.Time.now() - self._lastTimeExecute >= self._timeToWait:
                self._lastTimeExecute = -1
            return 'default'

        # Sécurité. Valeur censée ne jamais apparaître
        if self._detectedID == -1:
            return 'default'
        
        Logger.loginfo("Somme : " + str(self._detectedID))
        
        # Si on a détecté un Dagu hors action, on s'arrête
        # On redémarre quand le Dagu n'est plus là
        if self._detectedID == 0:
            if self._isDaguDetected == False:
                self._isDaguDetected = True
                try:
                    talker.talker("Stop")
                except rospy.ROSInterruptException:
                    pass
            return 'default'
        else:
            if self._isDaguDetected == True:
                self._isDaguDetected = False
                try:
                    talker.talker("Start")
                except rospy.ROSInterruptException:
                    pass

        # Si on a reçu un entier positif, c'est que l'IA a détecté des panneaux
        if self._detectedID > 0:
            # On décompose la somme reçue
            self.decompose()

            # On regarde chaque panneau pour réinitialiser si ça fait plus de 5 s ou pour exécuter
            for i in range(1, 7):
                if self._buffer[i].getTimer() != 0:
                    if rospy.Time.now() - self._buffer[i].getTimer() >= self._timeReset:
                        self._buffer[i].resetTimes()

                # Exécution dès qu'on a détecté le panneau plus de 5 fois
                if self._buffer[i].getTimes() >= 5:
                    self._buffer[i].resetTimes()
                
                    if i == 1:
                        return 'speed_50'
                    elif i == 2:
                        return 'priority'
                    elif i == 3:
                        self._lastTimeExecute = rospy.Time.now()
                        self._timeToWait = rospy.Duration(0)
                        return 'yieldSign'
                    elif i == 4:
                        self._lastTimeExecute = rospy.Time.now()
                        self._timeToWait = rospy.Duration(4)
                        return 'stop'
                    elif i == 5:
                        return 'forbidden'
                    elif i == 6:
                        return 'danger'
                    else:
                        return 'failed'
        else:
            self._detectedID = self._detectedID * -1
            
            if self._detectedID > 180:
                message = "Turn_G"
            else:
                message = "Turn_D"

            try:
                talker.talker(message)
            except rospy.ROSInterruptException:
                pass

    # Méthode de décomposition de la somme reçue
    def decompose(self):
        for i in range(6, 0, -1):
            power = pow(2, i)
            if self._detectedID >= power:
                self._detectedID -= power
                self._buffer[i].setTimer()
                self._buffer[i].incTimes()
                Logger.loginfo("Detected :" + str(i) + " - " + str(self._buffer[i].getTimes()))
            

class SignInfo():
    # timesDetected : nombre de fois qu'on a reçu le panneau
    # timer : dernière fois que le panneau a été détecté
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
