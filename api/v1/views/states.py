#!/usr/bin/python3
<<<<<<< HEAD
"""states"""
from api.v1.views import app_views
from flask import jsonify, abort, request
from models import storage
from models.state import State
from datetime import datetime
import uuid


@app_views.route('/states/', methods=['GET'])
def list_states():
    '''Retrieves a list of all State objects'''
    list_states = [obj.to_dict() for obj in storage.all("State").values()]
    return jsonify(list_states)


@app_views.route('/states/<state_id>', methods=['GET'])
def get_state(state_id):
    '''Retrieves a State object'''
    all_states = storage.all("State").values()
    state_obj = [obj.to_dict() for obj in all_states if obj.id == state_id]
    if state_obj == []:
        abort(404)
    return jsonify(state_obj[0])


@app_views.route('/states/<state_id>', methods=['DELETE'])
def delete_state(state_id):
    '''Deletes a State object'''
    all_states = storage.all("State").values()
    state_obj = [obj.to_dict() for obj in all_states if obj.id == state_id]
    if state_obj == []:
        abort(404)
    state_obj.remove(state_obj[0])
    for obj in all_states:
        if obj.id == state_id:
            storage.delete(obj)
=======
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
>>>>>>> cc2987ccb05104f2811cea01580e3a34fd386551
            storage.save()
    return jsonify({}), 200


<<<<<<< HEAD
@app_views.route('/states/', methods=['POST'])
def create_state():
    '''Creates a State'''
=======
@app_views.route("/states", methods=['POST'])
def save_state():
    """ Save a new state"""
>>>>>>> cc2987ccb05104f2811cea01580e3a34fd386551
    if not request.get_json():
        abort(400, 'Not a JSON')
    if 'name' not in request.get_json():
        abort(400, 'Missing name')
<<<<<<< HEAD
    states = []
    new_state = State(name=request.json['name'])
    storage.new(new_state)
    storage.save()
    states.append(new_state.to_dict())
    return jsonify(states[0]), 201


@app_views.route('/states/<state_id>', methods=['PUT'])
def updates_state(state_id):
    '''Updates a State object'''
    all_states = storage.all("State").values()
    state_obj = [obj.to_dict() for obj in all_states if obj.id == state_id]
    if state_obj == []:
        abort(404)
    if not request.get_json():
        abort(400, 'Not a JSON')
    state_obj[0]['name'] = request.json['name']
    for obj in all_states:
        if obj.id == state_id:
            obj.name = request.json['name']
    storage.save()
    return jsonify(state_obj[0]), 200
=======
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
>>>>>>> cc2987ccb05104f2811cea01580e3a34fd386551
