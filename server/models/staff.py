""" Module implementing Staff model """
from .db import db
from .base import BaseModel


class Staff(BaseModel):
    """
    Represents Staff database information
    """
    username = db.Column(db.String(60), unique=True, nullable=False)
    avatar_url = db.Column(db.String(250), nullable=False)
    comments = db.relationship('Comment', backref='staff', lazy='dynamic')

    def __repr__(self):
        return f'Client {vars(self)}'
