
class State:
    """ Markov chain state """
    def __init__(self):
        self.name = ""
        self.label = ""
        # Position in the transition matrix.
        self.position = 11 # first row first column
        # Steps to the other states.
        self.steps = dict()
