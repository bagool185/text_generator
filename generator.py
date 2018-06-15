from Parser import Parser
from Chain import Chain

import sys

def main():

    if (len(sys.argv) > 1): # if the filename is passed as an argument
        parser = Parser(sys.argv[1])

    else:
        filename = input("Enter the file's name\n")
        parser = Parser(filename)

    states = parser.create_states()
    chain = Chain(states[0], states)
    # Generate the text.
    for index in enumerate(states):
        chain.get_next_state()

        if index[0] % 7 == 0:
            print('')


if __name__ == "__main__":
    main()