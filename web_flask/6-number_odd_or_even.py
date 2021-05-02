#!/usr/bin/python3
"""This file is setting up a flask web app"""
from flask import Flask, escape, request, render_template


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


@app.route('/c/<text>')
def c(text):
    """prints c is followed by text"""
    nt = text.replace('_', ' ')
    return "C {}".format(nt)


@app.route('/python', defaults={'text': 'is cool'})
@app.route('/python/<text>')
def pyis(text='is cool'):
    """prints python followed by text, with default"""
    nt = text.replace('_', ' ')
    return "Python {}".format(nt)


@app.route('/number/<int:n>')
def num(n):
    """some random text here, brain.exe failed to compile"""
    return "{} is a number".format(n)


@app.route('/number_template/<int:n>')
def num_tem(n):
    """returns an html page"""
    return render_template('5-number.html', n=n)


@app.route('/number_odd_or_even/<int:n>')
def num_oe(n):
    """returns an html page"""
    return render_template('6-number_odd_or_even.html', n=n)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port='5000')
