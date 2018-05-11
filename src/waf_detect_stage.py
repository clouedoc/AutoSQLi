from . import log
from .whatwaf_interface import whatwaf_target
from .save import current_save

global current_save

# FIXME: I dunno if those two lines that are commented on the top are
# necessaries to edit the global save. Huum.
# I think we'll se this at debug time


def wafDetectStage(args):
    """ take an array of targets and associate WhatWaf properties with them """
    global current_save
    import pdb; pdb.set_trace()  # XXX BREAKPOINT
    log.warning("waf_detect_stage: see the comment inside the py file plz")

    index = 0
    for target in current_save.targets_to_test:
        log.debug("Waffing {}".format(target.url))
        target = whatwaf_target(target)
        current_save.targets_to_test[index] = target
        index += 1
