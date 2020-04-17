"""
Defines the blueprint for the hospital
"""
from flask import Blueprint
from flask_restful import Api

from resources import HospitalResource

HOSPITAL_BLUEPRINT = Blueprint("hospital", __name__)
Api(HOSPITAL_BLUEPRINT).add_resource(
    HospitalResource, "/gethospital/<string:id>"
)
