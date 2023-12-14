#!/usr/bin/python3
"""a script that starts a Flask web application and
diplays the cities related to the state based on the id
of the state passed in the url"""
from flask import Flask, render_template
from models import storage
from models.state import State
app = Flask(__name__)


@app.route("/states", strict_slashes=False)
def show():
    """display all the states"""
    states = list(storage.all(State).values())
    return render_template("9-states.html", states=states, show_state=True)


@app.route("/states/<id>", strict_slashes=False)
def show2(id):
    """if id is found we display the cities related
    to the state based on the id otherwise we print not found"""
    states = list(storage.all(State).values())
    for state in states:
        if state.id == id:
            searched_state = state.name
            cities = state.cities
            return render_template(
                "9-states.html",
                searched_state=searched_state,
                id=id,
                cities=cities,
                found=True)
    return render_template("9-states.html", found=False)


@app.teardown_appcontext
def teardown(exception):
    """remove the current SQLAlchemy Session"""
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
