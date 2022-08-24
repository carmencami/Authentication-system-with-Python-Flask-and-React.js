from flask import Flask, request, jsonify, url_for, Blueprint

from api.models import db, User
from api.utils import generate_sitemap, APIException
from flask_jwt_extended import create_access_token
api = Blueprint('api', __name__)

@api.route('/hello', methods=['POST', 'GET'])
def handle_hello():

    response_body = {
        "message": "Hello! I'm a message that came from the backend, check the network tab on the google inspector and you will see the GET request"
    }
    return jsonify(response_body), 200
@api.route('/login', methods=['POST', 'GET'])
def login():
    email = request.json.get("email")
    password = request.json.get("password")
    user = User.query.filter_by(email=email).first()
    print(email)
    if user:
        if password != user.password:
            return jsonify({"msg": "contraseña invalida"}), 401
    else:
        return jsonify({"msg": "email invalida"}), 401
    response_body = {
        "mensage": "login"
    }
    return jsonify(response_body), 200 (editado) 







