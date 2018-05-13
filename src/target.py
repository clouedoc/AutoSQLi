# From AutoSQLi

import uuid

REPORT_FORMAT = '-'*30 + """
Target: {}
    vulnerable  :   {}
    waf name    :   {}
    tampers     :   {}
""" + '-'*30


class Target:  # TODO: set proper getters and setters
    url = ""
    waf_detection_done = False
    is_protected_by_waf = False
    waf_name = ""
    working_tampers = []
    sqlmap_detection_done = False
    is_vulnerable = False
    sqlmap_logs = []

    def __init__(self, url):
        """ create a new Target from a url"""
        self.url = url
        self.uuid = uuid.uuid4()  # random UUID ( used to update in a list )

    def __str__(self):
        """ return the string representation of self """
        return REPORT_FORMAT.format(self.getUrl(), str(self.isVulnerable()),
                                    self.getWafName(), self.getTampers())

    def isVulnerable(self):
        return self.is_vulnerable

    def isSqlmapped(self):
        return self.sqlmap_exploitation_done

    def isWaffed(self):
        return self.waf_detection_done

    def getWafName(self):
        return self.waf_name

    def getUrl(self):
        return self.url

    def getTampers(self):
        return self.working_tampers


def urls_to_targets(urls):
    """ convert an url array to a Target array """
    target_list = []
    for url in urls:
        target_list.append(Target(url))

    return target_list
