"""
Define the Zip Alert model
"""
from . import db
from .abc import BaseModel, MetaBaseModel


class ZipAlert(db.Model, BaseModel, metaclass=MetaBaseModel):

    """ The Zipcode Distance model """

    __tablename__ = "zipcode_distance"

    zipcode = db.Column(db.String(5), primary_key=True)
    current_count = db.Column(db.Integer())
    on_alert = db.Column(db.Boolean())

    def __init__(self, zipcode, current_count, on_alert):
        """ Create a new record """
        self.zipcode = zipcode
        self.current_count = current_count
        self.on_alert = on_alert

    
