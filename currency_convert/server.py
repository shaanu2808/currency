import requests
from pycoingecko import CoinGeckoAPI
from flask import Flask, request, jsonify
import logging
import sys
from price_conversion import current_price

app = Flask(__name__)
logging.basicConfig(stream=sys.stdout, level=logging.DEBUG, format=f'%(asctime)s  %(message)s')
logger = logging.getLogger(__name__)


@app.route("/exchange", methods=["GET"])
def exchange_into_dollars():
    coin = request.args.get("coin", "")
    amount = request.args.get("amount")

    logger.info("coin input value is: %s (type: %s)" % (coin, type(coin)))
    logger.info("amount input value is: %s (type: %s)" % (amount, type(amount)))

    # Calculate this!
    print(coin,amount,"####")
    usd_amount, status = current_price(amount,coin)

    # if status == False:
    #     return jsonify({"error":"Invalid amount"})
    

    return jsonify(usd_amount=usd_amount)


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=6001)

# http://127.0.0.1:6001/exchange?coin=btc&amount=1.5