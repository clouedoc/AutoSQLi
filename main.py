#!/usr/bin/env python3
import argparse

from src import log
from src import findDorks

def search_dork(dork):
    return findDorks.dorkLines(([dork]))

def define_arguments():
    parser = argparse.ArgumentParser(
            usage="python autosqli.py [-d DORK] [-f DORKFILE]"
            )
    f = parser.add_argument_group("Files", "parameters relative to file manipulation")

    f.add_argument("-f", "--dork-file", metavar="dorkfile.txt", dest=dorkfile, help="if you already dorked, set a file where your dorks are contained ( one dork per line )")

def main():
    log.info("Welcome into AutoSQLi !")
    log.info("Enter a dork:")
    dork = input("dork: ")
    url_to_test = search_dork(dork)

if __name__ == "__main__":
    main()
