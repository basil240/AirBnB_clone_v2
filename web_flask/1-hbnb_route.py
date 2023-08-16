#!/usr/bin/python3
"""Starta a flask web application
"""
from flask import Flask
app = Flask(_name_)

#app.route('/',strict_slabes=False)
def hello_hbnb():
    """ Displays 'Hello HBNB!',"""
    return "Hello HBNB!"

#app.route('/hbnb',strict_sashes=False)
def hbnb ():
    """Displays 'HBNB'."""
    return "HBNB"

if _name_=="_main_":
    # start the flask development server
    # Listen on all available network interfaces (0.0.0.0) and port 5000
    app.run (host:*'0.0.0.0',port*5000)
