#!/usr/bin
from flask import Flask, abort, request, jsonify
import logging

logging.basicConfig(
    format='%(asctime)s %(levelname)s %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S',
    filename="/var/log/app/app.log",
    level=logging.INFO
)

app = Flask(__name__)

@app.route('/v1/color', methods=['GET'])
def get_color():
    try:
        ret = {'code': 'red', 'name': 'osm'}
        return jsonify(ret), 200
    except Exception as e:
        logging.error(e)
        abort(500)

@app.route('/health', methods=['GET'])
def get_health():
    try:
        ret = {'status': 'ok'}
        return jsonify(ret), 200
    except Exception as e:
        logging.error(e)
        abort(500)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080)