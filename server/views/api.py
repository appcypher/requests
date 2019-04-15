""" Module that contains restplus api isntantiation. """
from flask_restplus import Api
from config.blueprints import api_v1_blueprint

# Creates a restplus api instance
api = Api(api_v1_blueprint)
