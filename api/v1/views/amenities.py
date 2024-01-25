#!/usr/bin/python3
<<<<<<< HEAD
"""amenities"""
from api.v1.views import app_views
from flask import jsonify, abort, request
from models import storage
from models.amenity import Amenity
from datetime import datetime
import uuid


@app_views.route('/amenities/', methods=['GET'])
def list_amenities():
    '''Retrieves a list of all Amenity objects'''
    list_amenities = [obj.to_dict() for obj in storage.all("Amenity").values()]
    return jsonify(list_amenities)


@app_views.route('/amenities/<amenity_id>', methods=['GET'])
def get_amenity(amenity_id):
    '''Retrieves an Amenity object'''
    all_amenities = storage.all("Amenity").values()
    amenity_obj = [obj.to_dict() for obj in all_amenities
                   if obj.id == amenity_id]
    if amenity_obj == []:
        abort(404)
    return jsonify(amenity_obj[0])


@app_views.route('/amenities/<amenity_id>', methods=['DELETE'])
def delete_amenity(amenity_id):
    '''Deletes an Amenity object'''
    all_amenities = storage.all("Amenity").values()
    amenity_obj = [obj.to_dict() for obj in all_amenities
                   if obj.id == amenity_id]
    if amenity_obj == []:
        abort(404)
    amenity_obj.remove(amenity_obj[0])
    for obj in all_amenities:
        if obj.id == amenity_id:
            storage.delete(obj)
            storage.save()
    return jsonify({}), 200


@app_views.route('/amenities/', methods=['POST'])
def create_amenity():
    '''Creates an Amenity'''
    if not request.get_json():
        abort(400, 'Not a JSON')
    if 'name' not in request.get_json():
        abort(400, 'Missing name')
    amenities = []
    new_amenity = Amenity(name=request.json['name'])
    storage.new(new_amenity)
    storage.save()
    amenities.append(new_amenity.to_dict())
    return jsonify(amenities[0]), 201


@app_views.route('/amenities/<amenity_id>', methods=['PUT'])
def updates_amenity(amenity_id):
    '''Updates an Amenity object'''
    all_amenities = storage.all("Amenity").values()
    amenity_obj = [obj.to_dict() for obj in all_amenities
                   if obj.id == amenity_id]
    if amenity_obj == []:
        abort(404)
    if not request.get_json():
        abort(400, 'Not a JSON')
    amenity_obj[0]['name'] = request.json['name']
    for obj in all_amenities:
        if obj.id == amenity_id:
            obj.name = request.json['name']
    storage.save()
    return jsonify(amenity_obj[0]), 200
=======
"""Cities view
"""
from api.v1.views import app_views
from datetime import datetime
from flask import abort, jsonify, request
from models.amenity import Amenity
from models import storage


@app_views.route("/amenities", methods=['GET'])
def get_all_amenities():
    """ Get all amenities
    """
    amenities = storage.all(Amenity).values()
    amenity = [a.to_dict() for a in amenities]

    if amenity == []:
        abort(404)
    return jsonify(amenity)


@app_views.route("/amenities/<amenity_id>", methods=['GET'])
def get_amenity(amenity_id):
    """ Get an amenity
    """
    amenities = storage.all(Amenity).values()
    amenity = [a.to_dict() for a in amenities if a.id == amenity_id]

    if amenity == []:
        abort(404)
    return jsonify(amenity[0]), 200


@app_views.route("/amenities", methods=['POST'])
def save_amenity():
    """ Create new amenity
    """
    if not request.get_json():
        abort(400, "Not a JSON")
    if 'name' not in request.get_json():
        abort(400, "Missing name")

    amenity = []
    new_amenity = Amenity(name=request.json['name'])
    storage.new(new_amenity)
    storage.save()
    amenity.append(new_amenity.to_dict())
    return (amenity[0]), 201


@app_views.route("/amenities/<amenity_id>", methods=['DELETE'])
def delete_amenity(amenity_id):
    """ Delete an amenity
    """
    amenities = storage.all(Amenity).values()
    amenity = [a.to_dict() for a in amenities if a.id == amenity_id]

    if amenity == []:
        abort(404)
    amenity.remove(amenity[0])

    for a in amenities:
        if a.id == amenity_id:
            storage.delete(a)
            storage.save()
    return jsonify({}), 200


@app_views.route("/amenities/<amenity_id>", methods=['PUT'])
def update_an_amenity(amenity_id):
    """ Update an amenity base on the given ID
    """
    if not request.get_json():
        abort(400)

    amenities = storage.all(Amenity).values()
    amenity = [a.to_dict() for a in amenities if a.id == amenity_id]

    if amenity == []:
        abort(404)
    amenity[0]['name'] = request.json['name']

    for a in amenities:
        if a.id == amenity_id:
            a.name = request.json['name']
    storage.save()
    return jsonify[amenity[0]), 200
>>>>>>> cc2987ccb05104f2811cea01580e3a34fd386551
