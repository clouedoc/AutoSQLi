import json

from . import paths
from . import log

from .strings import BANNED_TAMPERS
from .satanize import remove_thing_url
from .execute import execute
from .consts import WHATWAF_VERIFY_NUM
from .consts import WHATWAF_DEBUG, WHATWAF_DEBUG_REPORT


def whatwaf_url(url):
    """ return WhatWaf's results for a specified url """
    log.debug("Launching WhatWaf on {}".format(url))
    return execute([
        "python2.7", paths.WHATWAF_NAME, "-u",
        remove_thing_url(url), "--ra", "--hide", "--json", "--verify-num",
        str(WHATWAF_VERIFY_NUM)
    ], paths.WHATWAF_PATH, None, True)


def whatwaf_target(target):
    """ add whatwaf details to a target and returns it """

    # if WHATWAF_DEBUG is True, use the sample WhatWaf report (from consts.py)
    if WHATWAF_DEBUG:
        log.warning("WhatWaf debug mode is on. To disable, " +
                    "check src/target.py ! ( WHATWAF_DEBUG )")

    whatwaf_report = WHATWAF_DEBUG_REPORT if WHATWAF_DEBUG else \
        whatwaf_url(target.url)

    if "no protection identified on target" in whatwaf_report:
        target.is_protected_by_waf = False
    elif '-' * 30 in whatwaf_report:
        # extract the json part ( using those " - " )
        gorgeous_report = whatwaf_report.split('-' * 30 + '\n')[1].split(
            '\n' + '-' * 30)[0]

        # load the json
        json_report = json.loads(gorgeous_report)
        # assign the json to the target
        target.is_protected_by_waf = json_report["is protected"]
        target.waf_name = json_report["identified firewall"]
        tampers = json_report["apparent working tampers"] if \
            json_report["apparent working tampers"] is not None else []
        for tamper in tampers:
            if tamper not in BANNED_TAMPERS:
                target.working_tamper.append(tamper)

    # TODO: analyze the report to return the target
    target.waf_detection_done = True
    return target
