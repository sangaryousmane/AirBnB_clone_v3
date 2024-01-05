#!/usr/bin/python3

from flask import Flask
from models import storage
from models.state import State

app = Flask('__name__')

@app.teardown_appcontext
def refresh(exception):
        models.storage.close()


@app.route("/states", strict_slashes=False)
def states():
    """ Display normal
    """
    states = storage.all(cls='State')
    return render_template("9-states.html", states=states.values())


@app.route("/states/<id>", strict_slashes=False)
def states_city_id_route():
    """ Get state city by ID
    """
    states = storage.all(cls='State')
    return render_template("9-states.html", states=states.values())


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
