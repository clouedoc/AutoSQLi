#!/usr/bin/env python3
# Adapted to the new save system

from src import log  # provides log.info/debug/warning/critical
from src.parse_args import argument_parse  # provides argument_parse()
# from src.save import Save           # provides Save() [class]
from src import save
from src import stages

# TODO: create a classes system for stages ( base stage class and sub class
# stages. I don't really know how I would do this for now, but fonctionnal
# programming ( which I think I'm doing seems not to be the best approach here
# ^^' )

# TODO: it would be nice if everything could be moved in specific classes, like
# a `nextStage.py` file and a `main.py` file in the `src` directory


def main():
    args = argument_parse()

    if args.debug:
        log.debug("Ok boss, launching in debug mode")
        import pdb
        pdb.set_trace()  # XXX BREAKPOINT

    log.info("Welcome into AutoSQLi!")
    log.debug("Checking for saves...")
    save.saveStartup(args)
    log.debug("Loading save...")
    save.importSave()

    log.debug("current_save.stage in main(): " + str(save.getStage()))

    while True:
        if args.debug:
            log.debug("activating breakpoint")
            pdb.set_trace()

        # do the current stage and increment
        log.debug("Getting into the next stage")
        stages.nextStage(args)
        # backup the current state (into autosqli.save)
        save.writeSave()  # TODO: add a time based saver
        log.debug("Save exported")
        if save.getStage() == stages.REPORT_STAGE:
            break

    log.info("Goodbye!")


if __name__ == "__main__":
    main()
