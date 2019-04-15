""" Module implementing Staff model. """
from .db import db
from .base import BaseModel


class Staff(BaseModel):
    """
    Represents Staff database information.
    """
    username = db.Column(db.String(60), unique=True, nullable=False)
    avatar_url = db.Column(db.String(250), nullable=False)
    # Relationships
    comments = db.relationship('Comment', back_populates='staff')
    requests = db.relationship('Request', back_populates='staff')
