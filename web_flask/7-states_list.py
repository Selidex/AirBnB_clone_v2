#!/usr/bin/python3
""" Setting up the web flask for HBNB"""
from flask import Flask, escape, request, render_template

app = Flask(__name__)
app.url_map.strict_slashes = False

if __name__ == "__main__":
    app.run(host='0.0.0.0', port='5000')
