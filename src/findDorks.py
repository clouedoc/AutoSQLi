#!/usr/bin/env python3

# From jesuiscamille, and a part of the AutoSQLi project
# Not the best piece of code I ever made, but do the job pretty well
# I should do some adjustement on the ddgr and googler path thing
# you should see a dorkoutput.txt file sitting on your $(pwd)
# after running this :)
import subprocess
import json
import time

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
            try:
                result_clean = json.loads(result)
            except:
                google_ban = True
                print("Google may have banned us\
                      , but don't worry, it's temporary")
            for x in result_clean:
                url = x['url']
                writeToFile(url)
                results.append(url)

        if not duck_ban:
            print("   |__ ducky dorking...")
            result = duckSearch(dork)
            try:
                result_clean = json.loads(result)
            except:
                duck_ban = True
                print("DuckduckGo may have banned us, \
                      but don't worry, it's temporary")

            for x in result_clean:
                url = x['url']
                writeToFile(url)
                results.append(url)

        # waiting 15 seconds to not get caught
        print(" -- waiting 15 seconds --")
        time.sleep(15)

    print("check out ./dorkoutput.txt :3")
    print("Thx 4 d0rk1ng ! Have fun")
    return results


def execute(command):
    """ command shall be an array """
    """ returns the stdout of command """
    result = subprocess.run(command, stdout=subprocess.PIPE)
    return result.stdout.decode('utf-8')


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


def writeToFile(text):
    """ write text to dorkoutput.txt """
    output = open("dorkoutput.txt", 'a')
    output.write(text)
    output.write('\n')
    output.close()


if __name__ == "__main__":
    main()
