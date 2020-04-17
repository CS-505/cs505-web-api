"""
Define the REST verbs relative to the test_count
"""

from flasgger import swag_from
from flask.json import jsonify
from flask_restful import Resource


class TestCountResource(Resource):
    """ Verbs relative to the test_count """

    @staticmethod
    @swag_from("../swagger/test_count/GET.yml")
    def get():
        return jsonify({"status": "this works!"})