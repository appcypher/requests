""" Module for seeding clients in the database """
from models import Client
from models.db import db


def seed_client():
    """
    Adds client seeds to the database
    """
    # Create seeds for clients
    clients = [
        Client(id=1, username='Client A', avatar_url=''),
        Client(id=2, username='Client B', avatar_url=''),
        Client(id=3, username='Client C', avatar_url=''),
    ]

    # Save to the database
    db.session.add_all(clients)
    db.session.commit()
