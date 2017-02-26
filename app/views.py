#!/usr/bin/env python3

from flask import jsonify
from flask_api import status
from app import app

from .helpers import coinmarketcap_data, fixerio_data

@app.route('/')
@app.route('/index')
def index():
    return jsonify({'status': 'OK'})


@app.route('/convert/<string:source_cryptocurrency>/<int:amount>/<string:target_currency>', methods=['GET'])
@app.route('/convert/<string:source_cryptocurrency>/<float:amount>/<string:target_currency>', methods=['GET'])
def convert(source_cryptocurrency, amount, target_currency):
    """Converts a given number of source cryptocurrency coins/units to the 'best guess' estimate of their equivalent
    value in a specific target fiat currency."""
    source_cryptocurrency = source_cryptocurrency.upper()
    target_currency = target_currency.upper()

    try:
        price_usd = float([x for x in coinmarketcap_data() if x['symbol'] == source_cryptocurrency][0]['price_usd'])
    except KeyError as e:
        return jsonify({'status': 'FAIL', 'reason': 'Requested source cryptocurrency symbol not found: {}.'
                       .format(source_cryptocurrency)}), status.HTTP_404_NOT_FOUND

    result = {source_cryptocurrency.lower(): amount, 'usd_per_unit': price_usd, 'usd': amount * price_usd}
    if target_currency != 'USD':
        try:
            result.update({target_currency.lower(): amount * price_usd * fixerio_data()['rates'][target_currency]})
        except KeyError as e:
            return jsonify({'status': 'FAIL', 'reason': 'Requested target fiat currency symbol not found: {}.'
                           .format(target_currency)}), status.HTTP_404_NOT_FOUND

    return jsonify(result), status.HTTP_200_OK
