# From AutoSQLi

from . import log
import pickle

DORK_STAGE = 0          # getting urls from dork(s)
WAF_DETECT_STAGE = 1    # detecting targets protected by a WAF
WAF_TAMPER_STAGE = 2    # getting tampers for targets
SQLMAP_STAGE = 3        # sqlmapping targets
REPORT_STAGE = 4        # reporting vulnerable websites

class Save:
    targets_to_test = []
    stage = DORK_STAGE  # getting urls from dork(s)

    def exportSave(self, path):
        """ export this class object to a file  """
        """ specified in path                   """
        log.debug("exportSave called")
        log.debug("exportSave path: " + path)
        pickle.dump(self, open(path, "wb"))
        log.debug("dumped and written to " + path)

def importSave(path):
    log.debug("importSave called")
    log.debug("importSave path: " + path)
    return pickle.load(open(path, "r"))
