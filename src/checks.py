from . import log
import os
import os.path
from time import sleep
from src.save import importSave     # provides importSave(path)


def saveChecks(args):
    # checking if -r is used ( to resume from autosqli.save )
    if args.resume is True:  # if the user wants to resume
        log.info("Using the previously created save...")
        # check if there is a save file
        if os.path.isfile("autosqli.save") is True:
            importSave("autosqli.save")
        else:
            log.critical("The save file doesn't exists ! (autosqli.save)")
            exit(3)     # save file error
    elif os.path.isfile("autosqli.save") is True:     # if a save exists
            log.warning("There is a save file in this directory")
            log.warning("If you don't quit now, this file will be erased !")
            log.warning("use -r to resume")
            log.info("waiting 10 seconds for user input")
            sleep(10)
    else:
        log.info("A save file will be created (autosqli.save)")
