# Adapted to the new save system
from . import log
from .whatwaf_interface import whatwaf_target
from . import save


def wafDetectStage(args):
    """ add details of the targets of the save """
    log.warning("waf_detect_stage: see the comment inside the py file plz")

    while True:
        target = save.getUnwaffedTarget()
        log.debug("Waffing {}".format(target.url))
        target = whatwaf_target(target)
        save.updateTarget(target)
