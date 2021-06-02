from os import environ, path
from dotenv import load_dotenv

basedir = path.abspath(path.dirname(__file__))
load_dotenv(path.join(basedir, '.env'))


class Config:
    """Set Flask config variables."""

    #FLASK_ENV = 'development'
    #FLASK_APP = 'run.py'
    #DEGUG = True
    SECRET_KEY = environ.get('SECRET_KEY')
    TEMPLATES_FOLDER = 'templates'

    # Database
    SQLALCHEMY_DATABASE_URI = 'sqlite:////path/to/db/name.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
