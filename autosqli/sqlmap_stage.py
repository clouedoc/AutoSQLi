# From AutoSQLi
from autosqli import save
from autosqli import sqlmap_interface


def sqlmap_stage(args):
    """ do a sqlmap scan on all the targets """

    while True:
        with save.get_unsqlmapped_target() as target:
            # there is no not sqlmapped target remaining
            if target is None:
                break


