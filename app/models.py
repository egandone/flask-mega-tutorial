from app import db
from datetime import datetime


class User(db.Model):
    id = db.Column('USER_ID', db.Integer, primary_key=True)
    username = db.Column('USER_NAME', db.String(64), index=True, unique=True)
    email = db.Column('USER_EMAIL', db.String(120), index=True, unique=True)
    password = db.Column('USER_PASSWORD', db.String(128))
    posts = db.relationship('Post', backref='author', lazy='dynamic')

    def __repr__(self):
        return f'<User {self.username}>'


class Post(db.Model):
    id = db.Column('POST_ID', db.Integer, primary_key=True)
    body = db.Column('POST_BODY', db.String(140))
    timestamp = db.Column('POST_WHEN', db.DateTime,
                          index=True, default=datetime.utcnow)
    user_id = db.Column('POST_USER_ID', db.Integer,
                        db.ForeignKey('user.USER_ID'))

    def __repr__(self):
        return '<Post {}>'.format(self.body)
