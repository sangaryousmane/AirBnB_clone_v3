#!/usr/bin/python3
"""Using flask framework 2
"""

from flask import Flask, render_template
from models import storage
from models.state import State

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


@app.route('/python/', defaults={'text': 'is_cool'})
@app.route("/python/<text>", strict_slashes=False)
def display_python(text):
    """ Display Python
    """
    msg = text.replace("_", " ")
    return f'Python {msg}'


@app.route("/number/<int:n>", strict_slashes=False)
def display_number(n):
    """ Display number only if
    """
    return f"{n} is a number"


@app.route("/number_template/<int:n>", strict_slashes=False)
def display_num_template(n):
    """ render number if it is an integer
    """
    return render_template("5-number.html", n=n)


@app.route("/number_odd_or_even/<int:n>", strict_slashes=False)
def display_odd_or_even(n):
    """Display odd or even
    """
    return render_template("6-number_odd_or_even.html", n=n)


@app.teardown_appcontext
def close_session(self):
    """Closes the SQLAlchemy Session after each request.
    """
    if storage is not None:
        storage.close()


@app.route("/states_list", strict_slashes=False)
def display_states():
    """ Display states from db
    """
    states = storage.all('State')
    return render_template("7-states_list.html", states=states.values())


if __name__ == '__main__':
    app.run()
