""" Module for staff view implementation. """
from flask import send_from_directory
from flask_restplus import Resource
from os import path
from .api import api


@api.route('/staff/<int:staff_id>')
class StaffEndpoint(Resource):
    """
    Endpoint for getting a staff information.
    """

    def get(self, staff_id):
        return {'success': False}
