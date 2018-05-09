from .execute import execute
from . import paths


WHATWAF_TIMEOUT = 60


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

def whatwaf_url(url):
    """ return WhatWaf's results for a specified url """
    return execute(["python2.7", paths.WHATWAF_NAME, "-u", url, "--ra",
                    "--hide"], paths.WHATWAF_PATH, WHATWAF_TIMEOUT)


def whatwaf_target(target):
    """ add whatwaf details to a target """
    # target
    whatwaf_report = whatwaf_url(target.url)
