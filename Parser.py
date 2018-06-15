from Chain import Chain 
from State import State 

import re

class Parser:
    """ Parse chain states from a text file """
    
    def __init__(self, filename):

        self.filename = filename

    def format_word(self, word):
        """ Return a string representing a stripped and lowercase word 
            containing only alpha-numeric characters
        """
        word = word.strip().lower()
        regex = re.compile('[,\.!?;:]')
        word = regex.sub('', word)

        return word

    def generate_states(self):
        """ Return a dictionary mapping words with their candidates
            i.e. words that follow them
        """
        read_file = open(self.filename, "r")

         # Temp dictionary to map words with their candidates.
        word_candidates = dict()

        for line in read_file:
            prev_word = ""

            for word in re.split(' |\.|\n', line):

                word = self.format_word(word)

                if prev_word != "" and word != "": # check if it's the first word in the sentence

                    if prev_word in word_candidates:
                        word_candidates[prev_word].append(word)
                    else:
                        word_candidates[prev_word] = [word]

                prev_word = word

        return word_candidates

    def get_states(self):
        """ Return a list of States """

        word_candidates = self.generate_states()
        states = list()
       
        label = 0

        for state, next_words in word_candidates.items():
            states.append(State(state, label, next_words))
            label += 1
    
        return states



