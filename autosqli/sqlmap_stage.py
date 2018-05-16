# From AutoSQLi
from autosqli import save
from autosqli import sqlmap_interface


def sqlmap_stage(args):
    """ do a sqlmap scan on all the targets """

    while True:
        target = save.get_unsqlmapped_target()

        if target is None:
            break


