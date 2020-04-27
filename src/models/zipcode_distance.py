"""
Define the Zipcode Distance model
"""
from . import db
from .abc import BaseModel, MetaBaseModel


class ZipCodeDistance(db.Model, BaseModel, metaclass=MetaBaseModel):

    """ The Zipcode Distance model """

    __tablename__ = "zipcode_distance"

    id = db.Column(db.Integer(), primary_key=True)
    zip_to = db.Column(db.String(5))
    zip_from = db.Column(db.String(5))
    distance = db.Column(db.Numeric(20,15))

    def __init__(self, zip_to, zip_from, distance):
        """ Create a new record """
        self.zip_to = zip_to
        self.zip_from = zip_from
        self.distance = distance

    
