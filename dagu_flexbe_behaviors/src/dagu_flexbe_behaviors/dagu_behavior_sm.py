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
from flexbe_states.log_state import LogState
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
		self.add_parameter('default_id', 0)
		self.add_parameter('detected_id', 0)

		# references to used behaviors

		# Additional initialization code can be added inside the following tags
		# [MANUAL_INIT]
		
		# [/MANUAL_INIT]

		# Behavior comments:



	def create(self):
		changing_msg = "Changement d'état !"
		not_changing_msg = "On reste dans l'état actuel"
		# x:54 y:499, x:237 y:502
		_state_machine = OperatableStateMachine(outcomes=['finished', 'failed'])

		# Additional creation code can be added inside the following tags
		# [MANUAL_CREATE]
		
		# [/MANUAL_CREATE]


		with _state_machine:
			# x:329 y:136
			OperatableStateMachine.add('Initial_State',
										DaguInitialState(default_id=self.default_id, detected_id=self.detected_id),
										transitions={'changing_state': 'Print_changing', 'not_changing': 'Print_not_changing'},
										autonomy={'changing_state': Autonomy.Off, 'not_changing': Autonomy.Off})

			# x:136 y:305
			OperatableStateMachine.add('Print_changing',
										LogState(text=changing_msg, severity=Logger.REPORT_HINT),
										transitions={'done': 'finished'},
										autonomy={'done': Autonomy.High})

			# x:411 y:350
			OperatableStateMachine.add('Print_not_changing',
										LogState(text=not_changing_msg, severity=Logger.REPORT_HINT),
										transitions={'done': 'finished'},
										autonomy={'done': Autonomy.High})


		return _state_machine


	# Private functions can be added inside the following tags
	# [MANUAL_FUNC]
	
	# [/MANUAL_FUNC]
