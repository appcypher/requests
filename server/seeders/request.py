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
            title='Improve customer care services',
            description='The current customer care services are reported to '
            'be abysmal with representatives dropping calls on customer or '
            'being rather unpleasant.',
            product_area=ProductArea.POLICIES,
            target_date=datetime.utcnow(),
            priority=1,
            staff_id=1,
            client_id=1,
        ),
        Request(
            title='Add PayPal payment support',
            description='Client B wants to be able to purchase '
            'using his PayPal ',
            product_area=ProductArea.BILLING,
            target_date=datetime.utcnow(),
            priority=1,
            staff_id=2,
            client_id=2,
        ),
        Request(
            title='Add option for clearing transactions',
            description='Client B wants to be able to clear old '
            'transaction list to reduce UI clutter',
            product_area=ProductArea.CLAIMS,
            target_date=datetime.utcnow(),
            priority=2,
            staff_id=2,
            client_id=3,
        ),
    ]

    # Save to the database
    db.session.add_all(requests)
    db.session.commit()
