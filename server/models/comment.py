""" Module implementing the Comment model. """
from .db import db
from .base import BaseModel


class Comment(BaseModel):
    """
    Represents comment database information.
    """
    message = db.Column(db.String(250), nullable=False)
    # Relationships
    staff_id = db.Column(db.Integer, db.ForeignKey('staff.id'), nullable=False)
    request_id = db.Column(
        db.Integer, db.ForeignKey('request.id'), nullable=False
    )
    staff = db.relationship('Staff', back_populates="comments")
    request = db.relationship('Request', back_populates="comments")
