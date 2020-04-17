"""
Define the REST verbs relative to the hospital
"""

from flasgger import swag_from
from flask.json import jsonify
from flask_restful import Resource


class HospitalResource(Resource):
    """ Verbs relative to the hospital """

    @staticmethod
    @swag_from("../swagger/hospital/GET.yml")
    def get(id):
        return jsonify({"id": "%s" % id})