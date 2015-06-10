import os

from furl import furl

from flask import Flask


DATABASE_NAME = os.environ['DATABASE_NAME']
DATABASE_USER = os.environ['DATABASE_USER']
DATABASE_PASSWORD = os.environ['DATABASE_PASSWORD']
DATABASE_HOST = os.environ['DATABASE_HOST']
DATABASE_PORT = os.environ['DATABASE_PORT']

DATABASE_URI = furl().set(scheme='postgres') \
    .set(username=DATABASE_USER) \
    .set(password=DATABASE_PASSWORD) \
    .set(host=DATABASE_HOST) \
    .set(port=DATABASE_PORT) \
    .set(path=DATABASE_NAME)


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = str(DATABASE_URI)
