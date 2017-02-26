#!/usr/bin/env python3

import json
from urllib import request

from app import cache

@cache.cached(timeout=3600, key_prefix="coinmarketcap_data")
def coinmarketcap_data():
    return json.loads(request.urlopen('https://api.coinmarketcap.com/v1/ticker/').read().decode('utf8'))

@cache.cached(timeout=3600, key_prefix="fixerio_data")
def fixerio_data():
    return json.loads(request.urlopen('https://api.fixer.io/latest?base=USD').read().decode('utf8'))
