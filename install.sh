#!/bin/bash
# From AutoSQLi

# This script install the requirements of DorkNet and WhatWaf
# And also chmod things up
pip install -r DorkNet/requirements.txt
pip install -r WhatWaf/requirements.txt

echo ""
echo "----------------------------"
echo "| dependencies installed ! |"
echo "----------------------------"
echo ""

#chmoding

echo "running chmod +x on *.py ..."
chmod +x DorkNet/dorknet.py
chmod +x WhatWaf/WhatWaf.py
chmod +x sqlmap/sqlmap.py

# installation of geckodriver

echo "installing geckodriver..."
# since we are pretty dumb as a shell programmer, just bulkly launch install commands with sudo privileges
echo "Don't mind if there are errors, that's ok. You should get two of them"
echo "If you're on macOS make sure that brew is in your PATH"
sudo pacman -S geckodriver
sudo apt-get install geckodriver
brew install geckodriver
