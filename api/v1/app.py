#!/usr/bin/python3
""" create a file app """

from flask import Flask
from models import storage
from api.v1.views import app_views
from os import getenv
from flask import Flask, Blueprint, jsonify
from flask_cors import CORS


app = Flask(__name__)
app.register_blueprint(app_views)
cors = CORS(app, resources={r"/api/*": {"origins": "0.0.0.0"}})


if __name__ == "__main__":
    host = getenv("HBNB_API_HOST", "0.0.0.0")
    port = getenv("HBNB_API_PORT", "5000")
    app.run(
        host=host,
        port=int(port),
        threaded=True,
        debug=True)