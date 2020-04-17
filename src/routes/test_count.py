"""
Defines the blueprint for the test_count
"""
from flask import Blueprint
from flask_restful import Api

from resources import TestCountResource

TEST_COUNT_BLUEPRINT = Blueprint("test_count", __name__)
Api(TEST_COUNT_BLUEPRINT).add_resource(
    TestCountResource, "/testcount"
)
