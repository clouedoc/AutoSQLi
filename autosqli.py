#!/usr/bin/env python3
import argparse

from src import log
from src import findDorks

def search_dork(dorks):
    return findDorks.dorkLines(dorks)

def argument_parse():
    parser = argparse.ArgumentParser(
            usage="python autosqli.py [-d DORK] [-f DORKFILE]",
            description="An automatic SQL Injection tool"
            )

    parser.add_argument("-f", "--dork-file", metavar="dorkfile.txt", dest="dorkfile", help="get your dorks from a file", default=None)
    parser.add_argument("-d", "--dork", metavar="site:cn inurl:index.php?id=", dest="dork", help="specify an unique dork to be used", default=None)
    return parser.parse_args()
    

def main():
    args = argument_parse()
    log.info("Welcome into AutoSQLi !")
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

    # search using findDorks.py ( which just search the dorks using google )
    urls_to_test = search_dork(dorks) 

    # now, we have a list of urls to test.
    # we gonna take all the urls one by one and check if they have a WAF.
    #   if yes, find some working tamper scripts using WhatWaf
    #   and finally, check if some parameters are vulnerable using sqlmap with the
    #       --smart and --batch functionalities
    # end of the line, gonna do this an other day

if __name__ == "__main__":
    main()
