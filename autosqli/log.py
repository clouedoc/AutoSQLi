# From AutoSQLi

from autosqli import colors

DEBUG_PREFIX = colors.OKBLUE + "[DEBUG] "
ERROR_PREFIX = colors.FAIL + "[ERROR] "
INFO_PREFIX = colors.OKBLUE + colors.BOLD + "[INFO] "
CRITICAL_PREFIX = colors.FAIL + colors.UNDERLINE + colors.BOLD + "[CRITICAL] "
WARNING_PREFIX = colors.FAIL + colors.BOLD + "[WARNING] "


def debug(msg):
    print(DEBUG_PREFIX + str(msg) + colors.ENDC)


def info(msg):
    print(INFO_PREFIX + str(msg) + colors.ENDC)


def error(msg):
    print(ERROR_PREFIX + str(msg) + colors.ENDC)


def critical(msg):
    print(CRITICAL_PREFIX + str(msg) + colors.ENDC)


def warning(msg):
    print(WARNING_PREFIX + str(msg) + colors.ENDC)
