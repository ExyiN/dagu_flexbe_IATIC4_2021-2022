#!/usr/bin/env python
# -*- coding: utf-8 -*-
###########################################################
#               WARNING: Generated code!                  #
#              **************************                 #
# Manual changes may get lost if file is generated again. #
# Only code inside the [MANUAL] tags will be kept.        #
###########################################################

from flexbe_core import Behavior, Autonomy, OperatableStateMachine, ConcurrencyContainer, PriorityContainer, Logger
from dagu_flexbe_states.dagu_initial_state import DaguInitialState
from dagu_flexbe_states.dagu_stop_state import DaguStopState
# Additional imports can be added inside the following tags
# [MANUAL_IMPORT]

# [/MANUAL_IMPORT]


'''
Created on Thu Jan 20 2022
@author: Jacques Tea
'''
class Dagu_BehaviorSM(Behavior):
	'''
	Behavior for the Dagu project
	'''


	def __init__(self):
		super(Dagu_BehaviorSM, self).__init__()
		self.name = 'Dagu_Behavior'

		# parameters of this behavior
		self.add_parameter('detectedID', 0)

		# references to used behaviors

		# Additional initialization code can be added inside the following tags
		# [MANUAL_INIT]
		
		# [/MANUAL_INIT]

		# Behavior comments:



	def create(self):
		default = "Etat initial"
		stop = "Panneau stop détecté"
		# x:54 y:499, x:237 y:502
		_state_machine = OperatableStateMachine(outcomes=['finished', 'failed'])

		# Additional creation code can be added inside the following tags
		# [MANUAL_CREATE]
		
		# [/MANUAL_CREATE]


		with _state_machine:
			# x:263 y:109
			OperatableStateMachine.add('Initial_State',
										DaguInitialState(detectedID=self.detectedID),
										transitions={'default': 'finished', 'stop': 'Stop_State', 'failed': 'failed'},
										autonomy={'default': Autonomy.Off, 'stop': Autonomy.Off, 'failed': Autonomy.Off})

			# x:401 y:326
			OperatableStateMachine.add('Stop_State',
										DaguStopState(),
										transitions={'restarting': 'finished'},
										autonomy={'restarting': Autonomy.Off})


		return _state_machine


	# Private functions can be added inside the following tags
	# [MANUAL_FUNC]
	
	# [/MANUAL_FUNC]
