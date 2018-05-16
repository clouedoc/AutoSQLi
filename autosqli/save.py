# From AutoSQLi

from autosqli import stages
from autosqli import log

import pickle
from os.path import isfile

SAVE_PATH = 'autosqli.save'

# this is the default save
save = {'targets': [], 'stage': stages.DORK_STAGE}


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
    """ if no target is found, return None """
    for target in save['targets']:
        if not target.isWaffed():
            return target

    return None


def get_unsqlmapped_target():
    """ return a target which needs to be analyzed by sqlmap """
    """ if no target is found, return None """
    for target in save['targets']:
        if not target.isSqlmapped():
            return target

    return None


def update_target(target):
    """ update an already existing target """
    index = 0
    targetUuid = target.uuid
    for toModifyTarget in save['targets']:
        if targetUuid == toModifyTarget.uuid:
            save['targets'][index] = target
            return

        index += 1


def getTargets():
    """ return all targets from the save """
    return save['targets']


def get_vulnerable_targets():
    """ returns all vulnerable targets from the save """
    vulnerable_list = []
    for target in save['targets']:
        if target.isVulnerable():
            vulnerable_list.append(target)

    return vulnerable_list


def get_invulnerable_targets():
    """ returns all invulnerable targets from the save """
    invulnerable_list = []
    for target in save['targets']:
        if not target.isVulnerable():
            invulnerable_list.append(target)

    return invulnerable_list
