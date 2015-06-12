import random
import string

from passlib.hash import sha256_crypt

from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.migrate import Migrate

from wsgi import app

db = SQLAlchemy(app)
migrate = Migrate(app, db)


class User(db.Model):
    __table__ = db.Table('users',
        db.Column('email', db.String(120), nullable=False),
        db.Column('salt', db.String(16), nullable=False),
        db.Column('password_hash', db.String(2048), nullable=False),
        db.PrimaryKeyConstraint('email', name='users_pk'),
    )

    @staticmethod
    def hash_password(plaintext, salt):
        return sha256_crypt.encrypt(plaintext, salt=salt)

    @staticmethod
    def random_salt():
        return "".join(random.choice(string.ascii_uppercase) for _ in range(16))

    @classmethod
    def verify_password(cls, plaintext, target_hash):
        return cls.hash_password(plaintext) == target_hash

    def __init__(self, email, password, salt=None):
        self.email = email
        self.salt = salt if salt is not None else self.__class__.random_salt()
        self.password_hash = self.__class__.hash_password(password, salt)

    def __repr__(self):
        return '<User %r>' % self.username

    def has_password(plaintext):
        return self.verify_password(plaintext, self.password_hash)
