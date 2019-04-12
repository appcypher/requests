from .db import db
from .base import BaseModel


class Comment(BaseModel):
    message = db.Column(db.String(250), nullable=False)
    staff_id = db.Column(db.Integer, db.ForeignKey('staff.id'), nullable=False)
    request_id = db.Column(db.Integer,
                           db.ForeignKey('request.id'),
                           nullable=False)

    def __repr__(self):
        return f'Request {vars(self)}'
