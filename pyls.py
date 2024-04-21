"""
Write a Python program, that takes a json file (which contains the information
of a directory in nested structure) and prints out its content in the console in
the style of ls (linux utility).
"""

import sys
import json
from ls_command.ls_methods import *

def open_file(file_path):
    # Opening JSON file
    file = open(file_path)
    return file


def load_data(file):
    # returns JSON object as a dictionary
    data = json.load(file)
    return data


def close_file(file):
    # Closing file
    file.close()


if __name__ == '__main__':

    number_of_parameters = len(sys.argv)

    parameters = sys.argv

    file_path_ = 'files/structure.json'

    file_ = open_file(file_path_)

    data_ = load_data(file_)

    close_file(file_)

    if number_of_parameters > 1:

        if sys.argv[1] == '-l':

            if number_of_parameters>2:

                if sys.argv[2] == '-r':

                    if number_of_parameters>3:

                        if sys.argv[3] == '-t':

                            if number_of_parameters>4:

                                if sys.argv[4].startswith('--filter'):
                                    # Subtask 6: ls -l -r -t --filter=<option>
                                    # python -m pyls -l       -r      -t  --filter=dir
                                    # TODO: def ls_l_r_t__filter(data_)
                                    pass

                                else:
                                    print('Invalid argument passed: {}'.format(sys.argv[4]))

                            else:
                                # Subtask 5: ls -l -r -t
                                # python -m pyls -l       -r      -t
                                ls_l_r_t(data_)

                        else:
                            print('Invalid argument passed: {}'.format(sys.argv[3]))


                    else:
                        # Subtask 4: ls -l -r
                        # python -m pyls -l       -r
                        ls_l_r(data_)

                else:
                    # Subtask 7: Handle Paths
                    # python -m pyls -l       <path>
                    pass

            else:
                # Subtask 3: ls -l
                # python -m pyls -l
                ls_l(data_)

        elif sys.argv[1] == '-A':
            # Subtask 2: ls -A
            # python - m pyls - A
            ls_a(data_)

        elif sys.argv[1] == '-h':
            # Subtask 8: ls -h
            # python -m pyls -h       <path>
            # TODO: def ls_h(data_)
            pass

        elif sys.argv[1] == '--help':
            # Subtask 9: ls --help
            # python -m pyls --help
            # TODO: def ls__help(data_)
            pass

        else:
            print('Invalid argument passed: {}'.format(sys.argv[1]))

    else:
        # Subtask 1: ls
        # python -m pyls
        ls(data_)
