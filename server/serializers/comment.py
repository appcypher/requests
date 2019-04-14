""" Module containing comment schema implementation """
from marshmallow import fields
from .base import BaseSchema
from middleware.validations import validate_string_length


class CommentSchema(BaseSchema):
    """
    Serialization specification for comment schema
    """
    message = fields.String(validate=validate_string_length(60), required=True)
    staff_id = fields.Integer(required=True)
    request_id = fields.Integer(required=True)
