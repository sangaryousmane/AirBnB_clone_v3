#!/usr/bin/python3
<<<<<<< HEAD
"""users"""
from api.v1.views import app_views
from flask import jsonify, abort, request
from models import storage
from models.user import User
from datetime import datetime
import uuid


@app_views.route('/users/', methods=['GET'])
@app_views.route('/users', methods=['GET'])
def list_users():
    '''Retrieves a list of all User objects'''
    list_users = [obj.to_dict() for obj in storage.all("User").values()]
    return jsonify(list_users)


@app_views.route('/users/<user_id>', methods=['GET'])
def get_user(user_id):
    '''Retrieves a User object'''
    all_users = storage.all("User").values()
    user_obj = [obj.to_dict() for obj in all_users if obj.id == user_id]
    if user_obj == []:
        abort(404)
    return jsonify(user_obj[0])


@app_views.route('/users/<user_id>', methods=['DELETE'])
def delete_user(user_id):
    '''Deletes a User object'''
    all_users = storage.all("User").values()
    user_obj = [obj.to_dict() for obj in all_users if obj.id == user_id]
    if user_obj == []:
        abort(404)
    user_obj.remove(user_obj[0])
    for obj in all_users:
        if obj.id == user_id:
            storage.delete(obj)
            storage.save()
    return jsonify({}), 200


@app_views.route('/users/', methods=['POST'])
def create_user():
    '''Creates a User'''
    if not request.get_json():
        abort(400, 'Not a JSON')
    if 'email' not in request.get_json():
        abort(400, 'Missing name')
    if 'password' not in request.get_json():
        abort(400, 'Missing name')
    users = []
    new_user = User(email=request.json['email'],
                    password=request.json['password'])
    storage.new(new_user)
    storage.save()
    users.append(new_user.to_dict())
    return jsonify(users[0]), 201


@app_views.route('/users/<user_id>', methods=['PUT'])
def updates_user(user_id):
    '''Updates a User object'''
    all_users = storage.all("User").values()
    user_obj = [obj.to_dict() for obj in all_users if obj.id == user_id]
    if user_obj == []:
        abort(404)
    if not request.get_json():
        abort(400, 'Not a JSON')
    try:
        user_obj[0]['first_name'] = request.json['first_name']
    except:
        pass
    try:
        user_obj[0]['last_name'] = request.json['last_name']
    except:
        pass
    for obj in all_users:
        if obj.id == user_id:
            try:
                if request.json['first_name'] is not None:
                    obj.first_name = request.json['first_name']
            except:
                pass
            try:
                if request.json['last_name'] is not None:
                    obj.last_name = request.json['last_name']
            except:
                pass
    storage.save()
    return jsonify(user_obj[0]), 200
=======
"""Users view
"""
from api.v1.views import app_views
from datetime import datetime
from flask import abort, jsonify, request
from models.city import City
from models import storage
from models.state import State
from models.user import User


@app_views.route("/users", methods=['GET'])
def get_all_users():
    """ Retrieves all the users info
    """
    users = storage.all(User).values()
    user = [s.to_dict() for s in states]

    if user == []:
        abort(404)

    return jsonify(user)


@app_views.route("/users/<user_id>", methods=['GET'])
def get_user(user_id):
    """ Get a user info
    """
    users = storage.all(User).values()
    user = [u.to_dict() for u in users if u.id == user_id]
    if user == []:
        abort(404)
    return jsonify(user[0]), 200


@app_views.route("/users", methods=['POST'])
def save_state(state_id):
    """ Creates a new user and save to DB
    """
    if not request.get_json():
        abort(400, 'Not a JSON')
    if 'email' not in request.get_json():
        abort(400, 'Missing email')
    if 'password' not in request.get_json():
        abort(400, 'Missing password')

    user = []
    name, password = request.json['password'], request.json['name']
    new_user = User(name=name, password=password)
    storage.new(new_user)
    storage.save()
    user.append(new_user.to_dict())
    return jsonify(user[0]), 201


@app_views.route("/user/<user_id>", methods=['DELETE'])
def delete_user(user_id):
    """ Delete a User from DB
    """
    users = storage.all(User).values()
    user = [u.to_dict() for u in users if u.id == user_id]

    if user == []:
        abort(404)

    user.remove(user[0])
    for u in users:
        if u.id == user_id:
            storage.delete(u)
            storage.save()
    return jsonify({}), 200


@app_views.route("/users/<user_id>", methods=['PUT'])
def update_user(user_id):
    """ Update a user info
    """
    users = storage.all(User).values()
    user = [u.to_dict() for u in users if u.id == user_id]

    if user == []:
        abort(404)

    if not request.get_json():
        abort(400, 'Not a JSON')

    user[0]['name'] = request.json['name']

    for u in users:
        if u.id == user_id:
            u.name = request.json['name']
    storage.save()
    return jsonify(user[0]), 200
>>>>>>> cc2987ccb05104f2811cea01580e3a34fd386551
