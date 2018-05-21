#!/bin/bash
# From AutoSQLi

# This script install the requirements of DorkNet and WhatWaf
# And also chmod things up
pip install -r WhatWaf/requirements.txt
pip install -r requirements.txt
pip install pysocks

echo ""
echo "----------------------------"
echo "| dependencies installed ! |"
echo "----------------------------"
echo ""

#chmoding

echo "running chmod +x on *.py ..."
chmod +x DorkNet/dorknet.py
chmod +x WhatWaf/whatwaf.py
chmod +x sqlmap/sqlmap.py
