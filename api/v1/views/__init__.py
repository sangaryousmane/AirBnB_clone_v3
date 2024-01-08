#!/usr/bin/python3
""" Create blueprint
"""
from flask import Blueprint

app_views = Blueprint('app_views', __name__, url_prefix='/api/v1')


if app_views is not None:
    from api.v1.views.index import *
    from api.v1.views.states import *
    from api.v1.views.cities import *
    from api.v1.views.amenities import *
    from api.v1.views.users import *
    from api.v1.views.places import *
    from api.v1.views.place_reviews import *
    from api.v1.place_amenities import *
