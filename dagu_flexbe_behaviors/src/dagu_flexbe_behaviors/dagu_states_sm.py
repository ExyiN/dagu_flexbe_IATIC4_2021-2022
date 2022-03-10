#!/usr/bin/env python
# -*- coding: utf-8 -*-
###########################################################
#               WARNING: Generated code!                  #
#              **************************                 #
# Manual changes may get lost if file is generated again. #
# Only code inside the [MANUAL] tags will be kept.        #
###########################################################

from flexbe_core import Behavior, Autonomy, OperatableStateMachine, ConcurrencyContainer, PriorityContainer, Logger
from tutorial_flexbe_states.dagu_danger_state import DaguDangerState
from tutorial_flexbe_states.dagu_forbidden_dir_state import DaguForbiddenDirState
from tutorial_flexbe_states.dagu_initial_state import DaguInitialState
from tutorial_flexbe_states.dagu_stop_state import DaguStopState
from tutorial_flexbe_states.dagu_yield_state import DaguYieldState
# Additional imports can be added inside the following tags
# [MANUAL_IMPORT]

# [/MANUAL_IMPORT]


'''
Created on Thu Mar 10 2022
@author: VIDAL
'''
class Dagu_statesSM(Behavior):
	'''
	Liste des états que le Dagu peut avoir
	'''


	def __init__(self):
		super(Dagu_statesSM, self).__init__()
		self.name = 'Dagu_states'

		# parameters of this behavior
		self.add_parameter('speed', 50)

		# references to used behaviors

		# Additional initialization code can be added inside the following tags
		# [MANUAL_INIT]
		
		# [/MANUAL_INIT]

		# Behavior comments:



	def create(self):
		# x:30 y:365, x:130 y:365
		_state_machine = OperatableStateMachine(outcomes=['finished', 'failed'])

		# Additional creation code can be added inside the following tags
		# [MANUAL_CREATE]
		
		# [/MANUAL_CREATE]


		with _state_machine:
			# x:169 y:255
			OperatableStateMachine.add('Initial',
										DaguInitialState(detectedID=1),
										transitions={'default': 'finished', 'stop': 'Stop', 'speed_50': 'failed', 'yieldSign': 'Yield', 'forbidden': 'Forbidden', 'danger': 'Danger'},
										autonomy={'default': Autonomy.High, 'stop': Autonomy.High, 'speed_50': Autonomy.High, 'yieldSign': Autonomy.High, 'forbidden': Autonomy.High, 'danger': Autonomy.High})

			# x:555 y:140
			OperatableStateMachine.add('Forbidden',
										DaguForbiddenDirState(),
										transitions={'idle': 'Initial'},
										autonomy={'idle': Autonomy.High})

			# x:602 y:455
			OperatableStateMachine.add('Stop',
										DaguStopState(),
										transitions={'initial': 'Initial'},
										autonomy={'initial': Autonomy.Off})

			# x:600 y:39
			OperatableStateMachine.add('Yield',
										DaguYieldState(),
										transitions={'restarting': 'Initial'},
										autonomy={'restarting': Autonomy.Off})

			# x:594 y:362
			OperatableStateMachine.add('Danger',
										DaguDangerState(),
										transitions={'initial': 'Initial'},
										autonomy={'initial': Autonomy.Off})


		return _state_machine


	# Private functions can be added inside the following tags
	# [MANUAL_FUNC]
	
	# [/MANUAL_FUNC]
