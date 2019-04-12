from .api import api
from flask import send_from_directory
from flask_restplus import Resource
from os import path


@api.route('/staff')
class Staff(Resource):
    def get(self):
        return {'success': False}
