from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.migrate import Migrate

from wsgi import app

db = SQLAlchemy(app)
migrate = Migrate(app, db)


class User(db.Model):
    email = db.Column(db.String(120), primary_key=True, unique=True, nullable=False)
    password_hash = db.Column(db.String(2048), nullable=False)

    def __init__(self, email):
        self.email = email
        self.password_hash = 'asdasd'

    def __repr__(self):
        return '<User %r>' % self.username
