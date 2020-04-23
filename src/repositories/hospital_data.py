""" Defines the hospital_data repository """

from models import HospitalData
from models import db

class HospitalRepository:
    """ The repository for the hospital_data model """

    @staticmethod
    def create(hospital_id, hospital_zip, beds_total, beds_occupied, beds_available):
        """ Create a new record """
        record = HospitalData(hospital_id=hospital_id , hospital_zip=hospital_zip, beds_total=beds_total, beds_occupied=beds_occupied, beds_available=beds_available)

        return record.save()
    
    @staticmethod
    def import_csv():
        """ Populate tabel from CSV """
        
        db.session.execute("LOAD DATA LOCAL INFILE './hospitals.csv' INTO TABLE hospital_data FIELDS TERMINATED BY ',' LINES TERMINATED BY '\n' IGNORE 1 LINES")
        db.session.commit()

    @staticmethod
    def reset_db():
        """ Reset all data in db """
        db.session.query(HospitalData).delete()
        db.session.commit()

    @staticmethod
    def query_by_id(id):
        """ Query a hospital by it's ID """
        hospital_record = HospitalData.query.filter_by(hospital_id = id).first()
        return hospital_record