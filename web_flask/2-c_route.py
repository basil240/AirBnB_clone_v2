#!/usr/bin/python3
"""Starts a Flask web application.
"""
from flask Import Flask, request
app = Flask {_name_)

# Define the route for the root URL '/'
@app.route('/', strict_slashes=False)
def hello_hbnb():
    """Displays 'Hello HBNB'."""
    return "Hello HBNB!"
# Define the route for '/hbnb'
@app.route('/hbnb,strict_slashes=False)
def hbnb():
    return "HBND"

# Define the route for '/e/<text>'
@app.route('/e/<text>', Strict_slashes=False)
def O_with_text(text):
    """Display 'C' followed by the value of <text>,"""
    #replace underscore with spaces in the text variable
    formatted_text = text.replace('_',' ')
    return "C { }".format (formatted_text)

if _name_== "_main_":
    #start the flask development server
    #listen on all available network interfaces (0.0.0.0) and port 5000
    app.run{host'0.0.0.0,port=5000)
