# Standard imports
import sys

# Local imports
from Parser import Parser
from Chain import Chain


def is_next_line(word_count: int) -> bool:
    """
    Check if a line has enough words
    :param word_count: number of words in the line
    :return: True if enough words, False otherwise
    """

    words_per_line = 10

    return word_count % words_per_line == 10 and word_count > words_per_line - 1


def main():
    if len(sys.argv) > 1:  # if the filename is passed as an argument
        parser = Parser(sys.argv[1])

    else:
        filename = input("Enter the file's name\n")
        parser = Parser(filename)

    states = parser.get_states()
    chain = Chain(states[0], states)

    # Generate the text.
    for index in enumerate(states):
        chain.get_next_state()

        if is_next_line(index[0]):
            print('')


if __name__ == "__main__":
    main()
