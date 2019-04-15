""" Module containing comment schema implementation. """
from marshmallow import fields
from middleware.validations import validate_string_length
from .base import BaseSchema
from .staff import StaffSchema


class CommentSchema(BaseSchema):
    """
    Comment schema for validating, serializing and deserializing Comment
    objects.
    """
    message = fields.String(validate=validate_string_length(60), required=True)
    staff_id = fields.Integer(required=True)
    request_id = fields.Integer(required=True)
    staff = fields.Nested(StaffSchema)
