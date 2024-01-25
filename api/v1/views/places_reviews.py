#!/usr/bin/python3
<<<<<<< HEAD
"""places_reviews"""
from api.v1.views import app_views
from flask import jsonify, abort, request
from models import storage
from models.place import Place
from models.review import Review
from datetime import datetime
import uuid


@app_views.route('/places/<place_id>/reviews', methods=['GET'])
@app_views.route('/places/<place_id>/reviews/', methods=['GET'])
def list_reviews_of_place(place_id):
    ''' Retrieves a list of all Review objects of a Place '''
    all_places = storage.all("Place").values()
    place_obj = [obj.to_dict() for obj in all_places if obj.id == place_id]
    if place_obj == []:
        abort(404)
    list_reviews = [obj.to_dict() for obj in storage.all("Review").values()
                    if place_id == obj.place_id]
    return jsonify(list_reviews)


@app_views.route('/places/<place_id>/reviews', methods=['POST'])
def create_review(place_id):
    '''Creates a Review'''
    if not request.get_json():
        abort(400, 'Not a JSON')
    if 'user_id' not in request.get_json():
        abort(400, 'Missing user_id')
    user_id = request.json['user_id']
    if 'text' not in request.get_json():
        abort(400, 'Missing text')
    all_places = storage.all("Place").values()
    place_obj = [obj.to_dict() for obj in all_places if obj.id == place_id]
    if place_obj == []:
        abort(404)
    all_users = storage.all("User").values()
    user_obj = [obj.to_dict() for obj in all_users if obj.id == user_id]
    if user_obj == []:
        abort(404)
    reviews = []
    new_review = Review(text=request.json['text'], place_id=place_id,
                        user_id=user_id)
    storage.new(new_review)
    storage.save()
    reviews.append(new_review.to_dict())
    return jsonify(reviews[0]), 201


@app_views.route('/reviews/<review_id>', methods=['GET'])
def get_review(review_id):
    '''Retrieves a Review object '''
    all_reviews = storage.all("Review").values()
    review_obj = [obj.to_dict() for obj in all_reviews if obj.id == review_id]
    if review_obj == []:
        abort(404)
    return jsonify(review_obj[0])


@app_views.route('/reviews/<review_id>', methods=['DELETE'])
def delete_review(review_id):
    '''Deletes a Review object'''
    all_reviews = storage.all("Review").values()
    review_obj = [obj.to_dict() for obj in all_reviews if obj.id == review_id]
    if review_obj == []:
        abort(404)
    review_obj.remove(review_obj[0])
    for obj in all_reviews:
        if obj.id == review_id:
            storage.delete(obj)
            storage.save()
    return jsonify({}), 200


@app_views.route('/reviews/<review_id>', methods=['PUT'])
def updates_review(review_id):
    '''Updates a Review object'''
    all_reviews = storage.all("Review").values()
    review_obj = [obj.to_dict() for obj in all_reviews if obj.id == review_id]
    if review_obj == []:
        abort(404)
    if not request.get_json():
        abort(400, 'Not a JSON')
    if 'text' in request.get_json():
        review_obj[0]['text'] = request.json['text']
        for obj in all_reviews:
            if obj.id == review_id:
                obj.text = request.json['text']
        storage.save()
    return jsonify(review_obj[0]), 200
=======
'''
Create a new view for Review objects - handles all default RESTful API
'''

from flask import abort, jsonify, request
from models.place import Place
from models.review import Review
from models.user import User
from api.v1.views import app_views
from models import storage


@app_views.route('/places/<place_id>/reviews', methods=['GET'],
                 strict_slashes=False)
def get_reviews_by_place(place_id):
    '''
    Retrieves the list of all Review objects of a Place
    '''
    place = storage.get(Place, place_id)
    if not place:
        abort(404)

    reviews = [review.to_dict() for review in place.reviews]
    return jsonify(reviews)


@app_views.route('/reviews/<review_id>', methods=['GET'],
                 strict_slashes=False)
def get_review(review_id):
    '''
    Retrieves a Review object
    '''
    review = storage.get(Review, review_id)
    if review:
        return jsonify(review.to_dict())
    else:
        abort(404)

@app_views.route('/reviews/<review_id>', methods=['DELETE'])
def delete_review(review_id):
    '''
    Deletes a Review object
    '''
    review = storage.get(Review, review_id)
    if review:
        storage.delete(review)
        storage.save()
        return jsonify({}), 200
    else:
        abort(404)


@app_views.route('/places/<place_id>/reviews', methods=['POST'],
                 strict_slashes=False)
def create_review(place_id):
    '''
    Creates a Review object
    '''
    place = storage.get(Place, place_id)
    if not place:
        abort(404)

    if not request.get_json():
        abort(400, 'Not a JSON')

    data = request.get_json()
    if 'user_id' not in data:
        abort(400, 'Missing user_id')
    if 'text' not in data:
        abort(400, 'Missing text')

    user = storage.get(User, data['user_id'])
    if not user:
        abort(404)

    data['place_id'] = place_id
    review = Review(**data)
    review.save()
    return jsonify(review.to_dict()), 201


@app_views.route('/reviews/<review_id>', methods=['PUT'], strict_slashes=False)
def update_review(review_id):
    '''
    Updates a Review object
    '''
    review = storage.get(Review, review_id)
    if review:
        if not request.get_json():
            abort(400, 'Not a JSON')

        data = request.get_json()
        ignore_keys = ['id', 'user_id', 'place_id', 'created_at', 'updated_at']
        for key, value in data.items():
            if key not in ignore_keys:
                setattr(review, key, value)

        review.save()
        return jsonify(review.to_dict()), 200
    else:
        abort(404)


@app_views.errorhandler(404)
def not_found(error):
    '''
    Returns 404: Not Found
    '''
    response = {'error': 'Not found'}
    return jsonify(response), 404


@app_views.errorhandler(400)
def bad_request(error):
    '''
    Return Bad Request message for illegal requests to the API
    '''
    response = {'error': 'Bad Request'}
    return jsonify(response), 400
>>>>>>> cc2987ccb05104f2811cea01580e3a34fd386551
