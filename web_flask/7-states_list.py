#!/usr/bin/python3
""" Script that runs Flask framework """
from flask import Flask, render_template
from models import storage
from models.state import State


app = Flask(__name__)


@app.teardown_appcontext
def teardown_db(exception):
    """Remove the current Sql session"""
    storage.close()


@app.route('/states_list', strict_slashes=False)
def states_list():
    """Display HTML page with a list of all state"""
    states = storage.all(State)
    to_html = {value.id: value.name for value in states.values()}
    return render_template('7-states_list.html',
                           Table="States",
                           items=to_html)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
