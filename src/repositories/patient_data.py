""" Defines the patient_data repository """

from models import PatientData
from models import db

class PatientRepository:
    """ The repository for the patient_data model """

    @staticmethod
    def reset_db():
        """ Reset all data in db """
        db.session.query(PatientData).delete()
        db.session.commit()

    @staticmethod
    def query_by_mrn(id):
        """ Query a patient by its mrn """
        patient_record = PatientData.query.filter_by(mrn = id).first()
        return patient_record

    @staticmethod
    def count_pos():
        """ Count positive and negative test cases """
        pos_count = PatientData.query.filter_by(is_positive = '1').count()
        return pos_count

    @staticmethod
    def count_neg():
        """ Count positive and negative test cases """
        neg_count = PatientData.query.filter_by(is_positive = '0').count()
        return neg_count