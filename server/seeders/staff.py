""" Module for seeding staff in the database. """
from models import Staff
from models.db import db


def seed_staff():
    """
    Adds client staff to the database.
    """
    # Create seeds for staff
    staff = [
        Staff(id=1, username='Steve Akinyemi', avatar_url=''),
        Staff(id=2, username='James Cameron', avatar_url=''),
        Staff(id=3, username='John Does', avatar_url=''),
    ]

    # Save to the database
    db.session.add_all(staff)
    db.session.commit()
