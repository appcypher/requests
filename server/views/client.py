""" Module containing client view implementation. """
from flask_restplus import Resource
from models import Client
from serializers import ClientSchema
from messages import messages
from .api import api


@api.route('/clients/<int:client_id>')
class ClientEndpoint(Resource):
    """
    Endpoint for getting a client.
    """

    def get(self, client_id):
        client = Client.find_by_id(client_id)
        client_schema = ClientSchema(exclude=('created_at', 'updated_at'))
        return {
            'success': True,
            'message': messages['fetched']('client'),
            'data': client_schema.serialize(client)
        }
