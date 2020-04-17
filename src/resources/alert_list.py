"""
Define the REST verbs relative to the alert list
"""

from flasgger import swag_from
from flask.json import jsonify
from flask_restful import Resource


class AlertListResource(Resource):
    """ Verbs relative to the alert list """

    @staticmethod
    @swag_from("../swagger/alert_list/GET.yml")
    def get():
        return jsonify({"status": "this works!"})