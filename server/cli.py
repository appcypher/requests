""" Module for flask commandline extension. """
import click
from flask.cli import AppGroup
from seeders import (seed_client, seed_comment, seed_request, seed_staff)

db_cli = AppGroup('model')


@db_cli.command('seed')
@click.argument('model')
def seed_model(model):
    """
    Seeds a model to the database.

    Args:
        model (str): database model.
    """
    if model == 'all':
        seed_all()
    elif model == 'client':
        seed_client()
    elif model == 'comment':
        seed_comment()
    elif model == 'staff':
        seed_staff()
    elif model == 'request':
        seed_request()


def seed_all():
    """
    Seeds all models to the database.

    Args:
        model (str): database model.

    Note:
        Order of seed function calls is important
    """
    seed_client()
    seed_staff()
    seed_request()
    seed_comment()
