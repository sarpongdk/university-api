from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

from api.config import Config

import os

# instantiation
db = SQLAlchemy()
cors = CORS()

def create_app(config_object = Config):
   app = Flask(__name__)
   app.config.from_object(config_object)

   db.init_app(app)
   cors.init_app(app, resources = {"*": {"origins": "*"}})

   from api.routes import university_api

   app.register_blueprint(university_api, url_prefix = os.environ.get("API_PREFIX", "/api"))

   return app

