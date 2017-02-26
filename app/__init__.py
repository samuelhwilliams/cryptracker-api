#!/usr/bin/env python3

from flask import Flask
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
from flask_cache import Cache

app = Flask(__name__)
limiter = Limiter(app, key_func=get_remote_address, global_limits=['50 per minute'])
cache = Cache(app, config={'CACHE_TYPE': 'simple'})

from app import views
