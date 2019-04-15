""" Module containing request schema implementation."""
from marshmallow import fields, post_load
from middleware.validations import validate_string_length, validate_priority
from marshmallow_enum import EnumField
from models.request import ProductArea
from .base import BaseSchema
from .staff import StaffSchema
from .comment import CommentSchema


class RequestSchema(BaseSchema):
    """
    Request schema for validating, serializing and deserializing Request
    objects.
    """
    title = fields.String(validate=validate_string_length(60), required=True)
    decription = fields.String(validate=validate_string_length(250),
                               required=True)
    product_area = EnumField(ProductArea, required=True)
    target_date = fields.DateTime(required=True)
    priority = fields.Integer(required=True)
    client_id = fields.Integer(required=True)
    staff_id = fields.Integer(required=True)
    comments = fields.Integer(required=True)
    staff = fields.Nested(StaffSchema())
    comments = fields.Nested(CommentSchema())

    @post_load
    def validate(self, data):
        """
        Holds post load validations for Request schema
        """
        validate_priority(client_id=data['client_id'],
                          priority=data['priority'])
