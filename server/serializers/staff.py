""" Module containing staff schema implementation. """
from marshmallow import fields
from middleware.validations import (validate_string_length, validate_url)
from .base import BaseSchema


class StaffSchema(BaseSchema):
    """
    Staff schema for validating, serializing and deserializing Staff objects.
    """
    username = fields.String(validate=validate_string_length(60),
                             required=True)
    avatar_url = fields.String(
        validate=[validate_string_length(250), validate_url], required=True)
