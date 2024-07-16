#!/usr/bin/env python3
'''
Basic Flask app
'''
from flask import Flask
from flask import jsonify, request, abort, make_response
from auth import Auth


app = Flask(__name__)
AUTH = Auth()


@app.route("/", methods=["GET"])
def home():
    """
    returns a JSON payload for the endpoint
    """
    return jsonify({"message": "Bienvenue"})


@app.route("/users", methods=["POST"])
def users() -> str:
    '''
    Register a user
    '''
    email = request.form.get('email')
    password = request.form.get('password')
    try:
        user = AUTH.register_user(email, password)
        return jsonify({"email": user.email, "message": "user created"})
    except Exception:
        return jsonify({"message": "email already registered"}), 400


@app.route("/sessions", methods=["POST"])
def sessions() -> str:
    '''
    Route to respond to the post session route
    '''
    email = request.form.get('email')
    password = request.form.get('password')
    if AUTH.valid_login(email, password):
        new_session_id = AUTH.create_session(email)
        response = make_response(jsonify({"email": email,
                                          "message": "logged in"}))
        response.set_cookie("session_id", new_session_id)
        return response
    else:
        abort(401)


@app.route("/sessions", methods=["DELETE"])
def logout() -> str:
    '''
    logout function
    '''
    try:
        session_id = request.cookies.get('session_id')
        if session_id is None:
            abort(403)
        user = AUTH.get_user_from_session_id(session_id)
        if not user:
            abort(403)
        else:
            AUTH.destroy_session(user.id)
            return redirect("/")
    except Exception:
        abort(403)


@app.route("/profile", methods=["GET"])
def profile() -> str:
    '''
    retrive a user profile
    '''
    session_id = request.cookies.get('session_id')
    user = AUTH.get_user_from_session_id(session_id)
    if session_id is None or user is None:
        abort(403)
    else:
        return jsonify({"email": user.email}), 200


@app.route("/reset_password", methods=["POST"])
def get_reset_password_token() -> str:
    '''
    This method implements a route to get the reset password token
    '''
    email = request.form.get('email')
    try:
        user = AUTH._db.find_user_by(email=email)
        if user is None:
            abort(403)
        else:
           reset_token = AUTH.get_reset_password_token(email)
            return jsonify({"email": user.email, "reset_token": reset_token})
    except Exception:
        abort(403)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
