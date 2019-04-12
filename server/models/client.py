from .db import db
from .base import BaseModel


class Client(BaseModel):
    username = db.Column(db.String(60), unique=True, nullable=False)
    avatar_url = db.Column(db.String(250), nullable=False)

    def __repr__(self):
        return f'Client {vars(self)}'
