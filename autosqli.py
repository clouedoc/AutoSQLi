#!/usr/bin/env python3

from src import log             # provides log.info/debug/warning/critical
from src.parse_args import argument_parse  # provides argument_parse()
# from src.save import Save           # provides Save() [class]
from src.save import current_save
from src import stages
from src import checks
from src.dork_stage import dorkStage
from src.waf_detect_stage import wafDetectStage

# TODO: create a classes system for stages ( base stage class and sub class
# stages. I don't really know how I would do this for now, but fonctionnal
# programming ( which I think I'm doing seems not to be the best approach here
# ^^' )

# TODO: it would be nice if everything could be moved in specific classes, like
# a `nextStage.py` file and a `main.py` file in the `src` directory

# FIXME: once the save system for the waf stage is fixed, make sure that it is
# for the dork stage too !

# TODO: URGENT: rebuild the save system with ZODB. check src/checks.py and
# src/save.py to reconstruct the api


def nextStage(args):
    """ execute the current stage out of current_save   """
    """ increase the stage number after it's execution  """
    global current_save

    if current_save.stage == stages.DORK_STAGE:     # if in dork stage
        log.debug("Launching the dork stage")
        dorkStage(args)  # launch the dork stage

    if current_save.stage == stages.WAF_DETECT_STAGE:
        log.debug("Launching the waf stage")
        wafDetectStage(args)

    if current_save.stage == stages.SQLMAP_STAGE:
        pass  # TODO: call the sqlmap stage

    log.debug("New stage number: " + str(current_save.stage))


def main():
    global current_save

    args = argument_parse()

    if args.debug:
        log.debug("ok boss, launching the debug mode")
        import pdb; pdb.set_trace()  # XXX BREAKPOINT

    log.info("Welcome into AutoSQLi !")

    # check if a save is already present, and if no, create a new one
    current_save = checks.saveChecks(args, current_save)  # set current save
    log.debug("current_save.stage in main(): " + str(current_save.stage))
    import pdb; pdb.set_trace()  # XXX BREAKPOINT

    while True:
        # do the current stage and increment
        log.debug("Getting into the next stage")
        nextStage(args)
        # backup the current state (into autosqli.save)
        current_save.simpleExportSave()
        log.debug("save exported")
        if current_save.stage > stages.REPORT_STAGE:
            break

    log.info("Goodbye !")


if __name__ == "__main__":
    main()
