# From AutoSQLi
from autosqli import save
from autosqli import sqlmap_interface
from autosqli import log

BASE_SQLMAP_OPTIONS = {
    # Stealthization
    'random_agent': True,

    # Optimization
    'keep_alive': True,
    'threads': 4,

    # Injection
    'risk': 2,  # Setted risk to two because we are risky peoples.
    'text-only': True,  # Comparing with images is weird and takes bandwitch.

    # Technique
    'time-sec': 15,  # Setted time-sec to 15 to avoid latency problems

    # General
    'batch': True,
    'output-dir': 'sqlmap_results',
    'tamper': '',  # Is modified with get_options_for_target
    'forms': True,

    # Misc
    'skip-waf': True,
    'beep': True,  # Beeps if an injection is found
    'smart': True,  # This flag aborts the scan is results are negatives
}


def get_options_for_target(target):
    """ return a customized set of sqlmap options for a target ( tampers ) """
    # FIXME: to debug :)
    tampers_string = ''
    tampers = target.get_tampers_paths()
    options = BASE_SQLMAP_OPTIONS

    for tamper in tampers:
        tampers.remove(tamper)
        tampers_string.append("{}{}".format(
            tampers,
            ',' if len(tampers == 0)
        ))


    options['tamper'] = tampers_string

    return options


def sqlmap_stage(args):
    """ do a sqlmap scan on all the targets """

    while True:
        target = save.get_unsqlmapped_target()

        if target is None:
            break
        else:
            sqlmapped_target = sqlmap_interface.\
                sqlmap_target(target, get_options_for_target(target))

            save.update_target(sqlmapped_target)
