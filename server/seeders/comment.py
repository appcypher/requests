from models import Comment
from models.db import db


def seed_comment():
    comments = [
        Comment(message='Test message 1', request_id=1, staff_id=1),
        Comment(message='Test message 2', request_id=1, staff_id=2),
    ]
    db.session.add_all(comments)
    db.session.commit()
