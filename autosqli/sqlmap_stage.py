# From AutoSQLi
from autosqli import save
from autosqli import sqlmap_interface

SQLMAP_OPTIONS = {}


def sqlmap_stage(args):
    """ do a sqlmap scan on all the targets """

    while True:
        target = save.get_unsqlmapped_target()

        if target is None:
            break
        else:
            sqlmapped_target = sqlmap_interface.sqlmap_target(target,
                                                              SQLMAP_OPTIONS)
            save.update_target(sqlmapped_target)
