#!/usr/bin/python3
""" Restful index
"""
from api.v1.views import app_views
from flask import jsonify, make_response


@app_views.route('/status', methods=['GET'])
def status_response():
    """ status OK
    """
    return jsonify({"status": 'OK'})

