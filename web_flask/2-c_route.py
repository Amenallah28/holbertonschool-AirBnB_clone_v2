#!/usr/bin/python3
"""a script that starts a Flask web application"""
from flask import Flask
from markupsafe import escape
app = Flask(__name__)


@app.route("/", strict_slashes=False)
def show():
    """display Hello HBNB!"""
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def show2():
    """display HBNB"""
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def show3(text):
    """display “C ” followed by the value
    of the text variable (replace
    underscore _ symbols with a space )"""
    text = text.replace("_", " ")
    return "C {}".format(escape(text))


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")