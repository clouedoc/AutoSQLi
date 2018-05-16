#!/usr/bin/env python3
# Adapted to the new save system

from autosqli import log  # provides log.info/debug/warning/critical
from autosqli.parse_args import argument_parse  # provides argument_parse()
# from autosqli.save import Save           # provides Save() [class]
from autosqli import save
from autosqli import stages

# TODO: create a classes system for stages ( base stage class and sub class
# stages. I don't really know how I would do this for now, but fonctionnal
# programming ( which I think I'm doing seems not to be the best approach here
# ^^' )


def main():
    args = argument_parse()

    if args.debug:
        log.debug("Ok boss, launching in debug mode")
        import pudb
        pudb.set_trace()  # XXX BREAKPOINT

    log.info("Welcome into AutoSQLi!")
    log.debug("Checking for saves...")
    save.saveStartup(args)
    log.debug("Loading save...")
    save.importSave()

    log.debug("current_save.stage in main(): " + str(save.getStage()))

    while True:
        # do the current stage and increment
        log.debug("Getting into the next stage")
        need_to_continue = stages.nextStage(args)
        # backup the current state (into autosqli.save)
        save.writeSave()  # TODO: add a time based saver
        log.debug("Save exported")
        if save.getStage() == stages.REPORT_STAGE or need_to_continue is False:
            break

    log.info("Goodbye!")


if __name__ == "__main__":
    main()
