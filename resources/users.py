from fns.api import FnsApi
from app import db
from data.models import User
from parsers.users import parser_create
from flask import jsonify, make_response
from flask_restful import Resource, abort


def abort_if_user_not_found(phone):
    session = db.session
    user = session.query(User).filter(User.phone == phone).first()
    session.close()
    if not user:
        abort(404, message=f"user not found")


class UsersResource(Resource):
    def get(self, phone):
        phone = str(phone)[1:]
        abort_if_user_not_found(phone)
        session = db.session
        user = session.query(User).filter(User.phone == phone).first()
        session.close()
        return jsonify({"user": user.to_dict(only=(
            "phone", "email", "name"
        ))})

    def delete(self, phone):
        phone = str(phone)[1:]
        abort_if_user_not_found(phone)
        session = db.session
        user = session.query(User).filter(User.phone == phone).first()
        session.delete(user)
        session.commit()
        session.close()
        return jsonify({"success": "OK"})


class UsersListResource(Resource):
    def get(self):
        session = db.session
        users = session.query(User).all()
        session.close()
        return jsonify({"users": [item.to_dict(
            only=("phone", "email", "name")
        ) for item in users]})

    def post(self):
        args = parser_create.parse_args()
        session = db.session
        phone = args["phone"][1:]
        email = args["email"]
        name = args["name"]
        if session.query(User).filter(User.phone == phone).first():
            session.close()
            return jsonify({"result": "user exists"})

        result = FnsApi.register(phone, email, name)
        if result.status_code == 204:
            user = User(phone=phone, name=name, email=email)
            session.add(user)
            session.commit()
            session.close()
            return jsonify({"result": "success"})
        session.close()
        return make_response({"result": result.text}, result.status_code)
