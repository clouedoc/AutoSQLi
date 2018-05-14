# Adapted to the new save system
from autosqli import log
from autosqli.whatwaf_interface import whatwaf_target
from autosqli import save


def wafDetectStage(args):
    """ add details of the targets of the save """

    while True:
        target = save.getUnwaffedTarget()
        if target is not None:
            log.debug("Waffing {}".format(target.url))
            target = whatwaf_target(target)
            save.updateTarget(target)
        else:
            log.debug("All targets got waffed !")
            break
