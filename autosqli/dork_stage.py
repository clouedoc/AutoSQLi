# Adapted to the new save system
# from .target import urls_to_targets
import os

from autosqli import log
from autosqli import find_dorks  # provides find_dorks.dorkLines(dorks)

# from . import save


def search_dork(dorks):
    return find_dorks.dorkLines(dorks)


def getdorks(args):
    if args.dorkfile is not None and args.dork is not None:
        log.critical("-f (--dork-file) and -d (--dork) are incompatible")
        exit(1)
    elif args.dorkfile is not None:
        if os.path.isfile(args.dorkfile):
            lines = []
            try:
                with open(args.dorkfile) as dork_file:
                    for line in dork_file:
                        lines.append(line)
            except IOError as e:
                log.critical('Got an error when reading the supplied dork file\
                             (-f/--dork-file): {}'.format(e))
        else:
            log.critical(
                "The dork file supplied (-f/--dork-file) does not exists"
            )
        pass  # TODO: accept a dorkfile
    elif args.dorkfile is None and args.dork is None:
        log.debug("interactively querying dork")
        log.info("Enter a dork:")
        dorks = [input("dork: ")]
    else:
        dorks = [args.dork]

    return dorks


def dork_stage(args):
    """ add targets to the save """

    # get dorks from the args provided
    dorks = getdorks(args)

    # search_dork create targets by itself
    search_dork(dorks)
