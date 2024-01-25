#!/usr/bin/python3
""" Starts a Flash Web Application """
from models import storage
from models.state import State
from os import environ
from flask import Flask, render_template
app = Flask(__name__)
# app.jinja_env.trim_blocks = True
# app.jinja_env.lstrip_blocks = True


@app.teardown_appcontext
<<<<<<< HEAD
def close_db(error):
    """ Remove the current SQLAlchemy Session """
    storage.close()


@app.route('/states_list', strict_slashes=False)
def states_list():
    """ displays a HTML page with a list of states """
    states = storage.all(State).values()
    states = sorted(states, key=lambda k: k.name)
    return render_template('7-states_list.html', states=states)


@app.route('/cities_by_states', strict_slashes=False)
def cities_list():
    """ displays a HTML page with a list of cities by states """
    states = storage.all(State).values()
    states = sorted(states, key=lambda k: k.name)
    st_ct = []
    for state in states:
        st_ct.append([state, sorted(state.cities, key=lambda k: k.name)])
    return render_template('8-cities_by_states.html',
                           states=st_ct,
                           h_1="States")


if __name__ == "__main__":
    """ Main Function """
=======
def close_session(self):
    """Closes the SQLAlchemy Session after each request.
    """
    if storage is not None:
        storage.close()


@app.route("/states_list", strict_slashes=False)
def display_states():
    """ Display states from db
    """
    states = storage.all('State').order_by(State.name).all()
    return render_template("7-states_list.html", states=states.values())


@app.route("/cities_by_states", strict_slashes=False)
def display_cities_with_states():
    """ Display cities with state
    """
    states = storage.all('State')
    return render_template("8-cities_by_states.html", states=states.values())


if __name__ == '__main__':
>>>>>>> cc2987ccb05104f2811cea01580e3a34fd386551
    app.run(host='0.0.0.0', port=5000)
