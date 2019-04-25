""" Module for seeding clients in the database. """
from models import Client
from models.db import db


def seed_client():
    """
    Adds client seeds to the database.
    """
    # Create seeds for clients.
    clients = [
        Client(
            id=1,
            username='Client A',
            avatar_url=(
                'https://github.com/appcypher/experiments/blob/master/images/'
                'client-a.jpg?raw=true'
            )
        ),
        Client(
            id=2,
            username='Client B',
            avatar_url=(
                'https://github.com/appcypher/experiments/blob/master/images/'
                'client-b.jpg?raw=true'
            )
        ),
        Client(
            id=3,
            username='Client C',
            avatar_url=(
                'https://github.com/appcypher/experiments/blob/master/images/'
                'client-c.jpg?raw=true'
            )
        ),
    ]

    # Save to the database.
    db.session.add_all(clients)
    db.session.commit()
