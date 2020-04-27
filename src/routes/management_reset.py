"""
Defines the blueprint for the reset
"""
from flask import Blueprint
from flask_restful import Api

from resources import ResetResource

RESET_BLUEPRINT = Blueprint("reset", __name__)
Api(RESET_BLUEPRINT).add_resource(
    ResetResource, "/reset"
)
