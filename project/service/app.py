from flask import Flask
from service.db import db
from service.api.v1.api import blueprint as service_api_v1_bp

# Instantiate flask and register blueprints
application = Flask(__name__)
application.register_blueprint(service_api_v1_bp)

# Prepare config for SQLAlchemy
application.config['SECRET_KEY'] = '\x89R\xd5\xaa\x03=\xd9\x12\x00;\x042\xb0\xf5\xbd\xf5'
application.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://'
application.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Init other applications
db.init_app(application)