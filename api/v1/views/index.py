#!/usr/bin/python3
""" create a file index.py """

from api.v1.views import app_views
from flask import jsonify
from models import storage
from models.state import State
from models.amenity import Amenity
from models.city import City
from models.review import Review
from models.place import Place
from models.user import User


@app_views.route('/status')
def views_jason():
    return jsonify({'status': 'OK'})


@app_views.route('/stats')
def views_stats():
    data = {
        "amenities": storage.count(Amenity),
        "cities": storage.count(City),
        "places": storage.count(Place),
        "reviews": storage.count(Review),
        "states": storage.count(State),
        "users": storage.count(User)
    }

    return jsonify(data)
