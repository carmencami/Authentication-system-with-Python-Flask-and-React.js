from flask import Flask, request, jsonify, url_for, Blueprint

from api.models import db, User
from api.utils import generate_sitemap, APIException
from flask_jwt_extended import create_access_token, get_jwt_identity, jwt_required
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
    if not user:
        return jsonify({"msg":"información incorrecta"})
    else:
        token = create_access_token(identity=user.id)  
        response_body = {
            "mensage": "login", "token":token
        }
        return jsonify(response_body), 200 

@api.route('/register', methods=['POST'])
def register():
    email = request.json.get("email")
    password = request.json.get("password")
    user = User(email=email, password=password)
    print(email)
    if user:
        db.session.add(user)
        db.session.commit()
        return jsonify({"user":user.serialize()})
    else:
        return jsonify({"msg":"usuario no creado"})
@api.route('/private', methods=['GET'])
@jwt_required()
def private():
    user_id=get_jwt_identity()
    user=User.query.get(user_id)
    if not user:
        return jsonify({"msg":"inicie sesión", "loged":False})
    else:
        return jsonify({"loged":True, "user":user.serialize()})







