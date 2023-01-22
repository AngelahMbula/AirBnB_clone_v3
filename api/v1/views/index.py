#!/usr/bin/python3
"""Index file with route information for general requests"""
from models import storage
from flask import jsonify
from api.v1.views import app_views


@app_views.route("/", strict_slashes=False)
def index():
    """index route of app"""
    return "No entries here so far\n"


@app_views.route("/status", strict_slashes=False)
def status():
    """status method to return status to api request"""
    return jsonify(status="OK")


@app_views.route('/stats', methods=['GET'], strict_slashes=False)
def number_objects():
    """ Retrieves the number of each objects by type """
    classes = [Amenity, City, Place, Review, State, User]
    names = ["amenities", "cities", "places", "reviews", "states", "users"]

    num_objs = {}
    for i in range(len(classes)):
        num_objs[names[i]] = storage.count(classes[i])

    return jsonify(num_objs)
