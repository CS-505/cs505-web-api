"""
Define the Hopsital Data model
"""
from . import db
from .abc import BaseModel, MetaBaseModel


class HospitalData(db.Model, BaseModel, metaclass=MetaBaseModel):
    """ The Hospital Data model """

    __tablename__ = "hospital_data"

    hospital_id = db.Column(db.String(9), primary_key=True)
    hospital_zip = db.Column(db.String(5))
    beds_total = db.Column(db.Integer())
    beds_occupied = db.Column(db.Integer())
    beds_available = db.Column(db.Integer())
    trauma_level = db.Column(db.Integer())
    

    def __init__(self, hospital_id, hospital_zip, beds_total, beds_occupied, beds_available, trauma_level):
        """ Create a new record """
        self.hospital_id = hospital_id
        self.hospital_zip = hospital_zip
        self.beds_total = beds_total
        self.beds_occupied = beds_occupied
        self.beds_available = beds_available
        self.trauma_level = trauma_level

       