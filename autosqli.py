#!/usr/bin/env python3

from src import log             # provides log.info/debug/warning/critical
from src.parse_args import argument_parse  # provides argument_parse()
from src.save import Save           # provides Save() [class]
from src import stages
from src import checks
from src.dork_stage import dorkStage

current_save = Save()


def nextStage(args):
    """ execute the current stage out of current_save   """
    """ increase the stage number after it's execution  """
    global current_save

    if current_save.stage == stages.DORK_STAGE:     # if in dork stage
        dorkStage(args)               # launch the dork stage

    current_save.stage += 1
    return current_save.stage


def main():
    global current_save
    args = argument_parse()
    log.info("Welcome into AutoSQLi !")

    checks.saveChecks(args)         # checks if a save is present
    while True:
        # do the current stage and increment
        nextStage(args)
        # backup the current state (into autosqli.save)
        current_save.simpleExportSave()

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
