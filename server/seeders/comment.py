""" Module for seeding comments in the database. """
from models import Comment
from models.db import db


def seed_comment():
    """
    Adds comment seeds to the database.
    """
    # Create seeds for comments.
    comments = [
        Comment(
            message='I will be working on this soon', request_id=12, staff_id=1
        ),
        Comment(
            message='I think we should wait for confirmation',
            request_id=12,
            staff_id=2
        ),
        Comment(
            message='How long will the Paypal support take?',
            request_id=2,
            staff_id=2
        ),
        Comment(
            message='Using other similar sprint, I\'m guessing one week?',
            request_id=3,
            staff_id=3
        ),
        Comment(
            message='I will be working on this soon', request_id=4, staff_id=1
        ),
        Comment(
            message='I think we should wait for confirmation',
            request_id=5,
            staff_id=2
        ),
        Comment(
            message='How long will the Paypal support take?',
            request_id=6,
            staff_id=2
        ),
        Comment(
            message='How long will the Paypal support take?',
            request_id=1,
            staff_id=2
        ),
        Comment(
            message='Using other similar sprint, I\'m guessing one week?',
            request_id=7,
            staff_id=3
        ),
        Comment(
            message='I will be working on this soon', request_id=12, staff_id=1
        ),
        Comment(
            message='I think we should wait for confirmation',
            request_id=1,
            staff_id=2
        ),
        Comment(
            message='You are right. Let\'s do that', request_id=11, staff_id=2
        ),
        Comment(
            message='How long will the Paypal support take?',
            request_id=1,
            staff_id=2
        ),
        Comment(
            message='Using other similar sprint, I\'m guessing one week?',
            request_id=3,
            staff_id=3
        ),
    ]

    # Save to the database.
    db.session.add_all(comments)
    db.session.commit()
