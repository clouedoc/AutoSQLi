# From AutoSQLi
# Adapted to the new save system

from . import save
from . import log
from . import dorkStage
from . import wafDetectStage

DORK_STAGE = 0          # getting urls from dork(s)
WAF_DETECT_STAGE = 1    # detecting and tampering WAFs
SQLMAP_STAGE = 2        # sqlmapping targets
REPORT_STAGE = 3        # reporting vulnerable websites


def nextStage(args):
    """ execute the current stage of the save """
    """ increase the stage number after its execution """

    current_stage = save.getStage()

    if current_stage == DORK_STAGE:     # if in dork stage
        log.debug("Launching the dork stage")
        dorkStage.dorkStage(args)

    if current_stage == WAF_DETECT_STAGE:
        log.debug("Launching the waf stage")
        wafDetectStage.wafDetectStage(args)

    if current_stage == SQLMAP_STAGE:
        log.debug("Launching the sqlmap stage")
        pass  # TODO: call the sqlmap stage

    save.incrementStage()
    log.debug("New stage number: " + str(save.getStage()))
