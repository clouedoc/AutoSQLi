# AutoSQLi, **the new way script-kiddies hack websites**

(that's a joke :p)

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

Yeah, I know.

### It looks like SQLiDumper, no ?

Yeah, I know.

## Popularity note ( 2018-05-10 )

When I woke up this morning, someone said that a guy by the name of NullArray tweeted about this project. 11 stars later, it makes me want to finish it more than ever !

## Contribution Note

Friday, the 11th of May, the first pull request of this project was sent by [@iyanuashiri](https://github.com/iyanuashiri).

## sTaTiStIcS

### 2018-05-11

Today, we are at 15 stars, and got our first pull request. The number of cloners and unique viewers is decreasing with the time, but I noticed that someone followed a link from `web.telegram.org`. Well, those referer statistics are cool.
I also finished implementing WhatWaf :)

### 2018-05-12

As of today, there is 21 stargazers. In fact there is only 4 unique cloners, so I'm wondering if the peoples who stars this repo aren't compulsive-stargazers. NO OFFENSES MEANT :), please, put a star on this repo, I like it.
The save system got completly modified, because the old one was pretty random.
The code now have debugging facilities ( a --debug switch ).
It can dork and automatically WAF websites.
That's all.
Damn, creating a piece of glue is quite hard :)

### 2018-05-13

We're at 22 stars, cause I starred my own repo. That's strange, the star haze seems to go down, end I'm pretty sure the first working version will be out in one or two weeks

Also, today, I was at the point of buying a HackRF One ( you know, these cards which can transmit on pretty all radio frequencies that are and were used by electronic things ).
The fact is I only have 100€ right now, and the HackRF One costs 300€. Ya.
I think I'll wait. ~please buy me a HackRF One :)~

# Disclaimer ( because you know, every InfoSec projects should have one )

## Don't mess up

This project is for demonstration purposes. Nobody should ever run AutoSQLi. Really.
Hacking into DB's is fun, but you know, there are guys just like you and me who don't want to get their entire work messed up. You don't to make them pull out their hairs, ya?
