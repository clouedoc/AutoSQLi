# AutoSQLi

## What is working right now

- Dorking
	- from the command line ( one dork ): YES
	- from a file: NO
	- from an interactive wizard: YES
- Waffing
	- Thanks to Eku, WhatWaf now has a JSON output function.
	- So it's mostly finished :)
	- UPDATE: WhatWaf is completly working with AutoSQLi. Sqlmap is the next big step
- Sqlmapping
	- I'll look if there is some sort of sqlmap API, because I don't wanna use `execute` this time (:
	- Sqlmap is cool
- Rest: NOPE

## TODO:

Could someone add a proper handling of the log? I mean, logging with different levels, cleanly ^^ ?
Also, could someone add an option to translate the save ( which is in pickle format ) to a json/csv save ?
Thanks :)

## The Plan

This plan is a bit outdated, but it will follow this idea

AutoSQLi will be a python application which will, automatically, using a dork provided by the user, return a list of websites vulnerable to a SQL injection.
To find vulnerable websites, the users firstly provide a dork [DOrking]( https://www.techopedia.com/definition/30938/google-dorking), which is passed to findDorks.py, which returns a list of URLs corresponding to it.
Then, AutoSQLi will do some very basic checks ( TODO: MAYBE USING SQLMAP AND IT's --smart and --batch function ) to verify if the application is protected by a Waf, or if one of it's parameters is vulnerable.
Sometimes, websites are protected by a Web Application Firewall, or in short, a WAF. To identify and get around of these WAFs, AutoSQLi will use WhatWaf.

Finally, AutoSQLi will exploit the website using sqlmap, and give the choice to do whatever he wants !

## Tor

Also, AutoSQLi should work using Tor by default. So it should check for tor availiability on startup.

## FAQ
### Cool :)

Yeah, I know.

### It looks like SQLiDumper, no ?

Yeah, I know.

TODO: please someone correct those wrongly spelled words and conjugational errors. I'm on Neovim right now and there is no auto-spelling check.

## Popularity note ( 2018-05-10 )

When I woke up this morning, someone said that a guy by the name of NullArray tweeted about this project. 11 stars later, it makes me want to finish it more than ever !

## Contribution Note

Friday, the 11th of May, the first pull request to this project was sent by [@iyanuashiri](https://github.com/iyanuashiri).

## sTaTiStIcS

###  2018-05-11

Today, we are at 15 stars, and got our first pull request. The number of cloners and unique viewers is decreasing with the time, but I noticed that someone followed a link from `web.telegram.org`. Well, those referer statistics are cool.
I also finished implementing WhatWaf :)
