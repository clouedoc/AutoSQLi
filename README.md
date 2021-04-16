# AutoSQLi, **the new way script-kiddies hack websites**

## Features

-   Save System
    		\- there is a complete save system, which can resume even when your pc crashed.
    		\- technology is cool
-   Dorking
    		\- from the command line ( one dork ): YES
    		\- from a file: NO
    		\- from an interactive wizard: YES
-   Waffing
    		\- Thanks to [Ekultek](https://github.com/Ekultek), WhatWaf now has a JSON output function.
    		\- So it's mostly finished :)
    		\- UPDATE: WhatWaf is completly working with AutoSQLi. Sqlmap is the next big step
-   Sqlmapping
    		\- I'll look if there is some sort of sqlmap API, because I don't wanna use `execute` this time (:
    		\- Sqlmap is cool
-   REPORTING: YES
-   Rest API: NOPE

## TODO:

-   [ ] Log handling (logging with different levels, cleanly)
-   [ ] Translate output (option to translate the save, which is in pickle format, to a json/csv save)
-   [ ] Spellcheck (correct wrongly spelled words and conjugational errors. I'm on Neovim right now and there is no auto-spelling check)

## The Plan

This plan is a bit outdated, but it will follow this idea

1.  AutoSQLi will be a python application which will, automatically, using a dork provided by the user, return a list of websites vulnerable to a SQL injection.
2.  To find vulnerable websites, the users firstly provide a dork [DOrking](https://www.techopedia.com/definition/30938/google-dorking), which is passed to findDorks.py, which returns a list of URLs corresponding to it.
3.  Then, AutoSQLi will do some very basic checks ( TODO: MAYBE USING SQLMAP AND IT's --smart and --batch function ) to verify if the application is protected by a Waf, or if one of it's parameters is vulnerable.
4.  Sometimes, websites are protected by a Web Application Firewall, or in short, a WAF. To identify and get around of these WAFs, AutoSQLi will use WhatWaf.
5.  Finally, AutoSQLi will exploit the website using sqlmap, and give the choice to do whatever he wants !

### Tor

Also, AutoSQLi should work using Tor by default. So it should check for tor availiability on startup.

## FAQ

### Cool :)

Thanks

### It looks like SQLiDumper, no ?

Yeah, I know.

## Don't mess up

This project is for demonstration purposes. Nobody should ever run AutoSQLi. Really.
Hacking into DB's is fun, but you know, there are guys just like you and me who don't want to get their entire work messed up. You don't to make them pull out their hairs, ya?
