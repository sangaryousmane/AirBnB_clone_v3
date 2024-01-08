#!/usr/bin/python3
"""State view
"""
from api.v1.views import app_views
from flask import abort, jsonify, request
from models import storage
from models.state import State
from datetime import datetime


@app_views.route("/states", methods=['GET'])
def get_states():
    """Handle the retrieving of all states from DB
    """
    states = storage.all(State).values()
    result = [s.to_dict() for s in states]
    return jsonify(result)


@app_views.route("/states/<state_id>", methods=['GET'])
def get_state(state_id):
    """ Retrieve a single state information
    """
    states = storage.all(State).values()
    result = [s.to_dict() for s in states if s.id == state_id]
    if state_id == []:
        abort(404)
    return jsonify(result[0])


@app_views.route("/states/<state_id>", methods=['DELETE'])
def delete_state(state_id):
    """ Delete a state base on ID
    """
    states = storage.all(State).values()
    result = [s.to_dict() for s in states if s.id == state_id]
    if result == []:
        abort(404)
    result.remove(result[0])

    for j in states:
        if j.id == state_id:
            storage.delete(j)
            storage.save()
    return jsonify({}), 200


@app_views.route("/states", methods=['POST'])
def save_state():
    """ Save a new state"""
    if not request.get_json():
        abort(400, 'Not a JSON')
    if 'name' not in request.get_json():
        abort(400, 'Missing name')
    state = []
    new_state = State(name=request.json.get("name"))
    storage.new(new_state)
    storage.save()
    state.append(new_state.to_dict())
    return jsonify(state[0]), 201


@app_views.route("/states/<state_id>", methods=['PUT'])
def update_state(state_id):
    """ Update a state info
    """
    states = storage.all(State).values()
    state = [s.to_dict() for s in states if s.id == state_id]

    if state == []:
        abort(404)
    if not request.get_json():
        abort(400, 'Not a JSON')
    state[0]['name'] = request.json['name']
    for obj in states:
        if obj.id == state_id:
            obj.name = request.json["name"]
    storage.save()
    return jsonify(state[0]), 200
