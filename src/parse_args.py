# From AutoSQLi
import argparse


def argument_parse():
    parser = argparse.ArgumentParser(
            usage="python autosqli.py [-d DORK] [-f DORKFILE]",
            description="An automatic SQL Injection tool"
            )

    parser.add_argument("-f",
                        "--dork-file",
                        metavar="dorkfile.txt",
                        dest="dorkfile",
                        help="get your dorks from a file",
                        default=None,
                        )
    parser.add_argument("-d",
                        "--dork",
                        metavar="site:cn inurl:index.php?id=",
                        dest="dork",
                        help="specify an unique dork to be used",
                        default=None,
                        )
    parser.add_argument("-r",
                        "--resume",
                        action="store_true",
                        dest="resume",
                        help="resume from the save file (autosploit.save)",
                        )

    parser.add_argument("--debug",
                        action="store_true",
                        dest="debug",
                        help="activate the debug mode",
                        )

    return parser.parse_args()
