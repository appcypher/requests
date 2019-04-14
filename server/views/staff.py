""" Module for staff view implementation """
from .api import api
from flask import send_from_directory
from flask_restplus import Resource
from os import path


@api.route('/staff/<int:staff_id>')
class Staff(Resource):
    """
    Endpoint for getting the staff
    """
    def get(self, staff_id):
        return {'success': False}
