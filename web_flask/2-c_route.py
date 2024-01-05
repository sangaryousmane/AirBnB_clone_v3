#!/usr/bin/python3
"""Using flask framework 2
"""

from flask import Flask
app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello():
    """ hello HBNB
    """
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def display_hbnb():
    """ Display HBNB
    """
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def display_c_with_text(text):
    """ display with text
    """
    remove_underscore = text.replace("_", " ")
    return f'C {remove_underscore}'


if __name__ == '__main__':
    app.run()
