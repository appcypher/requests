from .db import db
from .base import BaseModel
from enum import Enum


class ProductArea(Enum):
    POLICIES = 'POLICIES'
    BILLING = 'BILLING'
    CLAIMS = 'CLAIMS'
    REPORTS = 'REPORTS'


class Request(BaseModel):
    title = db.Column(db.String(250), nullable=False)
    description = db.Column(db.String(250), nullable=False)
    product_area = db.Column(db.Enum(ProductArea), nullable=False)
    target_date = db.Column(db.DateTime(timezone=True), nullable=False)
    priority = db.Column(db.Integer, nullable=False)
    staff_id = db.Column(db.Integer, db.ForeignKey('staff.id'), nullable=False)
    client_id = db.Column(db.Integer,
                          db.ForeignKey('client.id'),
                          nullable=False)  # Requesting client
    comments = db.relationship('Comment', backref='request', lazy='dynamic')

    def __repr__(self):
        return f'Request {vars(self)}'
