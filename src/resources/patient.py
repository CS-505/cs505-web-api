"""
Define the REST verbs relative to the patient
"""

from flasgger import swag_from
from flask.json import jsonify
from flask_restful import Resource


class PatientResource(Resource):
    """ Verbs relative to the patient """

    @staticmethod
    @swag_from("../swagger/patient/GET.yml")
    def get(mrn):
        return jsonify({"mrn": "%s" % mrn})