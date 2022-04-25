"""Flask configuration."""
from os import environ, path

basedir = path.abspath(path.dirname(__file__))

POSTGRES_HOST = environ.get('POSTGRES_HOST')
POSTGRES_DB = environ.get('POSTGRES_DB')
POSTGRES_USER = environ.get('POSTGRES_USER')
POSTGRES_PASSWORD = environ.get('POSTGRES_PASSWORD')
