"""
Define the REST verbs relative to the team management
"""

from flasgger import swag_from
from flask.json import jsonify
from flask_restful import Resource



class TeamResource(Resource):
    """ Verbs relative to the team management """

    @staticmethod
    @swag_from("../swagger/management_team/GET.yml")
    def get():
        return jsonify({"team_name": "TrueOrFalse",
            "Team_members_sids":["12377243"],"app_status_code":"1"})
