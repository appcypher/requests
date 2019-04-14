""" Module containing client view implementation """
from .api import api
from flask_restplus import Resource


@api.route('/clients/<int:client_id>')
class Client(Resource):
    """
    Endpoint for getting a client
    """
    def get(self, client_id):
        return {'success': False}
