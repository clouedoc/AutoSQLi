# From AutoSQLi
import subprocess


def execute(command, cwd=None, timeout=None, yes=None):
    """ must be an array """
    """ returns the stdout of command """
    """ command is an array of args """
    """ cwd is the current directory in which the command shall be executed """
    """ Timeout is the timeout of the command """
    """ yes = True: constantly feed stdin with a "y" """
    """ yes = False: constantly feed stdin with a "n" """
    finalCommand = []

    if yes != None:
        finalCommand.append("yes |" if yes else "yes n |")

    for arg in command:
        finalCommant.append(arg)

    result = subprocess.run(finalCommand, stdout=subprocess.PIPE, cwd=cwd,
                            timeout=timeout,
                            shell=True if yes != None else None)
    return result.stdout.decode('utf-8')
