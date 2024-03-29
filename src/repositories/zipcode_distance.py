""" Defines the zipcode_distance repository """

from models import ZipCodeDistance
from models import db
import csv


class ZipCodeRepository:
    """ The repository for the zipcode_distance model """

    @staticmethod
    def create(self, zip_to, zip_from, distance):
        """ Create a new record """
        record = ZipCodeDistance(zip_to=zip_to, zip_from=zip_from, distance=distance)
        db.session.add(record)
        db.session.commit()
        return record.save()

    @staticmethod
    def import_csv():
        """ Populate tabel from CSV """
               
        db.session.execute("LOAD DATA LOCAL INFILE './kyzipdistance.csv' INTO TABLE zipcode_distance FIELDS TERMINATED BY ',' LINES TERMINATED BY '\n' IGNORE 1 LINES")
        db.session.commit()
        
    @staticmethod
    def reset_db():
        """ Reset all data in db """
        db.session.query(ZipCodeDistance).delete()
        db.session.commit()

    @staticmethod
    def is_empty():

        if db.session.query(ZipCodeDistance).first() == None:
            return True
        else:
            return False
    
    @staticmethod
    def local_infile():
        db.session.execute("SET GLOBAL local_infile = 'ON'") 
        db.session.commit()