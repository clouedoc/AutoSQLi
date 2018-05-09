from . import log
from .whatwaf_interface import whatwaf_target


def wafDetectStage(targets):
    """ take an array of targets and associate WhatWaf properties with them """
    waffed_targets = []

    for target in targets:
        log.debug("Waffing {}".format(target.url))
        target = whatwaf_target(target)
        waffed_targets.append(target)

    return waffed_targets
