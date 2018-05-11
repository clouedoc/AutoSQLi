# From AutoSQLi


def satanize_for_bash(toSatanize):
    """ satanize a string to be used with bash """
    return "'" + toSatanize.replace("'", "\\'") + "'"


def remove_thing_url(url):
    return url.replace("'", "\\'")
