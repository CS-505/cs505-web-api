#!/usr/local/bin/python3
from flasgger import Swagger
from flask import Flask
from flask.blueprints import Blueprint

import config
import routes
from models import db

# config your API specs
# you can define multiple specs in the case your api has multiple versions
# ommit configs to get the default (all views exposed in /spec url)
# rule_filter is a callable that receives "Rule" object and
#   returns a boolean to filter in only desired views

server = Flask(__name__)

server.config["SWAGGER"] = {
    "swagger_version": "2.0",
    "title": "COVID-19 Tracker",
    "specs": [
        {
            "version": "0.0.1",
            "title": "CS 505 Final Project: COVID-19 Tracker",
            "endpoint": "spec",
            "route": "/application/spec",
            "rule_filter": lambda rule: True,  # all in
        }
    ],
    "static_url_path": "/apidocs",
}

Swagger(server)

server.debug = config.DEBUG
server.config["SQLALCHEMY_DATABASE_URI"] = config.DB_URI
server.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = config.SQLALCHEMY_TRACK_MODIFICATIONS
db.init_app(server)
db.app = server

for blueprint in vars(routes).values():
    if isinstance(blueprint, Blueprint):
        server.register_blueprint(blueprint, url_prefix=config.APPLICATION_ROOT)

if __name__ == "__main__":
    server.run(host=config.HOST, port=config.PORT)

#this isn't working for some reason
"""enables loading local data client side"""
db.session.execute("SET GLOBAL local_infile = 'ON'") 
db.session.commit()