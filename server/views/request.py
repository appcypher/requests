""" Module for request view implementation. """
from models import Request, Comment
from serializers import RequestSchema, CommentSchema
from messages import messages
from flask_restplus import Resource
from flask import request
from .api import api


@api.route('/requests')
class RequestEndpoint(Resource):
    """
    Endpoint for getting and creating requests.
    """

    def get(self):
        """
        Gets all feature requests.
        """
        # Get all requests
        request = Request.get_all()

        # Create a serialization schema
        request_schema = RequestSchema(
            exclude=('staff', 'comments'), many=True
        )
        return {
            'success': True,
            'message': messages['fetched']('requests'),
            'data': request_schema.serialize(request)
        }

    def post(self):
        """
        Adds a new request to the database.
        """
        # Convert request to dictionary
        request_dict = request.get_json() or {}

        # Create (de)serialization schema
        request_schema = RequestSchema(exclude=('created_at', 'updated_at'))

        # Deserialize for validation
        request_data = request_schema.deserialize(request_dict)

        # Save data to the database
        save_request(request_data)

        return {
            'success': True,
            'message': messages['created']('request'),
            'data': request_schema.serialize(request_data),
        }, 201


def save_request(request_data):
    """
    Reorders entries for a client if priority already exists and
    saves new request.

    Args:
        request_data (dict): request data to be saved.
    """
    priority = request_data['priority']
    client_id = request_data['client_id']

    # Check for row with similar priority
    request = Request.query.filter_by(client_id=client_id,
                                      priority=priority).all()
    # Update every duplicate we find.
    while request:
        # Increment priority.
        priority += 1

        # Check for row with the newly updated priority value.
        new_request = Request.query.filter_by(
            client_id=client_id, priority=priority
        ).all()

        # Update request with previous priority value.
        request[0].update(priority=priority)

        # Update request
        request = new_request

    Request(**request_data).save()


@api.route('/requests/<int:request_id>')
class SingleRequestEndpoint(Resource):
    """
    Endpoint for getting a single request.
    """

    def get(self, request_id):
        """
        Gets a specific request feature request and associated comments.
        """
        # Get the requested request
        request = Request.find_by_id(request_id)

        # Create a serialization schema
        request_schema = RequestSchema(exclude=('updated_at'))

        return {
            'success': True,
            'message': messages['fetched']('request'),
            'data': request_schema.serialize(request)
        }


@api.route('/requests/<int:request_id>/comments')
class RequestCommentsEndpoint(Resource):
    """
    Endpoint for getting or adding comments to a request.
    """

    def get(self, request_id):
        """
        Gets all the comments under a request.
        """
        # Get the requested comment
        comments = Request.find_by_id(request_id).comments

        # Create a serialization schema
        comments_schema = CommentSchema(exclude=('updated_at'), many=True)

        return {
            'success': True,
            'message': messages['fetched']('comments'),
            'data': comments_schema.serialize(comments)
        }

    def post(self, request_id):
        """
        Adds a comment under specified request.

        Args:
            request_id (int): request id to fetch.
        """
        # Convert request to dictionary
        request_dict = request.get_json() or {}

        # Add request_id field
        request_dict['request_id'] = request_id

        # Create (de)serialization schema
        comment_schema = CommentSchema(exclude=('created_at', 'updated_at'))

        # Deserialize for validation
        comment_data = comment_schema.deserialize(request_dict)

        # Save data to the database
        Comment(**comment_data).save()

        return {
            'success': True,
            'message': messages['created']('comment'),
            'data': comment_schema.serialize(comment_data),
        }, 201
