# From AutoSQLi

import uuid
import os

REPORT_FORMAT = '-' * 30 + """
Target: {}
    vulnerable  :   {}
    waf name    :   {}
    tampers     :   {}
""" + '-' * 30


class Target:
    url = ""
    waf_detection_done = False
    whatwaf_report = None
    is_protected_by_waf = False
    waf_name = ""
    working_tampers = []
    sqlmap_detection_done = False
    vulnerable = False
    sqlmap_logs = ''
    connection_error = False
    sqlmap_bug = False
    sqlmap_error = False

    def __init__(self, url):
        """ create a new Target from a url"""
        self.url = url
        self.uuid = uuid.uuid4()  # random UUID ( used to update in a list )

    def __str__(self):
        """ return the string representation of self """
        return REPORT_FORMAT.format(self.getUrl(), str(self.isVulnerable()),
                                    self.getWafName(), self.getTampers())

    def isVulnerable(self):
        return self.vulnerable

    def isSqlmapped(self):
        return self.sqlmap_detection_done

    def isWaffed(self):
        return self.waf_detection_done

    def getWafName(self):
        return self.waf_name

    def getUrl(self):
        return self.url

    def getTampers(self):
        return self.working_tampers

    def get_tampers_paths(self):
        """ return complete uri ( python file path ) of self.working_tampers"""
        uri_of_tampers = []
        for tamper in self.working_tampers:
            uri_of_tampers.append(os.path.abspath(
                'WhatWaf/'
                + self.working_tampers
                + '.py')
            )

        return uri_of_tampers

    def set_connection_error(self, error):
        self.connection_error = error

    def set_sqlmap_bug(self, bug):
        self.sqlmap_bug = bug

    def set_vulnerability_status(self, status):
        self.vulnerable = status

    def set_sqlmap_logs(self, logs):
        self.sqlmap_logs = logs

    def set_sqlmap_error(self, error):
        self.sqlmap_error = error


def urls_to_targets(urls):
    """ convert an url array to a Target array """
    target_list = []
    for url in urls:
        target_list.append(Target(url))

    return target_list
