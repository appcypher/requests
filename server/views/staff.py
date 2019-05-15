""" Module for staff view implementation. """
from flask_restplus import Resource
from models import Staff
from serializers import StaffSchema
from messages import messages
from .api import api


@api.route('/staff/<int:staff_id>')
class StaffEndpoint(Resource):
    """
    Endpoint for getting a staff information.
    """

    def get(self, staff_id):
        """
        Gets the staff with the specified id.

        Args:
            staff_id (int): staff id to fetch.
        """
        # Get the requested staff
        staff = Staff.find_by_id(staff_id)

        # Create a serialization schema
        staff_schema = StaffSchema(exclude=('created_at', 'updated_at'))

        return {
            'success': True,
            'message': messages['fetched']('staff'),
            'data': staff_schema.serialize(staff)
        }
