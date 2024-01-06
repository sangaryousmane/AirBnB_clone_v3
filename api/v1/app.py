#!/usr/bin/python3
""" Entry point of the Restful service
"""
from flask import Flask, make_response, jsonify
from api.v1.views import app_views
from models import storage
from flask_cors import CORS

app = Flask(__name__)
cors = CORS(app, resources={r"/api/*": {"origins": "0.0.0.0"}})


app.url_map.strict_slashes = False
app.register_blueprint(app_views)


@app.teardown_appcontext
def teardown():
    """ close storage
    """
    if storage:
        storage.close()


@app.errorhandler(404)
def status_code():
    """ Return a custom error for http code 404
    """
    return make_response(jsonify({"error": "Not found"}), 404)


if __name__ == '__main__':
    if getenv("HBNB_API_HOST") and getenv("HBNB_API_PORT"):
        app.run(host=HBNB_API_HOST, port=int(HBNB_API_PORT), threaded=True)
    else:
        app.run(host='0.0.0.0', port=5000)
