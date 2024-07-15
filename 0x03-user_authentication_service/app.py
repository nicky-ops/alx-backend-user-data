#!/usr/bin/env python3
'''
Basic Flask app
'''
from flask import Flask
from flask import jsonify


app = Flask(__name__)


@app.route("/", methods=["GET"])
def message():
    """
    returns a JSON payload for the endpoint
    """
    return jsonify({"message": "Bienvenue"})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
