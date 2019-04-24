""" Module containing request schema implementation."""
from marshmallow import fields, post_load
from marshmallow_enum import EnumField
from models.request import ProductArea
from models import Client, Staff
from middleware.validations import (
    validate_string_length, validate_priority, validate_id,
    validate_date
)
from .base import BaseSchema
from .staff import StaffSchema
from .comment import CommentSchema
from .client import ClientSchema


class RequestSchema(BaseSchema):
    """
    Request schema for validating, serializing and deserializing Request
    objects.
    """
    title = fields.String(validate=validate_string_length(60), required=True)
    description = fields.String(
        validate=validate_string_length(250), required=True
    )
    product_area = EnumField(ProductArea, by_value=True, required=True)
    target_date = fields.DateTime(validate=validate_date, required=True)
    priority = fields.Integer(required=True)
    client_id = fields.Integer(validate=validate_id(Client), required=True)
    staff_id = fields.Integer(validate=validate_id(Staff), required=True)
    comments = fields.Integer(required=True)
    resolved = fields.Bool(dump_only=False)
    client = fields.Nested(ClientSchema())
    staff = fields.Nested(StaffSchema())
    comments = fields.Nested(CommentSchema(), many=True)

    @post_load
    def validate(self, data):
        """
        Holds post load validations for Request schema
        """
        validate_priority(
            client_id=data['client_id'], priority=data['priority']
        )
