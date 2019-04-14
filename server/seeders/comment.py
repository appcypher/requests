""" Module for seeding comments in the database """
from models import Comment
from models.db import db


def seed_comment():
    """
    Adds comment seeds to the database
    """
    # Create seeds for comments
    comments = [
        Comment(message='Test message 1', request_id=1, staff_id=1),
        Comment(message='Test message 2', request_id=1, staff_id=2),
    ]

    # Save to the database
    db.session.add_all(comments)
    db.session.commit()
