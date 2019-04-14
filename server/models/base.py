""" Module containing the parent class implementation of all models """
from .db import db
from sqlalchemy.sql import func


class BaseModel(db.Model):
    """
    The base model contains fields and methods common to all subtypes of
    base model
    """
    __abstract__ = True

    id = db.Column(db.Integer, primary_key=True)
    created_at = db.Column(db.DateTime(timezone=True),
                           server_default=func.now())
    updated_at = db.Column(db.DateTime(timezone=True), onupdate=func.now())

    def save(self):
        """
        Saves the information of given instance in the database
        """
        db.session.add(self)
        db.session.commit()
        return self

    def update(self, **kwargs):
        """
        Updates the row with the values provided

        Arguments:
            kwargs (dict): values to update row with
        """
        for field, value in kwargs.items():
            setattr(self, field, value)
        db.session.add(self)
        db.session.commit()

    @classmethod
    def find_by_id(cls, id, includes=[]):
        """
        Finds and returns the row with the specified id

        Arguments:
            id (int): the id of the row to find
            includes (list): the set of relationship to include

        TODO: Add includes and check if id=id can be simplified into just id
        """
        return cls.query.filter_by(id=id).first()

    @classmethod
    def get_all(cls):
        """
        Gets all the rows of a model from the database
        """
        return cls.query.all()
