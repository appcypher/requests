""" Module containing the parent class implementation of all schemas. """
from marshmallow import Schema, fields
from errors import ClientError


class BaseSchema(Schema):
    """
    The base schema contains fields and methods common to all subtypes of
    base schema.
    """

    id = fields.Integer()
    created_at = fields.DateTime()

    def serialize(self, obj):
        """
        Serialize object into a dictionary.

        Args:
            obj (object): any serializable Python object.
        """

        return attempt(self.dump(obj))

    def deserialize(self, dictionary):
        """
        Deserialize object from a dictionary.

        Args:
            dictionary (dict): any serializable Python object.
        """

        return attempt(self.load(dictionary))


def attempt(result):
    """
    Checks the result for errors

    Args:
        obj (tuple): result of a marshmallow load or dump

    Raises:
        ServerError: if there are errors during (de)serialization
    """
    if result.errors:
        raise ClientError(result.errors)

    return result.data
