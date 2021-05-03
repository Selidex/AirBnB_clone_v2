#!/usr/bin/python3
""" Setting up the web flask for HBNB"""
from flask import Flask, escape, request, render_template
from models import storage
from models.state import State

app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/states_list')
def state_list():
    """Lists all states"""
    statelist = storage.all(State)
    return render_template('7-states_list.html', statelist=statelist)


@app.teardown_appcontext
def teardown():
    """ runs when app is done"""
    storage.close()


if __name__ == "__main__":
    app.run(host='0.0.0.0', port='5000')
