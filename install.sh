#!/bin/bash
# From AutoSQLi

# This script install the requirements of DorkNet and WhatWaf
# And also chmod things up
pip install -r DorkNet/requirements.txt
pip install -r WhatWaf/requirements.txt
pip install -r requirements.txt

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
