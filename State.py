
class State:
    """ Markov chain state """
    def __init__(self):
        self.value = ""
        self.label = ""
        # Steps to the other states.
        self.next_words = dict()
