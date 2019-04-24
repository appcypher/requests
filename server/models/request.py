""" Module implementing Requests model. """
from enum import Enum
from .db import db
from .base import BaseModel


class ProductArea(Enum):
    """
    Represents the range of allowed product area.
    """
    POLICIES = 'POLICIES'
    BILLING = 'BILLING'
    CLAIMS = 'CLAIMS'
    REPORTS = 'REPORTS'


class Request(BaseModel):
    """
    Represents request database information.
    """
    title = db.Column(db.String(250), nullable=False)
    description = db.Column(db.String(250), nullable=False)
    product_area = db.Column(db.Enum(ProductArea), nullable=False)
    target_date = db.Column(
        db.DateTime(timezone=True), nullable=False
    )
    priority = db.Column(db.Integer, nullable=True)
    resolved = db.Column(db.Boolean, default=False)
    # Relationships
    staff_id = db.Column(db.Integer, db.ForeignKey('staff.id'), nullable=False)
    client_id = db.Column(
        db.Integer, db.ForeignKey('client.id'), nullable=False
    )
    client = db.relationship('Client', back_populates='requests')
    staff = db.relationship('Staff', back_populates='requests')
    comments = db.relationship('Comment', back_populates='request')
