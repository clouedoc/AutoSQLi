# From AutoSQLi

# from . import log
# from . import stages

import ZODB, ZODB.FileStorage
import transaction

# import pickle


# choisi le fichier de sauvegarde
storage = ZODB.FileStorage.FileStorage('autosqli.save')
# crée un objet db
db = ZODB.DB(storage)
# crée une connexion à la bdd
connection = db.open()
# associe un objet à cette connexion
save = connection.root
# sauve cet objet et tout ses attributs
transaction.commit()

# def importSave(path):
#     """ return a Save from a pickle dump of a Save instance """
#     log.debug("importSave called")
#     log.debug("importSave path: " + path)
#     return pickle.load(open(path, "rb"))

#  # def importSave(path):
#      # """ return a Save from a pickle dump of a Save instance """
#      # log.debug("importSave called")
#      # log.debug("importSave path: " + path)
#      # return pickle.load(open(path, "rb"))


#  class Save(persistent.Persistent):
#      targets_to_test = []
#      stage = stages.DORK_STAGE  # getting urls from dork(s)
#
#  #    # def __init__(self):
#  #        # self.targets_to_test = []
#  #        # self.stage = stages.DORK_STAGE  # getting urls from dork(s)
#
#      def exportSave(self, path):
#          """ export this class object to a file  """
#          """ specified in path                   """
#          log.debug("exportSave called")
#          log.debug("exportSave path: " + path)
#          pickle.dump(self, open(path, "wb"))
#          log.debug("dumped and written to " + path)
#
#      def simpleExportSave(self):
#          """ same function as exportSave but uses "autosqli.save" as   """
#          """ the default path                                            """
#          self.exportSave("autosqli.save")


# here is defined the global save of the program.
# current_save = Save()

