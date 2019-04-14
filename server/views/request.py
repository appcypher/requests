""" Module for request view implementation """
from .api import api
from flask_restplus import Resource


@api.route('/requests')
class Request(Resource):
    """
    Endpoint for getting and creating requests
    """
    def get(self):
        return {'success': False}

    def post(self):
        return {'success': False}


@api.route('/requests/<int:request_id>')
class SingleRequest(Resource):
    """
    Endpoint for getting and creating a single request
    """
    def get(self, request_id):
        return {'success': False}


@api.route('/requests/<int:request_id>/comments')
class RequestComments(Resource):
    """
    Endpoint for getting or  adding comments to a request
    """
    def get(self, request_id):
        return {'success': False}

    def post(self, request_id):
        return {'success': False}
