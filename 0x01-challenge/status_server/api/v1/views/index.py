#!/usr/bin/python3
""" Index view
"""
from flask import jsonify
from flask import request
from api.v1.views import app_views


@app_views.route('/status', methods=['GET'], strict_slashes=False)
def status():
    """ Status of the web server
    """
    if request.method == 'GET':
        return jsonify({"status": "OK"})
