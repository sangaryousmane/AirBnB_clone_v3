#!/usr/bin/python3
"""Cities view
"""
from api.v1.views import app_views
from flask import abort, jsonify, request
from models import storage
from models.state import State
from datetime import datetime


@app_views.route("/states/<state_id>/cities", methods=['GET'])
@app_views.route("/states/<state_id>/cities/", methods=['GET'])
def get_all_cities(state_id):
    """ Retrieves all the cities of a state
    """
    cities = storage.all(City).values()
    city = [c.to_dict() for c in cities if c.state_id == state_id]

    if city == []:
        abort(404)

    return jsonify(city), 200

@app_views.route("/cities/<city_id>", methods=['GET'])
def get_city(city_id):
    """ Get a city info
    """
    cities = storage.all(City).values()
    city = [c.to_dict() for c in cities if c.id == city_id]
    if city == []:
        abort(404)
    return jsonify(city[0]), 200

@app_views.route("/states/<state_id>/cities", methods=['POST'])
def save_city(state_id):
    """ Creates a new city and save to DB
    """
    if not request.get_json():
        abort(400)
    if 'name' not in request.json['name']:
        abort(400, 'Not a JSON')
    city = []
    new_city = City(name=request.json['name'], state_id=state_id)
    storage.new(new_city)
    storage.save()
    city.append(new_city.to_dict())
    return jsonify(city[0]), 201
