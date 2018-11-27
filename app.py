# -*- coding: utf-8 -*-
from flask import Flask, render_template, jsonify, request
from api.get_forexrate import get_forexrate
import logging
app = Flask(__name__)

@app.route('/', methods=['GET'])
def verify():
    # when the endpoint is registered as a webhook, it must echo back
    # the 'hub.challenge' value it receives in the query arguments
    if request.args.get("hub.mode") == "subscribe" and request.args.get("hub.challenge"):
        if not request.args.get("hub.verify_token") == 'foo':
            return "Verification token mismatch", 403
        return request.args["hub.challenge"], 200

    return "Hello world! - Check completed", 200

@app.route('/api/forexrate', methods = ['GET'])
def forexrate():
    json_result = get_forexrate('https://www.vietcombank.com.vn/ExchangeRates/ExrateXML.aspx')
    return jsonify(json_result)

@app.errorhandler(500)
def server_error(e):
    # Log the error and stacktrace.
    logging.exception('An error occurred during a request.')
    return 'An internal error occurred.', 500


if __name__ == '__main__':
    app.run(debug = True)
