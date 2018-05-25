# Adapted to the new save system
from autosqli import log
from autosqli.whatwaf_interface import whatwaf_target, set_whatwaf_path
from autosqli import save

import shutil
import tempfile
import threading
import time

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


class WhatWafScan():
    """ threaded class to scan a target """

    def __init__(self, target):
        self.NOT_LAUCHED_STATE = 0
        self.RUNNING_STATE = 1
        self.ENDED_STATE = 2

        self.state = self.NOT_LAUCHED_STATE
        self.target = target
        self.waffed_target = None
        self.thread = None
        self.launched = False

    def get_waffed_target(self):
        """ return the new target WhatWaf created if the scan ended
             , else return None
        """
        if self.state is self.ENDED_STATE:
            return self.results
        else:
            return None

    def _scan_thread_function(self):
        self.launched = True
        log.debug("Waffing {}".format(self.target.url))
        self.waffed_target = whatwaf_target(self.target)

    def start(self):
        """ scan a target in a new thread and save it in self.waffed_target """
        self.thread = threading.Thread(target=self._scan_thread_function)
        self.thread.start()
        self.state = self.RUNNING_STATE

    def update_status(self):
        """ set self.state to self.ENDED_STATE if self.launched and
        self.thread is dead
        """
        try:
            if self.launched and not self.thread.is_alive():
                self.state = self.ENDED_STATE
        except AttributeError:
            pass

    def save_target(self):
        """ update the target which resides in the save """
        save.update_target(self.waffed_target)

    def join(self):
        if self.state is self.ENDED_STATE:
            self.thread.join()

    def isEnded(self):
        return True if self.state is self.ENDED_STATE else False

    def isRunning(self):
        return True if self.state is self.RUNNING_STATE else False

    def gotStarted(self):
        return False if self.state is self.NOT_LAUCHED_STATE else True


def wafdetect_stage(args):
    """init whatwaf with custom tampers and add details to the targets of the
    save
    """
    set_whatwaf_path(init_whatwaf())

    targets_queue = []
    whatwafscan_queue = []

    # add all unwaffed targets to targets_queue
    for target in save.getTargets():
        if not target.isWaffed():
            if target is not None:
                targets_queue.append(target)

    # create a whatwafscan for every target and add them in whatwafscan_queue
    for target in targets_queue:
        log.debug('Adding {} to the target queue'.format(target.url))
        whatwafscan_queue.append(WhatWafScan(target))

    # constantly check the number of scans launched
    # if it is under 5, launch scan
    # also, check for ended scans. If there are, do scan.save_target(), and
    # remove() it from whatwafscan_queue
    # if there are no scans remaining, break.
    MINIMUM_RUNNING_SCANS = 5
    while True:
        # break if there are no scan remaining
        if len(whatwafscan_queue) == 0:
            break

        running_scans = 0
        for scan in whatwafscan_queue:
            # if the scan is finished, save and remove
            scan.update_status()
            if scan.isEnded():
                log.debug(
                    'Properly ending scan for {}'
                    .format(scan.target.url)
                )

                scan.save_target()
                whatwafscan_queue.remove(scan)

            # if the scan is running, increment running_scans
            if scan.isRunning():
                running_scans += 1

        # if there are not enough running scans, launch some
        to_launch = MINIMUM_RUNNING_SCANS - running_scans
        log.debug('Running scans: {}; Scans to launch: {}'.format(
            running_scans, to_launch
        ))

        for scan in whatwafscan_queue:
            if to_launch > 0:
                if not scan.gotStarted():
                    log.debug('Starting scan for {}'.format(scan.target.url))
                    scan.start()
                    to_launch -= 1
            else:
                break

        # check every 5 seconds
        time.sleep(5)

    # hello, code reader. If you like reading code, tell me in the issue
    # tracker !
