#!/usr/bin/python3
"""create blueprint"""
from flask import Blueprint

app_views = Blueprint('app_views', __name__, url_prefix='/api/v1')

<<<<<<< HEAD
=======

>>>>>>> cc2987ccb05104f2811cea01580e3a34fd386551
if app_views is not None:
    from api.v1.views.index import *
    from api.v1.views.states import *
    from api.v1.views.cities import *
    from api.v1.views.amenities import *
    from api.v1.views.users import *
    from api.v1.views.places import *
<<<<<<< HEAD
    from api.v1.views.places_reviews import *
    from api.v1.views.places_amenities import *
=======
    from api.v1.views.place_reviews import *
    from api.v1.place_amenities import *
>>>>>>> cc2987ccb05104f2811cea01580e3a34fd386551
