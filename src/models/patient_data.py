"""
Define the Patient Data model
"""
from . import db
from .abc import BaseModel, MetaBaseModel


class PatientData(db.Model, BaseModel, metaclass=MetaBaseModel):
    """ The Patient Data model """

    __tablename__ = "patient_data"

    mrn = db.Column(db.String(50), nullable=False, primary_key=True)
    location_code = db.Column(db.String(9))
    is_positive = db.Column(db.Integer(), nullable=True)
    
    

    def __init__(self, mrn, location_code, is_positive):
        """ Create a new record """
        self.mrn = mrn
        self.location_code = location_code
        self.is_positive = is_positive
        