# From AutoSQLi
# Most parts of this file where took from here:
# https://github.com/Ekultek/Zeus-Scanner/blob/master/lib/attacks/sqlmap_scan/__init__.py
# Thanks to Ekultek (https://github.com/Ekultek) !

import json
import re
import requests
import psutil
from multiprocessing import Process

from autosqli.execute import execute
from autosqli import log


def sqlmapapi_launch():
    """ launches sqlmapapi in another process """

    def background():
        sta = execute(['python2.7', 'sqlmapapi.py', '-s'], 'sqlmap/', None,
                      None)

        if 'Address already in use' in sta:
            log.critical('sqlmapapi.py said: {}'.format(sta))

        if 'bash' in sta:
            log.critical('bash error: {}'.format(sta))

    p = Process(target=background)
    p.start()


def sqlmapapi_check():
    """ verify if sqlmapi is launched, if not launch it """
    log.info("Checking if sqlmapapi is already launched")

    launched = False
    launched = 'sqlmapapi.py' in str({p.pid: p.info for p in
                                      psutil.process_iter(attrs=['cmdline'])})
    if not launched:
        log.info("Launching sqlmapapi")
        sqlmapapi_launch()


def sqlmap_url(url, options):
    """ return sqlmap results for a specific url and specified options """
    # check if sqlmapapi is available
    sqlmapapi_check()

    # create the new api interface
    sqlmap = SqlmapHook(url)

    # init a new scan ( create it, but don't launch it )
    sqlmap.init_new_scan()

    scan_id = sqlmap.get_scan_id()
    log.debug("Launching a sqlmap scan for {} (id: {})".format(url, scan_id))
    sqlmap.start_scan(scan_id, options)
    # TODO: wait for scan to finish
    pass  # FIXME: not done


def sqlmap_target(target):
    """ add sqlmap details to a Target """
    report = sqlmap_url(target.url)
    log.debug("report: {}".format(report))
    pass


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
        return requests.get(new_scan_url, params=self.headers)

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
        # req = urllib2.Request(
        #     start_scan_url,
        #     data=post_data,
        #     headers=self.headers
        # )
        requests.post(
            start_scan_url,
            data=post_data,
            headers=self.headers
        )

    def show_sqlmap_log(self, api_id):
        """
        show the sqlmap log during the API scan
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
        if current_status != "running":
            log.critical(
                "sqlmap API failed to start the run, check the client and see "
                "what the problem is and try again"
            )
        already_displayed = set()
        while current_status == "running":
            # while the current status evaluates to `running`
            # we can load the JSON data and output the log information
            # we will skip over information that has already been provided
            # by using the already displayed container set.
            # this will allow us to only output information that we
            # have not seen yet.
            current_status = json.loads(
                requests.get(running_status_url).content
            )["status"]
            log_req = requests.get(running_log_url)
            log_json = json.loads(log_req.content)
            for i in range(0, len(log_json["log"])):
                if log_json["log"][i]["message"] in already_displayed:
                    pass
                else:
                    print(
                        "sqlmap> [{} {}] {}".format(
                            log_json["log"][i]["time"],
                            log_json["log"][i]["level"],
                            log_json["log"][i]["message"]
                        )
                    )
                already_displayed.add(log_json["log"][i]["message"])
