#!/usr/bin/env python3
import os.path
from time import sleep

from src import log             # provides log.info/debug/warning/critical
from src import findDorks       # provides findDorks.dorkLines(dorks)
from src.parse_args import argument_parse # provides argument_parse()
from src.save import Save       # provides Save() [class]
from src.save import importSave # provides importSave(path)

autosploit_save = Save()

def search_dork(dorks):
    return findDorks.dorkLines(dorks)

def main():
    args = argument_parse()
    log.info("Welcome into AutoSQLi !")

    # checking if -r is used ( to resume from autosploit.save )
    if args.resume == True: # if the user wants to resume
        log.info("Using the previously created save...")
        # check if there is a save file
        if os.path.isfile("autosploit.save") == True:
            importSave("autosploit.save")
        else:
            log.critical("The save file doesn't exists ! (autosploit.save)")
            exit(3) # save file error
    elif os.path.isfile("autosploit.save") == True: # if a save exists
            log.warning("There is a save file in this directory")
            log.warning("If you don't quit now, this file will be erased !")
            log.warning("use -r to resume")
            log.info("waiting 10 seconds for user input")
            sleep(10)
    else:
        log.info("A save file will be created (autosploit.save)")

    if args.dorkfile != None and args.dork != None:
        log.critical("-f (--dork-file) and -d (--dork) are incompatible")
        exit(1)
    elif args.dorkfile != None:
        exit(2) # not implemented
        pass # TODO: accept a dorkfile
    elif args.dorkfile == None and args.dork == None:
        log.debug("interactively querying dork")
        log.info("Enter a dork:")
        dorks = [input("dork: ")]
    else:
        dorks = [args.dork]

    ###### END OF ARGUMENT PARSING #######

    # search using findDorks.py ( which just search the dorks using google )
    urls_to_test = search_dork(dorks) 

    # TODO:
    # convert urls_to_test into some targets
    # save the targets

    # WTF TODO:
    # now, we have a list of urls to test.
    # we gonna take all the urls one by one and check if they have a WAF.
    #   if yes, find some working tamper scripts using WhatWaf
    #   and finally, check if some parameters are vulnerable using sqlmap with the
    #       --smart and --batch functionalities
    # end of the line, gonna do this an other day

if __name__ == "__main__":
    main()
