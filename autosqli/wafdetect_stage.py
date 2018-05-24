# Adapted to the new save system
from autosqli import log
from autosqli.whatwaf_interface import whatwaf_target, set_whatwaf_path
from autosqli import save

import shutil
import tempfile

WHITELISTED_TAMPERS_PATH = './tampers/whitelisted'


def init_whatwaf():
    """copy WhatWaf in a tmp dir with tampers in ./tampers/whitelisted/*
    and returns WhatWaf's new path
    """
    log.debug("Initializing WhatWaf")

    # create a temporary directory
    tmp_dir = tempfile.mkdtemp()
    # always have a / at the end
    tmp_dir = tmp_dir + '/' if tmp_dir[-1] != '/' else ''
    tmp_whatwaf_dir = tmp_dir + 'WhatWaf/'
    log.debug("Tmp dir: {}".format(tmp_dir))

    # copy ./WhatWaf to the temp directory ( without the tampers )
    shutil.copytree('./WhatWaf', tmp_whatwaf_dir)
    # remove the `content/tampers` dir
    shutil.rmtree(tmp_whatwaf_dir + 'content/tampers/')
    # copy the tampers
    shutil.copytree(
        WHITELISTED_TAMPERS_PATH,
        tmp_whatwaf_dir + 'content/tampers/'
    )

    log.debug('tmp WhatWaf dir: {}'.format(tmp_whatwaf_dir))
    return tmp_whatwaf_dir


def wafdetect_stage(args):
    """init whatwaf with custom tampers and add details to the targets of the
    save
    """
    set_whatwaf_path(
        init_whatwaf()
    )

    while True:
        target = save.getUnwaffedTarget()
        if target is not None:
            log.debug("Waffing {}".format(target.url))
            target = whatwaf_target(target)
            save.updateTarget(target)
        else:
            log.debug("All targets got waffed !")
            break


print(init_whatwaf())
