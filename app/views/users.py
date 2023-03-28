from flask_restx import Namespace, Resource
from app.container import user_service
from app.dao.model.user import UserSchema
from flask import request

from app.helpers.decorations import auth_required

user_ns = Namespace("user")

user_schema = UserSchema()
users_schema = UserSchema(many=True)


@user_ns.route("/")
class UsersView(Resource):

    def get(self):
        return users_schema.dump(user_service.get_all()), 200

    def post(self):
        req_data = request.json
        user_service.create(req_data)
        return "", 201


@user_ns.route("/<int:uid>/")
class UserView(Resource):

    def get(self, uid):
        return user_schema.dump(user_service.get_one(uid)), 200

    # @auth_required
    def patch(self, uid):
        data = request.json
        user_service.update(data, uid)
        return "", 204


@user_ns.route("/password/")
class UserViewPassword(Resource):
    def put(self, uid):
        data = request.json
        user_service.update(data, uid)
        return "", 204
