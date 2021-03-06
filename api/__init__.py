from flask import Flask

from api.config import get_config
from api.extensions import mail, db, cors

import os

def create_app():
   app = Flask(__name__)
   config_object = get_config()
   app.config.from_object(config_object)

   db.init_app(app)
   mail.init_app(app)
   cors.init_app(app, resources = {"*": {"origins": "*"}})

   from api.routes import university_api

   app.register_blueprint(university_api, url_prefix = os.environ.get("API_PREFIX", "/api"))

   return app

