# From AutoSQLi
# Adapted to the new save system

from autosqli import save
from autosqli import log
from autosqli.dorkStage import dorkStage
from autosqli.wafDetectStage import wafDetectStage
from autosqli.reportStage import reportStage

DORK_STAGE = 0  # getting urls from dork(s)
WAF_DETECT_STAGE = 1  # detecting and tampering WAFs
SQLMAP_STAGE = 2  # sqlmapping targets
REPORT_STAGE = 3  # reporting vulnerable websites


def launchDorkStage(args):
    log.debug("Launching the dork stage")
    dorkStage(args)


def launchWafStage(args):
    log.debug("Launching the waf stage")
    wafDetectStage(args)


def launchSlmapStage(args):  # FIXME: implement this plz
    log.debug("Launching the sqlmap stage")
    pass


def launchReportStage(args):  # FIXME: implement this plz
    """ execute the report stage ( REPORT_STAGE ) """
    log.debug("Launching the report stage")
    reportStage(args)


def nextStage(args):
    """ execute the current stage of the save """
    """ increase the stage number after its execution """
    """ return True if it should be called another time """
    """ return False if it shouldn't be called another time """

    current_stage = save.getStage()

    if args.reportOnly:
        launchReportStage(args)
        return False
    elif args.dorkOnly:
        launchDorkStage(args)
        return False
    else:
        if current_stage == DORK_STAGE:  # if in dork stage
            launchDorkStage(args)
            return True
        elif current_stage == WAF_DETECT_STAGE:
            launchWafStage(args)
            return True
        elif current_stage == SQLMAP_STAGE:
            launchSlmapStage(args)
            return True
        elif current_stage == REPORT_STAGE:
            launchReportStage(args)
            return False
        else:
            launchReportStage(args)
            return False

        save.incrementStage()
        log.debug("New stage number: " + str(save.getStage()))
