from marshmallow import Schema, fields
from errors import ServerError


class BaseSchema(Schema):
    id = fields.Integer()
    created_at = fields.DateTime()
    updated_at = fields.DateTime()
    
    def __init__(self, obj):
        data, errors = self.load(obj)
        if errors:
            raise ServerError('Can\'t convert object to schema', 500)
        data
