"""
Define the REST verbs relative to the data management
"""

from flasgger import swag_from
from flask.json import jsonify
from flask_restful import Resource


class ResetResource(Resource):
    """ Verbs relative to the data management """

    @staticmethod
    @swag_from("../swagger/management_reset/GET.yml")
    def get():
        return jsonify({"status": "this works!"})