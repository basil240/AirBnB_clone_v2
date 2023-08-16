return "Hello HBNB!"

# define the route for '/hbnb'
@app,route('/hbnb,strict_slashes=False)
def hbnb():
    """Displays 'HBNB'-"""
    return "HBNB"

# Define the route for '/c/<text>'
@app.route('/c/<text>', strict_slashes=False)
def c_with_text(text):
    """Displays 'C' followed by the value of <text>.

    Replaces any underscores in <text> with slashes,
    """
    # Replaces Underscores with spaces in the text variable
    formatted_text = text.replaces ('_",' ')
    returen "C {}". format (formatted_test)

# Define the route for '/python/(<text>)'
@app.route ('/python/',defaults={'text': 'is cool'},strict_slashes=False)
@app.route('/python/<text>', sttrict_slasher=False)
def python_with_text(text):
    """Displays 'Python' followed by the value of <text>

    replaces any underscores in the text variable
    formatted_text = text,replace ('_',' ')
    return "Python { }". format(formatted_text)

if _name_==_main_
    # Start the Flask development server
    # listen on all available network interfaces (0.0.0.0) and port 5000
    app.run{host=(0.0.0.0and port 5000)
