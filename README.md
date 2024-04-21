# ls-command
Takes a json file (which contains the information of a directory in nested structure) and prints out its content in the console in the style of ls (linux utility).

Subtask 1: ls                                   python -m pyls
Subtask 2: ls -A                                python -m pyls -A
Subtask 3: ls -l                                python -m pyls -l
Subtask 4: ls -l -r                             python -m pyls -l       -r
Subtask 5: ls -l -r -t                          python -m pyls -l       -r      -t
Subtask 6: ls -l -r -t --filter=<option>        python -m pyls -l       -r      -t  --filter=dir (or file)
Subtask 7: Handle Paths                         python -m pyls -l       <path>
Subtask 8: ls -h                                python -m pyls -h       <path>
Subtask 9: ls --help                            python -m pyls --help

To install:
pip install .

To run:
python pyls.py <arguments>

To test:
python -m pytest tests