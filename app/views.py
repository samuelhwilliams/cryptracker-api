#!/usr/bin/env python3

from flask import render_template, jsonify, request as flask_request
from flask_api import status
from app import app
from lxml import html
import json
from urllib import request

COINMARKETCAP_DATA = json.loads(request.urlopen('https://api.coinmarketcap.com/v1/ticker/').read().decode('utf8'))
FIXERIO_DATA = json.loads(request.urlopen('https://api.fixer.io/latest?base=USD').read().decode('utf8'))

@app.route('/')
@app.route('/index')
def index():
    return jsonify({'status': 'OK'})


@app.route('/convert', methods=['GET'])
def convert():
    if not all([x in flask_request.args for x in ('source', 'amount', 'target')]):
        return jsonify({'status': 'FAIL', 'reason': 'Mandatory parameters not passed: source, amount, target.'}),\
               status.HTTP_400_BAD_REQUEST

    try:
        source_cryptocurrency = flask_request.args.get('source').lower()
        amount = float(flask_request.args.get('amount'))
        target_currency = flask_request.args.get('target').lower()
    except ValueError as e:
        return jsonify({'status': 'FAIL', 'reason': 'Invalid amount (must be float-able): '
                                                    '{}'.format(request.args.get('amount'))}),\
               status.HTTP_400_BAD_REQUEST

    bought_at = flask_request.args.get('bought_at')
    if bought_at:
        try:
            bought_at = float(bought_at)
        except ValueError as e:
            return jsonify({'status': 'FAIL', 'reason': 'Invalid bought_at (must be float-able): '
                                                        '{}'.format(bought_at)}),\
                   status.HTTP_400_BAD_REQUEST

    price_usd = float([x for x in COINMARKETCAP_DATA if x['name'].lower() == source_cryptocurrency][0]['price_usd'])

    result = {source_cryptocurrency: amount, 'usd_per_unit': price_usd, 'usd': amount * price_usd}
    if target_currency != 'usd':
        result.update({target_currency: amount * price_usd * FIXERIO_DATA['rates'][target_currency.upper()]})

    if bought_at:
        result.update({'bought_at': bought_at, 'change': result[target_currency] - bought_at})

    return jsonify(result), status.HTTP_200_OK
