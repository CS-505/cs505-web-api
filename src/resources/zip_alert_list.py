"""
Define the REST verbs relative to the zip alert list
"""

from flasgger import swag_from
from flask.json import jsonify
from flask_restful import Resource
from repositories import ZipAlertRepository


class ZipAlertListResource(Resource):

    @staticmethod
    @swag_from("../swagger/zip_alert_list/GET.yml")
    def get():
        return jsonify(ziplist=ZipAlertRepository.get_alerted_zip_codes())