#From AutoSQLi

# Intensity of WhatWaf's WAF research. Must be >= 1 and <= 5
WHATWAF_VERIFY_NUM = "3"

WHATWAF_DEBUG = True
WHATWAF_DEBUG_REPORT = """
------------------------------
{
    "apparent working tampers": null,
    "identified firewall": "Apache generic website protection",
    "is protected": true,
    "url": "http://youwontknowthisurl.com/q=12345678"
}
------------------------------
"""
