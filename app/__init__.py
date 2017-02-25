#!/usr/bin/env python3

from flask import Flask
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address

app = Flask(__name__)
limiter = Limiter(app, key_func=get_remote_address, global_limits=['10 per hour'])

from app import views