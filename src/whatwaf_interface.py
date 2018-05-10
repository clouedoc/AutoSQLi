from .execute import execute
from . import paths
import json
from .strings import BANNED_TAMPERS


# this specifies the time that whatwaf is allowed to use to scan a target
# WHATWAF_TIMEOUT = 60


# def isProtectedByWaf(url):
# # """ run a rapid WhatWaf check to verify if a \
#    # target is protected by a WAF """
# # """ returns True if a protection is detected """
# # """ otherwise returns false """
# # whatwafResponse = execute(["python2.7",
#                           # paths.WHATWAF_NAME,
#                           # "-u", url, "--ra", "--hide",
#                           # "--skip"], paths.WHATWAF_PATH, WHATWAF_TIMEOUT)
#
# # if "no protection identified on target" in whatwafResponse:
#    # return False  # no protection

def satanize_url(url):
    """ satanize a url to be used with bash """
    return "'" + url.replace("'", "\\'")


def whatwaf_url(url):
    """ return WhatWaf's results for a specified url """
    return execute(["python2.7", paths.WHATWAF_NAME, "-u", satanize_url(url),
                    "--ra", "--hide"],
                   paths.WHATWAF_PATH, None, True)


def whatwaf_target(target):
    """ add whatwaf details to a target and returns it """

    whatwaf_report = whatwaf_url(target.url)
    if "no protection identified on target" in whatwaf_report:
        target.is_protected_by_waf = False
    elif '-'*30 in whatwaf_report:
        # extract the json part ( using those " - " )
        gorgeous_report = whatwaf_report.split('-'*30 + '\n')[1].split(
            '\n' + '-'*30)[0]

        # load the json
        json_report = json.loads(gorgeous_report)
        # assign the json to the target
        target.is_protected_by_waf = json_report["is protected"]
        target.waf_name = json_report["identified firewall"]
        for tamper in json_report["apparent working tampers"]:
            if tamper not in BANNED_TAMPERS:
                target.working_tamper.append(tamper)

    # TODO: analyze the report to return the target
    target.waf_detection_done = True
    return target
