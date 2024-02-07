#!/usr/bin/python3
"""
Create an endpoint that retrieves the number of each objects by type:
"""
from api.v1.views import app_views
from flask import jsonify
from models import storage


@app_views.route('/status', methods=['GET'])
def status():
    """
    Create JSON status
    """
    return jsonify({"status": "OK"})

@app_views.route('/stats', methods=['GET'])
def get_stats():
    """Get statistics about the number of objects by type"""
    stats = {}
    classes = ["Amenity", "City", "Place", "Review", "State", "User"]
    for cls in classes:
        count = storage.count(cls)
        stats[cls] = count
    return jsonify(stats)