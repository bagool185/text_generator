 
from State import State

import numpy as np
import random

class Chain:
    """ Markov chain """
d
    def __init__(self, current_state, states):

        self.states = states 
        self.current_state = current_state 

    def get_next_state(self):
        """ Update the current_state property with the new state """
        candidates = self.current_state.next_words

        rand = random.randrange(0, len(candidates))

        new_state = candidates.keys()[rand]
        
        for state in self.states:
            if state.value == new_state:
                self.current_state = state
                break 