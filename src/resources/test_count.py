"""
Define the REST verbs relative to the test_count
"""

from flasgger import swag_from
from flask.json import jsonify
from flask_restful import Resource
from repositories import PatientRepository


class TestCountResource(Resource):
    """ Verbs relative to the test_count """

    @staticmethod
    @swag_from("../swagger/test_count/GET.yml")
    def get():
        pos_count = PatientRepository.count_pos()
        neg_count = PatientRepository.count_neg()
                
        return jsonify(positive_test=str(pos_count), negative_test=str(neg_count))