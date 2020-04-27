""" Defines the zipcode_distance repository """

from models import ZipAlert
from models import db
import csv


class ZipAlertRepository:
    """ The repository for the zipcode_distance model """

    @staticmethod
    def reset_db():
        """ Reset all data in db """
        db.session.query(ZipAlert).delete()
        db.session.commit()

    @staticmethod
    def get_alerted_zip_codes():
        zip_codes = ZipAlert.query.with_entities(ZipAlert.zipcode).filter_by(on_alert = True).all()
        return [zip_code[0] for zip_code in zip_codes]
    
    @staticmethod
    def is_state_alerted():
        zip_code_count = ZipAlert.query.filter_by(on_alert = True).count()
        return zip_code_count >= 5


    
    