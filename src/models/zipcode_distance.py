"""
Define the Zipcode Distance model
"""
from . import db
from .abc import BaseModel, MetaBaseModel


class ZipCodeDistance(db.Model, BaseModel, metaclass=MetaBaseModel):
    """ The User model """

    __tablename__ = "zipcode_distance"

    zip_to = db.Column(db.String(5), primary_key=True)
    zip_from = db.Column(db.String(5), primary_key=True)
    distance = db.Column(db.Numeric(20,15))

    def __init__(self, zip_to, zip_from, distance):
        """ Create a new User """
        self.zip_to = zip_to
        self.zip_from = zip_from
        self.distance = distance
