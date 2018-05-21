# From AutoSQLi

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
