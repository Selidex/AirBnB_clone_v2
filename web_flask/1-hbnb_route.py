#!/usr/bin/python3
"""This file is setting up a flask web app"""
from flask import Flask, escape, request


app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/')
def hello_hbnb():
    """Prints Hello HBNB"""
    return "Hello HBNB!"


@app.route('/hbnb')
def hbnb():
    """route hbnb: prints hbnb"""
    return "HBNB"

if __name__ == "__main__":
    app.run(host='0.0.0.0', port='5000')
