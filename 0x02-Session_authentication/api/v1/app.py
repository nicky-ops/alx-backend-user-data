#!/usr/bin/env python3
"""
Route module for the API
"""
from os import getenv
from api.v1.views import app_views
from flask import Flask, jsonify, abort, request
from flask_cors import (CORS, cross_origin)
import os


app = Flask(__name__)
app.register_blueprint(app_views)
CORS(app, resources={r"/api/v1/*": {"origins": "*"}})
auth = None
auth_type = getenv('AUTH_TYPE')

if auth_type == 'basic_auth':
    from api.v1.auth.basic_auth import BasicAuth
    auth = BasicAuth()
elif auth_type == 'session_auth':
    from api.v1.auth.session_auth import SessionAuth
    auth = SessionAuth()
else:
    from api.v1.auth.auth import Auth
    auth = Auth()


@app.errorhandler(404)
def not_found(error) -> str:
    """ Not found handler
    """
    return jsonify({"error": "Not found"}), 404


@app.errorhandler(401)
def unauthorized(error) -> str:
    '''
    Unauthorized handler
    '''
    return jsonify({"error": "Unauthorized"}), 401


@app.errorhandler(403)
def not_allowed(error) -> str:
    '''
    403 handler
    '''
    return jsonify({"error": "Forbidden"}), 403


@app.before_request
def before_request():
    '''
    This method handles before_request
    '''
    if auth is None:
        pass
    else:
        setattr(request, "current_user", auth.current_user(request))
        excluded_list = ['/api/v1/status/',
                         '/api/v1/unauthorized/', '/api/v1/forbidden/',
                         '/api/v1/auth_session/login/']

        if auth.require_auth(request.path, excluded_list):
            cookie = auth.session_cookie(request)
            if auth.authorization_header(request) is None and cookie is None:
                abort(401, description="Unauthorized")
            if auth.current_user(request) is None:
                abort(403, description='Forbidden')


if __name__ == "__main__":
    host = getenv("API_HOST", "0.0.0.0")
    port = getenv("API_PORT", "5000")
    app.run(host=host, port=port)
