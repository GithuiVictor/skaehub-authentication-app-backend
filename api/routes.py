import os
from flask import Flask, request, jsonify, url_for, Blueprint
from werkzeug.exceptions import MethodNotAllowed
from werkzeug.wrappers import response
from flask_jwt_extended import create_access_token
from flask_jwt_extended import get_jwt_identity
from flask_jwt_extended import jwt_required
from flask_jwt_extended import JWTManager

#Create Flask App
api = Blueprint('api', __name__)

# Setup the Flask-JWT-Extended extension
api.config["JWT_SECRET_KEY"] = os.getEnv('JWT_SECRET')
jwt = JWTManager(api)

# Create a route to authenticate your users and return JWTs. The
# create_access_token() function is used to actually generate the JWT.
@api.route("/token", methods=["POST"])
def create_token():
    email = request.json.get("email", None)
    password = request.json.get("password", None)
    if email != "test" or password != "test":
        return jsonify({"msg": "Bad username or password"}), 401

    access_token = create_access_token(identity=email)
    return jsonify(access_token=access_token)