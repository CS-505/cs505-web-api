"""
Define the REST verbs relative to the data management
"""

from flasgger import swag_from
from flask.json import jsonify
from flask_restful import Resource
from repositories import ZipCodeRepository
from repositories import HospitalRepository
from repositories import PatientRepository
from repositories import ZipAlertRepository

class ResetResource(Resource):
    """ Verbs relative to the data management """

    @staticmethod
    @swag_from("../swagger/management_reset/GET.yml")
    def get():

        #broke this out since the conditionals were affecting it
        ZipCodeRepository.local_infile()

        if HospitalRepository.is_empty() == True:
            HospitalRepository.import_csv()
        else:
            HospitalRepository.reset_db()

        if ZipCodeRepository.is_empty() == True:
            ZipCodeRepository.import_csv()                 
               
        PatientRepository.reset_db()
        ZipAlertRepository.reset_db()
                        
        #the assignment also asks for code 0 on failure, do we need this?
        return jsonify({"reset_status_code": "1"})
        

