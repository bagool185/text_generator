
class State:
    """ Markov chain state """
    def __init__(self, value, label, next_words):
        self.value = value
        self.label = label
        # Steps to the other states.
        self.next_words = next_words
