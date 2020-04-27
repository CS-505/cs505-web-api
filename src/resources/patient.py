"""
Define the REST verbs relative to the patient
"""

from flasgger import swag_from
from flask.json import jsonify
from flask_restful import Resource
from repositories import PatientRepository

class PatientResource(Resource):
    """ Verbs relative to the patient """

    @staticmethod
    @swag_from("../swagger/patient/GET.yml")
    def get(mrn):
        patient = PatientRepository.query_by_mrn(mrn)

        
        if (patient == None):
            return jsonify("invalid mrn")
        else:
            return jsonify(mrn=patient.mrn, location_code=patient.location_code)