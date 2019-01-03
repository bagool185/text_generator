import random


class Chain:
    """ Markov chain """

    def __init__(self, initial_state, states):

        self.states = states
        self.current_state = initial_state

        print(self.current_state.value, end=' ')

    def get_next_state(self):
        """ Update the current_state property with the new state """
        # Iterate through words until a non-terminal one is found
        # i.e. a word not followed by anything 
        while len(self.current_state.next_words) == 0:
            rand = random.randrange(0, len(self.states))
            self.current_state = self.states[rand]
        
        candidates = self.current_state.next_words
        # Pick a random candidate and then delete it
        # in order not to repeat it.
        rand = random.randrange(0, len(candidates))
        new_state = candidates[rand]
        del candidates[rand]

        print(new_state, end=' ')
        # Look for the state corresponding to the candidate
        # and update the current state with it.
        for state in self.states:
            if state.value == new_state:
                self.current_state = state
                break
