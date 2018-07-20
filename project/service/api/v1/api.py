from flask import Blueprint
from flask_restful import Api

blueprint = Blueprint('service', __name__)
api = Api(app=blueprint, prefix='/api/v1')
