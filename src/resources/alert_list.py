"""
Define the REST verbs relative to the alert list
"""

from flasgger import swag_from
from flask.json import jsonify
from flask_restful import Resource
from repositories import ZipAlertRepository

class AlertListResource(Resource):
    """ Verbs relative to the alert list """

    @staticmethod
    @swag_from("../swagger/alert_list/GET.yml")
    def get():
        status = "1" if ZipAlertRepository.is_state_alerted() else "0"
        return jsonify(state_status=status)