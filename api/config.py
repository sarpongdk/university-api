import os, secrets, dotenv

basedir = os.path.abspath(os.path.dirname(__file__))
ENV_PATH = os.path.join(basedir, ".env")

dotenv.load_dotenv(verbose = True, dotenv_path = ENV_PATH)

class Config:
   DEBUG = os.getenv('DEBUG', True)
   SECRET_KEY = os.getenv('SECRET_KEY', str(secrets.token_hex(16)))
   SQLALCHEMY_DATABASE_URI = os.getenv('SQLALCHEMY_DATABASE_URI', "mysql://root@localhost/universitydb")
