# AutoSQLi

## The Plan

AutoSQLi will be a python application which will, automatically, using a dork provided by the user, return a list of websites vulnerable to a SQL injection.
To find vulnerable websites, the users firstly provide a dork ( TODO: document what is a dork, or provide a link ), which is passed to DorkNet, which returns a list of URLs corresponding to it.
Then, AutoSQLi will do some very basic checks ( TODO: MAYBE USING SQLMAP AND IT's --smart and --batch function ) to verify if the application is protected by a Waf, or if one of it's parameters is vulnerable.
Sometimes, websites are protected by a Web Application Firewall, or in short, a WAF. To identify and get around of these WAFs, AutoSQLi will use WhatWaf.

Finally, AutoSQLi will exploit the website using sqlmap, and give the choice to do whatever he wants !

## FAQ
### Cool :)

Yeah, I know.

### It looks like SQLiDumper, no ?

Yeah, I know.

TODO: please someone correct those wrongly spelled words and conjugational errors. I'm on Neovim right now and there is no auto-spelling check.
