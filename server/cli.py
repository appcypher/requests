import click
from flask.cli import AppGroup

db_cli = AppGroup('model')


@db_cli.command('seed')
@click.argument('model')
def seed_model(model):
    click.echo('>>>>>>>> SEED MODEL!')
