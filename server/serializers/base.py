""" Module containing the parent class implementation of all schemas """
from marshmallow import Schema, fields
from errors import ServerError


class BaseSchema(Schema):
    """
    The base schema contains fields and methods common to all subtypes of
    base schema
    """

    id = fields.Integer()
    created_at = fields.DateTime()
    updated_at = fields.DateTime()

    def from_object(self, obj):
        """
        Loads object into the schema

        Arguments:
            obj (object): any serializable Python object

        Raises:
            ServerError: if there are error while loading from object
        """
        data, errors = self.load(obj)
        if errors:
            raise ServerError('Can\'t convert object to schema', 500)
        return data
