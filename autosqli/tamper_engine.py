# From AutoSQLi
from autosqli import sqlmap_options


def get_options_for_target(target):
    """ return a customized set of sqlmap options for a target ( tampers ) """

    # FIXME: to debug :)
    tampers = target.get_tampers_paths()
    options = sqlmap_options.BASE_SQLMAP_OPTIONS
    import pudb; pudb.set_trace()  # XXX BREAKPOINT

    # add all the tampers in tampers to a string: tampers_string
    # format: tamper1,tamper2,tamper3
    tampers_string = ''
    for tamper in tampers:
        tampers.remove(tamper)
        tampers_string.append("{}{}".format(
            tampers,
            ',' if len(tampers == 0) else None
            )
        )

    options['tamper'] = tampers_string

    return options
