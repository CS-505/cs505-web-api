"""
Define the REST verbs relative to the data management
"""

from flasgger import swag_from
from flask.json import jsonify
from flask_restful import Resource
from repositories import ZipCodeRepository
from repositories import HospitalRepository

class ResetResource(Resource):
    """ Verbs relative to the data management """

    @staticmethod
    @swag_from("../swagger/management_reset/GET.yml")
    def get():

        ZipCodeRepository.reset_db()
        HospitalRepository.reset_db()
        ZipCodeRepository.import_csv()
        HospitalRepository.import_csv()
        
        #the assignment also asks for code 0 on failure, do we need this?
        return jsonify({"reset_status_code": "1"})

