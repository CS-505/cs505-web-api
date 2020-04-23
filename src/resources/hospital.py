"""
Define the REST verbs relative to the hospital
"""

from flasgger import swag_from
from flask.json import jsonify
from flask_restful import Resource
from repositories import HospitalRepository


class HospitalResource(Resource):
    """ Verbs relative to the hospital """

    @staticmethod
    @swag_from("../swagger/hospital/GET.yml")
    def get(id):
        hospital = HospitalRepository.query_by_id(id)

        #better messaging for result not found?
        if (hospital == None):
            return jsonify("invalid id")
        else:
            return jsonify(total_beds=hospital.beds_total, available_beds=hospital.beds_available, zipcode=hospital.hospital_zip)