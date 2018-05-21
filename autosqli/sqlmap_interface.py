# From AutoSQLi
# Most parts of this file were taken from here:
# https://github.com/Ekultek/Zeus-Scanner/blob/master/lib/attacks/sqlmap_scan/__init__.py
# Thanks to Ekultek (https://github.com/Ekultek) !

import json
import re
import requests
import psutil
import time
from multiprocessing import Process

from autosqli.execute import execute
from autosqli import log


def sqlmapapi_launch():
    """ launches sqlmapapi in another process and make sure it launched """

    def background():
        sta = execute(['python2.7', 'sqlmapapi.py', '-s'], 'sqlmap/', None,
                      None)

        if 'Address already in use' in sta:
            log.critical('sqlmapapi.py said: {}'.format(sta))

        if 'bash' in sta:
            log.critical('bash error: {}'.format(sta))

    p = Process(target=background)
    p.start()

    time.sleep(5)

    if not is_sqlmapapi_launched:
        log.critical("sqlmapapi.py couldn't be launched")


def is_sqlmapapi_launched():
    """ return True if sqlmapapi is launched, otherwise False """
    launched = False
    launched = 'sqlmapapi.py' in str({p.pid: p.info for p in
                                      psutil.process_iter(attrs=['cmdline'])})

    return launched


def sqlmapapi_check():
    """ verify if sqlmapi is launched, if not launch it """
    log.info("Checking if sqlmapapi is already launched")

    if not is_sqlmapapi_launched():
        log.info("Launching sqlmapapi")
        sqlmapapi_launch()


def sqlmap_url(url, options):
    """ return sqlmap results for a specific url and specified options """
    """ if there was an error, return None """
    # check if sqlmapapi is available
    sqlmapapi_check()

    # create the new api interface
    sqlmap = SqlmapHook(url)

    # init a new scan ( create it, but don't launch it )
    sqlmap.init_new_scan()

    scan_id = sqlmap.get_scan_id()
    log.debug("Launching a sqlmap scan for {} (id: {})".format(url, scan_id))
    log.debug("Options for {}: {}".format(url, options))
    sqlmap.start_scan(scan_id, options)

    while True:
        time.sleep(1)
        logs, running = sqlmap.show_sqlmap_log(scan_id)

        if not running:
            return logs

        time.sleep(4)


def parse_report(report, target):
    """ add sqlmap report details to a given target """
    log.debug("report: {}".format(report))
    if 'CRITICAL' in report:
        if 'all tested parameters do not appear to be injectable.' in report:
            # The detection process was error-free but didn't found a SQLi
            target.set_vulnerability_status(False)
        else:
            # There was an error that we are too lazy to handle
            target.set_vulnerability_status(False)
            target.set_sqlmap_error(True)
    else:
        log.critical("not finished yetttt :(")
        print('report:\n\n{}'.format(report))
        exit(69)

    target.set_sqlmap_logs(report)
    return target


def sqlmap_target(target, options):
    """ add sqlmap details to a Target and return it """
    report = sqlmap_url(target.getUrl(), options)
    if report is None:
        log.critical("There was an error while scanning {}".format(target.url))
        exit(1)  # just to be sure

    target = parse_report(report, target)
    # TODO: finish this :)
    return target


class SqlmapHook(object):

    """
    Sqlmap API hook, will process API requests, and output API data
    """

    def __init__(self, to_scan, port=None, api_con="http://127.0.0.1:{}",
                 default_port=8775):
        self.to_scan = to_scan
        self.port = port or default_port
        self.headers = {"Content-Type": "application/json"}
        self.connection = api_con.format(self.port)
        self.commands = {
            "init": "/task/new",
            "id": "/admin/0/list",
            "start": "/scan/{}/start",
            "status": "/scan/{}/status",
            "log": "/scan/{}/log"
        }

    def init_new_scan(self):
        """
        create a new API scan
        """
        new_scan_url = "{}{}".format(self.connection, self.commands["init"])
        try:
            results = requests.get(new_scan_url, params=self.headers)
            return results
        except Exception as e:
            log.critical("An error happenned in init_new_scan: {}".format(e))
            return None

    def get_scan_id(self, split_by=16):
        """
        get the ID of the current API scan
        """
        # current_scan_id = None
        id_re = re.compile(r"[a-fA-F0-9]{16}")
        api_id_url = "{}{}".format(self.connection, self.commands["id"])
        req = requests.get(api_id_url)
        to_check = str(json.loads(req.content)["tasks"]).lower()
        return ''.join(id_re.findall(to_check))

    def start_scan(self, api_id, opts=None):
        """
        start the API scan
        """
        start_scan_url = "{}{}".format(
            self.connection,
            self.commands["start"].format(api_id)
        )
        data_dict = {"url": self.to_scan}
        if opts is not None:
            for i in range(0, len(opts)):
                data_dict[opts[i][0]] = opts[i][1]
        post_data = json.dumps(data_dict)

        requests.post(
            start_scan_url,
            data=post_data,
            headers=self.headers
        )

    def show_sqlmap_log(self, api_id):
        """show the sqlmap log
        return a tuple like this: (logs, is_running)
        """

        running_status_url = "{}{}".format(
            self.connection,
            self.commands["status"].format(api_id)
        )

        running_log_url = "{}{}".format(
            self.connection,
            self.commands["log"].format(api_id)
        )

        status_req = requests.get(running_status_url)
        status_json = json.loads(status_req.content)
        current_status = status_json["status"]

        is_running = True
        logs = ''

        if current_status != "running":
            log.debug("[scan: {}] scan isn't running: {}".
                      format(api_id, current_status))
            is_running = False

        current_status = json.loads(
            requests.get(running_status_url).content
        )["status"]

        log_req = requests.get(running_log_url)
        log_json = json.loads(log_req.content)

        for i in range(0, len(log_json["log"])):
            logs += log_json["log"][i]["message"]

        return (logs, is_running)
