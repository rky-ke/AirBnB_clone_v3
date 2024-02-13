#!/usr/bin/python3
'''
    app for registering blueprint and starting flask
'''
import os
from flask import Flask, jsonify
from flask_cors import CORS
from models import storage
from api.v1.views import app_views

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "0.0.0.0"}})

app.register_blueprint(app_views)

@app.teardown_appcontext
def teardown(exception):
    '''
    close query after each session
    '''
    storage.close()

# Error handler for 404 Not Found
@app.errorhandler(404)
def not_found_error(error):
    '''
    return JSON formatted 404 status code response
    '''
    return jsonify({"error": "Not found"}), 404

if __name__ == "__main__":
    host = os.getenv("HBNB_API_HOST", "0.0.0.0")
    port = int(os.getenv("HBNB_API_PORT", 5000))
    app.run(host=host, port=port, threaded=True)
