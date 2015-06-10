from flask.ext.flask_restful import Resource, Api

from wsgi import app

api = Api(app)

class HelloWorld(Resource):
    def get(self):
        return {'hello': 'world'}

api.add_resource(HelloWorld, '/')
