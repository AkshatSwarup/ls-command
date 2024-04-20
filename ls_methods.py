import time
from datetime import datetime


def ls(data):
    """
    First command to implement is ls. Name of your program should be pyls. For
    the above structure, your script should parse the json file, and when run like
    the following:
    $ python -m pyls
    Should produce the following output:
    LICENSE README.md ast go.mod lexer main.go parser token
    This lists out the top level (in the directory interpreter) directories and files.
    Notice it does not list .gitignore, because that is the default behaviour of ls,
    i.e. files and directories whose names start with . are omitted by default.
    NOTE: following are some command line arguments that you will need to
    implement, it should be implemented in such a way, that the command line
    arguments are composable with each other.
    """

    # Iterating through the json
    names = ''
    for line in data['contents']:
        # skip files starting with '.'
        if not str(line['name']).startswith('.'):
            names = names + line['name'] + ' '
    print(names)


def ls_a(data):
    """
    Implement the argument -A, which prints all the files and directories (including
    files starting with ’.’), example:
    $ python -m pyls -A
    Should produce the following output:
    .gitignore LICENSE README.md ast go.mod lexer main.go parser token
    """

    # Iterating through the json
    names = ''
    for line in data['contents']:
        names = names + line['name'] + ' '
    print(names)


def ls_l(data):
    """
    Implement the argument -l, that prints the results vertically with additional
    information:
    $ python -m pyls -l
    -rw-r--r-- 1071 Nov 14 11:27 LICENSE
    -rw-r--r-- 83 Nov 14 11:27 README.md
    drwxr-xr-x 4096 Nov 14 15:58 ast
    -rw-r--r-- 60 Nov 14 13:51 go.mod
    drwxr-xr-x 4096 Nov 14 15:21 lexer
    -rw-r--r-- 74 Nov 14 13:57 main.go
    drwxr-xr-x 4096 Nov 17 12:51 parser
    drwxr-xr-x 4096 Nov 14 14:57 token
    NOTE: First column corresponds to permissions, 2nd column corresponds to
    size, 3rd to 5th is date and time, and the last is file or directory name.
    """

    # Iterating through the json
    information = ''
    for line in data['contents']:

        if not str(line['name']).startswith('.'):
            permissions = line['permissions']

            size = str(line['size'])

            time_modified = line['time_modified']
            date_string = time.ctime(time_modified)
            date_format = "%a %b %d %H:%M:%S %Y"
            date_time = datetime.strptime(date_string, date_format)
            expected_format = "%b %d %H:%M"
            date = datetime.strftime(date_time, expected_format)

            name = line['name']

            information = permissions + '\t' + size + '\t' + str(date) + '\t' + name

            print(information)


def ls_l_r(data):
    """
    Implement the argument -r, that prints the results in reverse:
    $ python -m pyls -l -r
    drwxr-xr-x 4096 Nov 14 14:57 token
    drwxr-xr-x 4096 Nov 17 12:51 parser
    -rw-r--r-- 74 Nov 14 13:57 main.go
    drwxr-xr-x 4096 Nov 14 15:21 lexer
    -rw-r--r-- 60 Nov 14 13:51 go.mod
    drwxr-xr-x 4096 Nov 14 15:58 ast
    -rw-r--r-- 83 Nov 14 11:27 README.md
    -rw-r--r-- 1071 Nov 14 11:27 LICENSE
    """

    # Iterating through the json
    information = list()
    for line in data['contents']:

        if not str(line['name']).startswith('.'):
            permissions = line['permissions']

            size = str(line['size'])

            time_modified = line['time_modified']
            date_string = time.ctime(time_modified)
            date_format = "%a %b %d %H:%M:%S %Y"
            date_time = datetime.strptime(date_string, date_format)
            expected_format = "%b %d %H:%M"
            date = datetime.strftime(date_time, expected_format)

            name = line['name']

            information_line = permissions + '\t' + size + '\t' + str(date) + '\t' + name

            information.append(information_line)

    information.reverse()

    for line in information:
        print(line)


def ls_l_r_t(data):
    """
    Implement the argument -t that prints the results sorted by time_modified
    (oldest first):
    $ python -m pyls -l -r -t
    drwxr-xr-x 4096 Nov 17 12:51 parser
    drwxr-xr-x 4096 Nov 14 15:58 ast
    drwxr-xr-x 4096 Nov 14 15:21 lexer
    drwxr-xr-x 4096 Nov 14 14:57 token
    -rw-r--r-- 74 Nov 14 13:57 main.go
    -rw-r--r-- 60 Nov 14 13:51 go.mod
    -rw-r--r-- 1071 Nov 14 11:27 LICENSE
    -rw-r--r-- 83 Nov 14 11:27 README.md
    NOTE: Notice, in the above example, the flag -r is also present, so the files
    are printed in reverse order of time_modified (i.e. newest first)
    """

    # Iterating through the json
    information = dict()
    for line in data['contents']:

        if not str(line['name']).startswith('.'):
            permissions = line['permissions']

            size = str(line['size'])

            time_modified = line['time_modified']
            date_string = time.ctime(time_modified)
            date_format = "%a %b %d %H:%M:%S %Y"
            date_time = datetime.strptime(date_string, date_format)
            expected_format = "%b %d %H:%M"
            date = datetime.strftime(date_time, expected_format)

            name = line['name']
            information_line = permissions + '\t' + size + '\t' + str(date) + '\t' + name
            information[information_line] = time_modified

    res = {key: val for key, val in sorted(information.items(), key=lambda kv: (kv[1], kv[0]), reverse=True)}

    for info, timestamp in res.items():
        # print(timestamp)
        print('{}'.format(info))


def ls_l_r_t__filter(data_):
    # TODO: code logic
    pass


def ls_h(data_):
    # TODO: code logic
    pass


def ls__help(data_):
    # TODO: code logic
    pass
