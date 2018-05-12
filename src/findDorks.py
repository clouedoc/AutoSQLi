#!/usr/bin/env python3
# Adapted to the new save system

# Ugly code I now.

import json
import time
from .execute import execute
from . import save
from .target import Target

# here is the path thing
ddgr_path = "ddgr/ddgr"
googler_path = "googler/googler"


def main():
    filename = input("Enter your dork file name: ")
    print("Reading " + filename + " ...")
    # filename = "testdorks.txt"
    dorkFromFile(filename)


def dorkFromFile(filename):
    f = open(filename, 'r')
    lines = f.readlines()   # read all the lines of the file into 'lines'
    f.close()
    dorkLines(lines)


def dorkLines(lines):
    # remove annoying trailing characters
    google_ban = False
    duck_ban = False

    index = 0
    for i in lines:
        lines[index] = lines[index].rstrip()
        index += 1

    results = []
    result_clean = []
    # dorking !
    for dork in lines:
        if google_ban is True and duck_ban is True:
            break

        print(" |__ dork: " + dork)
        # dorking with google and writing to file
        if not google_ban:
            print("   |__ googly dorking...")
            result = googleSearch(dork)

            # TODO: google ban handling
            result_clean = json.loads(result)
#            # try:
#                # result_clean = json.loads(result)
#            # except:
#                # google_ban = True
#                # print("Google may have banned us\
#                      # , but don't worry, it's temporary")

            for x in result_clean:
                # url = x['url']
                save.addTarget(Target(x['url']))

        if not duck_ban:
            print("   |__ ducky dorking...")
            result = duckSearch(dork)
            result_clean = json.loads(result)

#            # TODO: ducky ban handling
#            # try:
#                # result_clean = json.loads(result)
#            # except:
#                # duck_ban = True
#                # print("DuckduckGo may have banned us, \
#                      # but don't worry, it's temporary")

            for x in result_clean:
                # url = x['url']
                save.addTarget(Target(x['url']))

        # waiting 15 seconds to not get caught
        print(" -- waiting 15 seconds --")
        time.sleep(15)

    print("check out ./dorkoutput.txt :3")
    print("Thx 4 d0rk1ng ! Have fun")
    return results


def googleSearch(dork):
    """ dork shall be a string which contains... a dork. """
    """ returns the google json response for the specified dork """
    return execute([googler_path, "-n", "100", dork, "--noprompt", "--json"])


def duckSearch(dork):
    """ dork shall be a string which contains... a dork. """
    """ returns the duckduckgo json response for the specified dork """
    return execute([ddgr_path,
                    dork,
                    "--unsafe", "--json", "--np", "--num", "25"])


if __name__ == "__main__":
    main()
