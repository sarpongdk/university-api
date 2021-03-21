from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from flask_mail import Mail

from api.http_service import HTTPFactory

# instantiation
db = SQLAlchemy()
cors = CORS()
mail = Mail()
http = HTTPFactory.get_http()
