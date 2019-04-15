""" Module for seeding requests in the database. """
from models import Request
from models.db import db
from datetime import datetime
from models.request import ProductArea


def seed_request():
    """
    Adds request seeds to the database.
    """
    # Create seeds for request
    requests = [
        Request(
            id=1,
            title='Test title',
            description='test description',
            product_area=ProductArea.CLAIMS,
            target_date=datetime.utcnow(),
            priority=1,
            staff_id=1,
            client_id=1,
        ),
    ]

    # Save to the database
    db.session.add_all(requests)
    db.session.commit()
