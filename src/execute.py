# From AutoSQLi
import subprocess
from . import log
from .satanize import satanize_for_bash


def execute(command, cwd=None, timeout=None, yes=None):
    """ must be an array """
    """ returns the stdout of command """
    """ command is an array of args """
    """ cwd is the current directory in which the command shall be executed """
    """ Timeout is the timeout of the command """
    """ yes = True: constantly feed stdin with a "y" """
    """ yes = False: constantly feed stdin with a "n" """
    pre_command = []

    if yes is not None:
        pre_command.append("yes |" if yes else "yes n |")

    import pdb; pdb.set_trace()  # XXX BREAKPOINT
    for arg in command:
        pre_command.append(arg)

    assembled_pre_command = ""
    for arg in pre_command:
        assembled_pre_command += " " + arg

    final_command = ["bash -c {}".format(
        satanize_for_bash(assembled_pre_command))]

    shellmode = True if yes is not None else None
    log.debug("command: {}; cwd: {}; timeout: {}; shellmode: {}".format(
        final_command, cwd, timeout, shellmode))
    import pdb; pdb.set_trace()  # XXX BREAKPOINT
    result = subprocess.run(final_command, stdout=subprocess.PIPE, cwd=cwd,
                            timeout=timeout,
                            shell=shellmode)
    return result.stdout.decode('utf-8')
