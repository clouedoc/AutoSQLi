# From AutoSQLi
# Adapted to the new save system

from autosqli import save
from autosqli import log
from autosqli.dork_stage import dork_stage
from autosqli.wafdetect_stage import wafdetect_stage
from autosqli.report_stage import report_stage
from autosqli.sqlmap_stage import sqlmap_stage

DORK_STAGE = 0  # getting urls from dork(s)
WAF_DETECT_STAGE = 1  # detecting and tampering WAFs
SQLMAP_STAGE = 2  # sqlmapping targets
REPORT_STAGE = 3  # reporting vulnerable websites


def launchDorkStage(args):
    log.debug("Launching the dork stage")
    dork_stage(args)


def launchWafStage(args):
    log.debug("Launching the waf stage")
    wafdetect_stage(args)


def launchSqlmapStage(args):
    log.debug("Launching the sqlmap stage")
    sqlmap_stage(args)


def launchReportStage(args):
    """ execute the report stage ( REPORT_STAGE ) """
    log.debug("Launching the report stage")
    report_stage(args)


def nextStage(args):
    """ execute the current stage of the save
    increase the stage number after its execution
    return True if it should be called another time
    return False if it shouldn't be called another time
    """

    current_stage = save.getStage()

    if args.reportOnly:
        launchReportStage(args)
        return_value = False
    elif args.dorkOnly:
        launchDorkStage(args)
        return_value = False
        # since we got target data, we can increment the stage for future use
        if save.getStage() == DORK_STAGE:
            save.incrementStage()
    else:
        if current_stage == DORK_STAGE:  # if in dork stage
            launchDorkStage(args)
            return_value = True
        elif current_stage == WAF_DETECT_STAGE:
            launchWafStage(args)
            return_value = True
        elif current_stage == SQLMAP_STAGE:
            launchSqlmapStage(args)
            return_value = True
        elif current_stage == REPORT_STAGE:
            launchReportStage(args)
            return_value = False
        else:
            launchReportStage(args)
            return_value = False

        save.incrementStage()
        log.debug("New stage number: " + str(save.getStage()))

    return return_value
