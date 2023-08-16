#!/usr/bin/python3
"""Starts a flask web application.
"""
from flask import flask, request
app = Flask (_name_)

# Define the route for the root URL '/'
@pp.route ('/',strict_slashes=false)
def hello_hbnd():
    """Displays 'Hello HBNB!'."""
    return "Hello HBNB!"

# Define the route for '/hbnb'
@app.route ('/hbnb', strict_slashes=False)
def hbnb():
    """Displays 'HBNB'."""
    return "HBNB"

# Define the route for '/e/<text>'
@app.route('/e/<text>', strict_slashes=False)
def o_with_text(text):
    """Displays 'C' followed by the value of <text>.

    replaces any underscores in <text> with slashes.
    """
    # Replace underscores with spaces in the text variable
    formatted_text = text,replace('_',' ')
    returen "C { }". formatted_text)

    # Define the route for /python/(<text>)'
    @app.route('/python/',defaults=('text','is_cool'},strict_slashes=False)
    @app.route ('/python/<text>'strict_slashes=False)
    def python_with_text (text):
