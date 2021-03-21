import os, secrets, dotenv

basedir = os.path.abspath(os.path.dirname(__file__))
ENV_PATH = os.path.join(basedir, ".env")

dotenv.load_dotenv(verbose = True, dotenv_path = ENV_PATH)

class BaseConfig:
   SQLALCHEMY_TRACK_MODIFICATIONS = False
   SECRET_KEY = os.getenv('SECRET_KEY', str(secrets.token_hex(16)))
   MAIL_SERVER = os.getenv('MAIL_SERVER', "smtp.googlemail.com")
   MAIL_PORT = os.getenv('MAIL_PORT', 587)
   MAIL_USE_TLS = os.getenv('MAIL_USE_TLS', True)
   MAIL_USERNAME = os.getenv('MAIL_USERNAME')
   MAIL_PASSWORD = os.getenv('MAIL_PASSWORD')
   MAIL_DEBUG = os.getenv('MAIL_DEBUG', True)
   MAIL_DEFAULT_SENDER = os.getenv('MAIL_DEFAULT_SENDER', "zulf.gbede@gmail.com")
   MAIL_DEFAULT_RECEIVER = os.getenv('MAIL_DEFAULT_RECEIVER', "sarpong.david2@gmail.com")

class DevelopmentConfig(BaseConfig):
   DEBUG = True
   SQLALCHEMY_DATABASE_URI = os.getenv('SQLALCHEMY_DATABASE_URI', "mysql://root@localhost/universitydb")

class ProductionConfig(BaseConfig):
   DEBUG = os.getenv('DEBUG', True)
   SQLALCHEMY_DATABASE_URL = os.getenv('DATABASE_URL')


configs = {
   "development": api.config.DevelopmentConfig,
   "production": api.config.ProductionConfig
}

def get_config():
   config_name = os.getenv("FLASK_ENV", "development")
   return config[config_name]
