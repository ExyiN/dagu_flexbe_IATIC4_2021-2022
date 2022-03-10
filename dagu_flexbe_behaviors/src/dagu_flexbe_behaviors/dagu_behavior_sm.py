#!/usr/bin/env python
# -*- coding: utf-8 -*-
###########################################################
#               WARNING: Generated code!                  #
#              **************************                 #
# Manual changes may get lost if file is generated again. #
# Only code inside the [MANUAL] tags will be kept.        #
###########################################################

from flexbe_core import Behavior, Autonomy, OperatableStateMachine, ConcurrencyContainer, PriorityContainer, Logger
from dagu_flexbe_states.dagu_danger_state import DaguDangerState
from dagu_flexbe_states.dagu_forbidden_dir_state import DaguForbiddenDirState
from dagu_flexbe_states.dagu_initial_state import DaguInitialState
from dagu_flexbe_states.dagu_speed_50_state import DaguSpeed50State
from dagu_flexbe_states.dagu_stop_state import DaguStopState
from dagu_flexbe_states.dagu_yield_state import DaguYieldState
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
		# x:978 y:342, x:237 y:502
		_state_machine = OperatableStateMachine(outcomes=['finished', 'failed'])

		# Additional creation code can be added inside the following tags
		# [MANUAL_CREATE]
		
		# [/MANUAL_CREATE]


		with _state_machine:
			# x:260 y:304
			OperatableStateMachine.add('Initial_State',
										DaguInitialState(detectedID=self.detectedID),
										transitions={'default': 'Initial_State', 'stop': 'Stop_State', 'speed_50': 'Speed50', 'yieldSign': 'Yield', 'forbidden': 'Forbidden', 'danger': 'Danger', 'failed': 'failed'},
										autonomy={'default': Autonomy.Off, 'stop': Autonomy.Off, 'speed_50': Autonomy.Off, 'yieldSign': Autonomy.Off, 'forbidden': Autonomy.Off, 'danger': Autonomy.Off, 'failed': Autonomy.Off})

			# x:550 y:383
			OperatableStateMachine.add('Forbidden',
										DaguForbiddenDirState(),
										transitions={'idle': 'finished'},
										autonomy={'idle': Autonomy.Off})

			# x:549 y:465
			OperatableStateMachine.add('Speed50',
										DaguSpeed50State(),
										transitions={'changing': 'Initial_State'},
										autonomy={'changing': Autonomy.Off})

			# x:551 y:62
			OperatableStateMachine.add('Stop_State',
										DaguStopState(),
										transitions={'restarting': 'Initial_State'},
										autonomy={'restarting': Autonomy.Off})

			# x:549 y:545
			OperatableStateMachine.add('Yield',
										DaguYieldState(),
										transitions={'restarting': 'Initial_State'},
										autonomy={'restarting': Autonomy.Off})

			# x:554 y:211
			OperatableStateMachine.add('Danger',
										DaguDangerState(),
										transitions={'restarting': 'Initial_State'},
										autonomy={'restarting': Autonomy.Off})


		return _state_machine


	# Private functions can be added inside the following tags
	# [MANUAL_FUNC]
	
	# [/MANUAL_FUNC]
