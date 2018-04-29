# From AutoSQLi

from . import log
from . import stages

import pickle


class Save:
    targets_to_test = []
    stage = stages.DORK_STAGE  # getting urls from dork(s)

    def exportSave(self, path):
        """ export this class object to a file  """
        """ specified in path                   """
        log.debug("exportSave called")
        log.debug("exportSave path: " + path)
        pickle.dump(self, open(path, "wb"))
        log.debug("dumped and written to " + path)

    def simpleExportSave(self):
        """ same function as exportSave but uses "autosqli.save" as   """
        """ the default path                                            """
        self.exportSave("autosqli.save")


def importSave(path):
    log.debug("importSave called")
    log.debug("importSave path: " + path)
    return pickle.load(open(path, "r"))
