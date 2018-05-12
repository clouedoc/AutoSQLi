# From AutoSQLi

# from . import log
from . import stages
from . import log

import pickle
from os.path import isfile

SAVE_PATH = 'autosqli.save'

# this is the default save
save = {
    'targets': [],
    'stage': stages.DORK_STAGE
}


def writeSave():
    """ write in picle format the storage var """
    with open(SAVE_PATH, 'wb') as f:
        pickle.dump(save, f, pickle.HIGHEST_PROTOCOL)


def importSave():
    """ write autosqli.save to the current global save dict """
    global save

    with open(SAVE_PATH, 'rb') as f:
        save = pickle.load(f)


def addTarget(target):
    """ add a target to the current global save """
    global save

    save['targets'].append(target)


def removeTarget(target):
    """ remove a target of the current global save """
    global save

    save['targets'].remove(target)


def setStage(stage):
    """ set the current stage of the current global save """
    global save
    save['stage'] = stage


def incrementStage():
    """ increment the current stage of the current global save """
    global save
    save['stage'] += 1


def getStage():
    """ returns the current stage of the save """
    return save['stage']


def saveStartup(args):
    """ if no save is detected, create a new one """
    """ if -r is used, load from save """
    """ else, ask user to confirm they want to erase their save """
    if not isfile(SAVE_PATH):
        log.warning("It seems that there is no save here. Creating one.")
        writeSave()
    elif args.resume:
        log.info("Resuming from save (-r)...")
        importSave()
        log.info("Save imported !")
    else:
        log.warning("It seems there is a save here. Turn on -r to use it.")
        input("Press enter to continue ( this will erase your save ).")
        writeSave()


def getUnwaffedTarget():
    """ return a target which needs to be analyzed by WhatWaf """
    for target in save['targets']:
        if not target.waf_detection_done:
            return target


def updateTarget(target):
    """ update an already existing target """
    index = 0
    targetUuid = target.uuid
    for toModifyTarget in save['targets']:
        if targetUuid == toModifyTarget.uuid:
            save['targets'][index] = target
            return

        index += 1
