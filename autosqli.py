#!/usr/bin/env python3

from src import log             # provides log.info/debug/warning/critical
from src.parse_args import argument_parse  # provides argument_parse()
from src.save import Save           # provides Save() [class]
from src import stages
from src import checks
from src.dork_stage import dorkStage
from src.waf_detect_stage import wafDetectStage

current_save = Save()


def nextStage(args):
    """ execute the current stage out of current_save   """
    """ increase the stage number after it's execution  """
    global current_save

    if current_save.stage == stages.DORK_STAGE:     # if in dork stage
        log.debug("Launching the dork stage")
        current_save.targets_to_test = dorkStage(args)  # launch the dork stage

    if current_save.stage == stages.WAF_DETECT_STAGE:
        log.debug("Launching the waf stage")
        current_save.targets_to_test = \
            wafDetectStage(args, current_save.targets_to_test)

    current_save.stage += 1
    log.debug("New stage number: " + str(current_save.stage))


def main():
    global current_save
    args = argument_parse()
    if args.debug:
        log.debug("ok boss, launching the debug mode")
        import pdb; pdb.set_trace()  # XXX BREAKPOINT

    log.info("Welcome into AutoSQLi !")

    # check if a save is already present, and if no, create a new one
    current_save = checks.saveChecks(args, current_save)
    log.debug("current_save.stage in main(): " + str(current_save.stage))

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

    # WAF_DETECT_STAGE =============================

    # WTF TODO:
    # now, we have a list of urls to test.
    # we gonna take all the urls one by one and check if they have a WAF.
    #   if yes, find some working tamper scripts using WhatWaf
    #   and finally, check if some parameters are vulnerable using
    #       sqlmap with the --smart and --batch functionalities
    # end of the line, gonna do this an other day


if __name__ == "__main__":
    main()
