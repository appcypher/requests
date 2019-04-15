""" Module for request view implementation. """
from flask_restplus import Resource
from .api import api


@api.route('/requests')
class RequestEndpoint(Resource):
    """
    Endpoint for getting and creating requests.
    """

    def get(self):
        return {'success': False}

    def post(self):
        return {'success': False}


@api.route('/requests/<int:request_id>')
class SingleRequestEndpoint(Resource):
    """
    Endpoint for getting a single request.
    """

    def get(self, request_id):
        return {'success': False}


@api.route('/requests/<int:request_id>/comments')
class RequestCommentsEndpoint(Resource):
    """
    Endpoint for getting or  adding comments to a request.
    """

    def get(self, request_id):
        return {'success': False}

    def post(self, request_id):
        return {'success': False}
