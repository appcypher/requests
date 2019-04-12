from marshmallow import fields
from .base import BaseSchema
from middleware.validations import string_length_validate


class RequestSchema(BaseSchema):
    title = fields.String(validate=string_length_validate(60), required=True)
    decription = fields.String(validate=string_length_validate(250),
                               required=True)
    product_area = fields.String(required=True)
    target_date = fields.DateTime(required=True)
    priority = fields.Integer(required=True)
    client_id = fields.Integer(required=True)
    comments = fields.Integer(required=True)
