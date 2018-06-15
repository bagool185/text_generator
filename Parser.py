from Chain import Chain 
from State import State 

import re

class Parser:
    """ Parse a text file """
    
    def __init__(self, filename):

        self.filename = filename


    def create_states(self):

        read_file = open(self.filename, "r")

        states = list()
        temp = dict()

        for line in read_file:
            prev_word = ""

            for word in line.split(' '):

                word = word.strip()
                regex = re.compile('[,\.!?;:]')
                word = regex.sub('', word)

                if prev_word != "":

                    if prev_word in temp:
                        temp[prev_word].append(word)
                    else:
                        temp[prev_word] = [word]

                prev_word = word


        label = 0

        for state, next_words in temp.items():
            states.append(State(state, label, next_words))
            label += 1
    
        return states



