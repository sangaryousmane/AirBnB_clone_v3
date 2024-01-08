#!/usr/bin/python3
"""Cities view
"""
from api.v1.views import app_views
from datetime import datetime
from flask import abort, jsonify, request
from models.City import City
from models import storage
from models.state import State


@app_views.route("/states/<state_id>/cities", methods=['GET'])
@app_views.route("/states/<state_id>/cities/", methods=['GET'])
def get_all_cities(state_id):
    """ Retrieves all the cities of a state
    """
    states = storage.all(State).values()
    state = [s.to_dict() for s in states if s.id == state_id]

    if state == []:
        abort(404)

    cities = storage.all(City).values()
    city = [c.to_dict() for c in cities if state_id == c.state_id]
    return jsonify(city)


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
@app_views.route("/states/<state_id>/cities/", methods=['POST'])
def save_city(state_id):
    """ Creates a new city and save to DB
    """
    if not request.get_json():
        abort(400, 'Not a JSON')
    if 'name' not in request.json['name']:
        abort(400, 'Missing name')
    states = storage.all(State).values()
    state = [s.to_dict() for s in states if s.id == state_id]
    if state == []:
        abort(404)

    city = []
    new_city = City(name=request.json['name'], state_id=state_id)
    storage.new(new_city)
    storage.save()
    city.append(new_city.to_dict())
    return jsonify(city[0]), 201


@app_views.route("/cities/<city_id>", methods=['DELETE'])
def delete_city(city_id):
    """ Delete an info for city
    """
    cities = storage.all(City).values()
    city = [c.to_dict() for c in cities if c.id == city_id]

    if city == []:
        abort(404)

    city.remove(city[0])
    for c in cities:
        if c.id == city_id:
            storage.delete(c)
            storage.save()
    return jsonify({}), 200


@app_views.route("/cities/<city_id>", methods=['UPDATE'])
def update_city(city_id):
    """ Update city info
    """
    cities = storage.all(City).values()
    city = [c.to_dict() for c in cities if c.id == city_id]

    if city == []:
        abort(404)

    if not request.get_json():
        abort(400, 'Not a JSON')

    city[0]['name'] = request.json['name']

    for c in cities:
        if c.id == city_id:
            c.name = request.json['name']
    storage.save()
    return jsonify(city[0]), 200
