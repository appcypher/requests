""" Module containing the parent class implementation of all models. """
from sqlalchemy.sql import func
from errors import ClientError
from functools import reduce
from .db import db


class BaseModel(db.Model):
    """
    The base model contains fields and methods common to all subtypes of
    base model.
    """
    __abstract__ = True

    id = db.Column(db.Integer, primary_key=True)
    created_at = db.Column(db.DateTime(timezone=True),
                           server_default=func.now())
    updated_at = db.Column(db.DateTime(timezone=True), onupdate=func.now())

    def save(self):
        """
        Saves the information of given instance in the database.
        """
        db.session.add(self)
        db.session.commit()
        return self

    def update(self, **kwargs):
        """
        Updates the row with the values provided.

        Args:
            kwargs (dict): values to update row with.
        """
        for field, value in kwargs.items():
            setattr(self, field, value)
        db.session.commit()

    @classmethod
    def find_by_id(cls, id, includes=[]):
        """
        Finds and returns the row with the specified id.

        Args:
            id (int): the id of the row to find.
            includes (list): a list of model relationship to include.

        Examples:
            The includes argument takes models that can be included with
            the result.

            >>> Comment.find_by_id(1, [Staff])
            Comment {'message': 'Hello', 'staff_id': 2, 'request_id': 1,
            'staff': { 'username': 'John', 'avatar_url': 'xyz.com'}}

        Raises:
            ClientError: if not row with specified client id does not exist.
        """
        query = reduce(lambda query, model: query.join(model), includes,
                       cls.query)

        result = query.filter_by(id=id).first()
        if not result:
            raise ClientError('cannot find specified client', 404)
        return result

    @classmethod
    def get_all(cls):
        """
        Gets all the rows of a model from the database
        """
        return cls.query.all()

    def __repr__(self):
        """
        Returns a string representation of the model instance
        """
        model_repr = vars(self).copy()

        # Remove unecessary fields
        for key in ('_sa_instance_state', 'created_at', 'updated_at'):
            if key in model_repr:
                del model_repr[key]

        return f'{self.__class__.__name__} {model_repr}'
