# From AutoSQLi

from autosqli import log
from autosqli import save


def report_stage(args):
    # TODO: add a --json argument
    # TODO: better display
    log.info("Launching the report stage")

    # display targets that are vulnerables
    print('-' * 5 + '\tvulnerable targets' + '\t-' * 5)
    for target in save.get_vulnerable_targets():
        print(target)  # prints the string representation of the target.

    print('-' * 5 + '\tinvulnerable targets' + '\t-' * 5)
    for target in save.get_invulnerable_targets():
        print(target)  # prints the string representation of the target.
