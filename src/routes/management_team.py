"""
Defines the blueprint for the users
"""
from flask import Blueprint
from flask_restful import Api

from resources import TeamResource

TEAM_BLUEPRINT = Blueprint("team", __name__)
Api(TEAM_BLUEPRINT).add_resource(
    TeamResource, "/getteam"
)
