# From AutoSQLi

from autosqli import log
from autosqli.save import getInvulnerableTargets, getVulnerableTargets


def report_stage(args):
    # TODO: add a --json argument
    # TODO: better display
    log.info("Launching the report stage")

    # display targets that are vulnerables
    print('-' * 5 + '\tvulnerable targets' + '\t-' * 5)
    for target in getVulnerableTargets():
        print(target)  # prints the string representation of the target.

    print('-' * 5 + '\tinvulnerable targets' + '\t-' * 5)
    for target in getInvulnerableTargets():
        print(target)  # prints the string representation of the target.
