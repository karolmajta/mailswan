from flask_restful import Resource, Api

from wsgi import app
import db

api = Api(app)
session = db.db.session

class User(Resource):
    def put(self, email):
        user = db.User(email=email)
        session.add(user)
        session.commit()
        return {'email': email}

api.add_resource(User, '/user/<email>')
