#!/usr/bin/python3
<<<<<<< HEAD
"""app"""
from flask import Flask, make_response, jsonify
from models import storage
from api.v1.views import app_views
from os import getenv
=======
''' app.py '''

from api.v1.views import app_views
>>>>>>> cc2987ccb05104f2811cea01580e3a34fd386551
from flask_cors import CORS
from flask import Flask, make_response, jsonify
from models import storage
from os import getenv


app = Flask(__name__)
cors = CORS(app, resources={r"/api/*": {"origins": "0.0.0.0"}})


app.url_map.strict_slashes = False
app.register_blueprint(app_views)


@app.teardown_appcontext
def tear(self):
    ''' closes storage engine '''
    storage.close()


@app.errorhandler(404)
<<<<<<< HEAD
def not_found(error):
    ''' handles 404 error and gives json formatted response '''
    return make_response(jsonify({'error': 'Not found'}), 404)

if __name__ == '__main__':
    if getenv("HBNB_API_HOST") is None:
        HBNB_API_HOST = '0.0.0.0'
    else:
        HBNB_API_HOST = getenv("HBNB_API_HOST")
    if getenv("HBNB_API_PORT") is None:
        HBNB_API_PORT = 5000
    else:
        HBNB_API_PORT = int(getenv("HBNB_API_PORT"))
=======
def status_code(self):
    ''' Return a custom error for http code 404
    '''
    return make_response(jsonify({"error": "Not found"}), 404)


if __name__ == '__main__':
    if getenv("HBNB_API_HOST") and getenv("HBNB_API_PORT"):
        HBNB_API_HOST = getenv("HBNB_API_HOST")
        HBNB_API_PORT = int(getenv("HBNB_API_PORT"))
    else:
        HBNB_API_HOST = '0.0.0.0'
        HBNB_API_PORT = 5000
>>>>>>> cc2987ccb05104f2811cea01580e3a34fd386551
    app.run(host=HBNB_API_HOST, port=HBNB_API_PORT, threaded=True)
