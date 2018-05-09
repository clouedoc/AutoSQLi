import subprocess


def execute(command, cwd=None, timeout=None):
    """ must be an array """
    """ returns the stdout of command """
    print(cwd)
    result = subprocess.run(command, stdout=subprocess.PIPE, cwd=cwd, timeout=timeout)
    return result.stdout.decode('utf-8')
