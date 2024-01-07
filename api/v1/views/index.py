#!/usr/bin/python3
""" Restful index
"""
from api.v1.views import app_views
from flask import jsonify
from models import storage
from models.amenity import Amenity
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.review import Review


@app_views.route('/status', methods=['GET'])
def status_response():
    """ status OK
    """
    return jsonify({"status": 'OK'})


@app_views.route('/stats', methods=['GET'])
def stats_count():
    """ count length of classes
    """
    counter_dict = {}
    all_classes = {"users": "User", "places": "Place", "states": "State",
                   "cities": "City", "amenities": "Amenity",
                   "reviews": "Review"}

    for count in all_classes:
        counter_dict[count] = storage.count(all_classes[count])
    return jsonify(counter_dict)
