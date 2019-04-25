""" Module for seeding requests in the database. """
from models import Request
from models.db import db
from datetime import datetime, timedelta
from models.request import ProductArea


def seed_request():
    """
    Adds request seeds to the database.
    """

    today = datetime.utcnow()
    yesterday = datetime.now() - timedelta(1)
    before_yesterday = datetime.now() - timedelta(2)
    way_before_yesterday = datetime.now() - timedelta(3)
    future_day = datetime.now() + timedelta(20)

    # Create seeds for request.
    requests = [
        Request(
            title='Add option for clearing transactions or archiving them'
            ' transactions',
            description='People want to be able to clear old'
            ' transaction list to reduce UI clutter. This will require'
            ' the frontend and backend team working together to create'
            ' a new user experience',
            product_area=ProductArea.CLAIMS,
            target_date=future_day,
            created_at=today,
            priority=2,
            staff_id=2,
            client_id=3,
            id=12,
            resolved=True,
        ),
        Request(
            title='Improve customer care services to reduce client churn',
            description='The current customer care services are reported to '
            ' be abysmal with representatives dropping calls on customer or '
            ' being rather unpleasant. ',
            product_area=ProductArea.POLICIES,
            target_date=today,
            created_at=way_before_yesterday,
            priority=1,
            staff_id=1,
            client_id=1,
        ),
        Request(
            title='Fix issue with the customisation section. It hangs'
            ' sometimes and breaks immersion',
            description='People want to be able to clear old'
            ' transaction list to reduce UI clutter',
            product_area=ProductArea.CLAIMS,
            target_date=today,
            created_at=before_yesterday,
            priority=7,
            staff_id=3,
            client_id=3,
        ),
        Request(
            title='Create a new option to make payment vis Visa to open door'
            ' to new clients',
            description='The current customer care services are reported to'
            ' be abysmal with representatives dropping calls on customer or'
            ' being rather unpleasant. ',
            product_area=ProductArea.POLICIES,
            target_date=future_day,
            created_at=before_yesterday,
            priority=2,
            staff_id=3,
            client_id=1,
        ),
        Request(
            title='Add PayPal payment support and improve payment systems',
            description='People want to be able to purchase'
            ' using PayPal. We need to also imptove the existing PayStack'
            ' support to allow new implementation and get rid of old crust',
            product_area=ProductArea.BILLING,
            target_date=future_day,
            created_at=before_yesterday,
            priority=1,
            staff_id=2,
            client_id=2,
            resolved=True,
        ),
        Request(
            title='Remove old UI feature that prevents clients from making'
            ' withdrawals on Sunday',
            description='People want to be able to purchase'
            ' using his PayPal.',
            product_area=ProductArea.BILLING,
            target_date=future_day,
            created_at=before_yesterday,
            priority=3,
            staff_id=2,
            client_id=2,
        ),
        Request(
            title='Add a chat section. We need to be able discuss about'
            ' products and interests',
            description='People want to be able to clear old'
            ' transaction list to reduce UI clutter',
            product_area=ProductArea.CLAIMS,
            target_date=today,
            created_at=yesterday,
            priority=5,
            staff_id=2,
            client_id=3,
        ),
        Request(
            title='Add shopping cart to make it easy for clients to keep logs'
            ' of interested items',
            description='People want to be able to purchase'
            ' using their PayPal. We need',
            product_area=ProductArea.BILLING,
            target_date=future_day,
            created_at=yesterday,
            priority=1,
            staff_id=2,
            client_id=3,
            resolved=True,
        ),
        Request(
            title='Add a ratings system to make it possible to rate sellers'
            ' based on their past services.',
            description='The current customer care services are reported to'
            ' be abysmal with representatives dropping calls on customer or'
            ' being rather unpleasant. ',
            product_area=ProductArea.POLICIES,
            target_date=today,
            created_at=yesterday,
            priority=6,
            staff_id=2,
            client_id=2,
        ),
        Request(
            title='Make it possible for users to wipe all their data on the'
            ' platform if they choose to do so',
            description='People want to be able to purchase'
            ' using PayPal. We need to also imptove the existing PayStack'
            ' support to allow new implementation and get rid of old crust',
            product_area=ProductArea.CLAIMS,
            target_date=future_day,
            created_at=yesterday,
            priority=4,
            staff_id=2,
            client_id=3,
            resolved=True,
        ),
        Request(
            title='Implement payment sharing feature to allow clients share'
            ' payment of items',
            description='The current customer care services are reported to'
            ' be abysmal with representatives dropping calls on customer or'
            ' being rather unpleasant. ',
            product_area=ProductArea.POLICIES,
            target_date=future_day,
            created_at=today,
            priority=3,
            staff_id=2,
            client_id=3,
        ),
        Request(
            title='Create a portfolio section for allowing sellers to showcase'
            ' their experience in the sale of a particular good',
            description='People want to be able to purchase'
            ' using PayPal. We need to also imptove the existing PayStack'
            ' support to allow new implementation and get rid of old crust',
            product_area=ProductArea.BILLING,
            target_date=future_day,
            created_at=today,
            priority=4,
            staff_id=2,
            client_id=2,
            resolved=True,
        ),
    ]

    # Save to the database.
    db.session.add_all(requests)
    db.session.commit()
