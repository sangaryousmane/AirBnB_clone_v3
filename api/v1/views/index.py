#!/usr/bin/python3
"""index"""
from api.v1.views import app_views
from flask import jsonify
from models import storage
from models.amenity import Amenity
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.review import Review

classes = {"users": "User", "places": "Place", "states": "State",
           "cities": "City", "amenities": "Amenity",
           "reviews": "Review"}


@app_views.route('/status', methods=['GET'])
def status():
    ''' routes to status page '''
    return jsonify({'status': 'OK'})


@app_views.route('/stats', methods=['GET'])
<<<<<<< HEAD
def count():
    '''retrieves the number of each objects by type'''
    count_dict = {}
    for cls in classes:
        count_dict[cls] = storage.count(classes[cls])
    return jsonify(count_dict)
=======
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
>>>>>>> cc2987ccb05104f2811cea01580e3a34fd386551
