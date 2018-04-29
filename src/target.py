# From AutoSQLi

class Target:
    url = ""
    waf_detection_done = False
    is_protected_by_waf = False
    working_tampers = []
    sqlmap_exploitation_done = False
    is_vulnerable = False
    def __init__(self, url):
        """ create a new Target """
        self.url = url
