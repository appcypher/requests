from .api import api
from flask import send_from_directory
from flask_restplus import Resource
from os import path


@api.route('/clients')
class Client(Resource):
    def get(self):
        return {'success': False}
