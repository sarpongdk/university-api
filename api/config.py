import os, secrets, dotenv

basedir = os.path.abspath(os.path.dirname(__file__))
ENV_PATH = os.path.join(basedir, ".env")

dotenv.load_dotenv(verbose = True, dotenv_path = ENV_PATH)

class Config:
   DEBUG = os.getenv('DEBUG', True)
   SECRET_KEY = os.getenv('SECRET_KEY', str(secrets.token_hex(16)))
   DATABASE_URL = os.getenv('DATABASE_URL', "mysql://bff87691226f29:44c2d26c@us-cdbr-east-03.cleardb.com/heroku_4d5eaecda761fa0?reconnect=true")
   SQLALCHEMY_DATABASE_URI = os.getenv('SQLALCHEMY_DATABASE_URI', "mysql://root@localhost/universitydb")
   MAIL_SERVER = os.getenv('MAIL_SERVER', "smtp.googlemail.com")
   MAIL_PORT = os.getenv('MAIL_PORT', 587)
   MAIL_USE_TLS = os.getenv('MAIL_USE_TLS', True)
   MAIL_USERNAME = os.getenv('MAIL_USERNAME')
   MAIL_PASSWORD = os.getenv('MAIL_PASSWORD')
   MAIL_DEBUG = os.getenv('MAIL_DEBUG', True)
   MAIL_DEFAULT_SENDER = os.getenv('MAIL_DEFAULT_SENDER', "zulf.gbede@gmail.com")
   MAIL_DEFAULT_RECEIVER = os.getenv('MAIL_DEFAULT_RECEIVER', "sarpong.david2@gmail.com")
