"""
Defines the blueprint for the alert_list
"""
from flask import Blueprint
from flask_restful import Api

from resources import AlertListResource

ALERT_LIST_BLUEPRINT = Blueprint("alert_list", __name__)
Api(ALERT_LIST_BLUEPRINT).add_resource(
    AlertListResource, "/alertlist"
)
