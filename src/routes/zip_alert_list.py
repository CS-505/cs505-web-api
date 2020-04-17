"""
Defines the blueprint for the Zip Alert List
"""
from flask import Blueprint
from flask_restful import Api

from resources import ZipAlertListResource

ZIP_ALERT_LIST_BLUEPRINT = Blueprint("zip_alert_list", __name__)
Api(ZIP_ALERT_LIST_BLUEPRINT).add_resource(
    ZipAlertListResource, "/zipalertlist"
)
