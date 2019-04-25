""" Module for seeding staff in the database. """
from models import Staff
from models.db import db


def seed_staff():
    """
    Adds client staff to the database.
    """
    # Create seeds for staff.
    staff = [
        Staff(
            id=1,
            username='Steve Akinyemi',
            avatar_url=(
                'https://github.com/appcypher/experiments/blob/master/images/'
                'staff-1.jpg?raw=true'
            )
        ),
        Staff(
            id=2,
            username='Anu Johnson',
            avatar_url=(
                'https://github.com/appcypher/experiments/blob/master/images/'
                'staff-2.jpg?raw=true'
            )
        ),
        Staff(
            id=3,
            username='James Waldo',
            avatar_url=(
                'https://github.com/appcypher/experiments/blob/master/images/'
                'staff-3.jpg?raw=true'
            )
        ),
    ]

    # Save to the database.
    db.session.add_all(staff)
    db.session.commit()
