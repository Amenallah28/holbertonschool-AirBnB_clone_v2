#!/usr/bin/python3
"""a script that starts a Flask web application"""

from flask import Flask
app=Flask(__name__)


@app.route('/',strict_slashes=False)
def display():
    """display Hello HBNB!"""
    return "Hello HBNB!"


@app.route('/hbnb',strict_slashes=False)
def hbnb():
    """display the string HBNB"""
    return"HBNB"


@app.route('/c/<text>',strict_slashes=False)
def displayC(text):
    """ display “C ” followed by the value of the text variable 
    (replace underscore _ symbols with a space ) """
    return "C " + text.replace('_', ' ')


@app.route('/python', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def displayPython(text='is cool'):
    """display python + a text"""
    return "Python " + text.replace('_', ' ')


@app.route('/number/<n:int>')
def display_n(n):
    return "{:d} is a number".format(n)

if __name__=="__main__":
    app.run(host="0.0.0.0",port=5000)

    
