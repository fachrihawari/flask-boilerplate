from os import getenv

APPLICATION_NAME = getenv('APPLICATION_NAME', 'Flask Boilerplate')

SECRET_KEY = getenv('SECRET_KEY', 'Your Secret Key')
DEBUG = getenv('DEBUG', True)

# SQLAlchemy config
SQLALCHEMY_ECHO = getenv('SQLALCHEMY_ECHO', False)
SQLALCHEMY_TRACK_MODIFICATIONS = getenv('SQLALCHEMY_TRACK_MODIFICATIONS', True)
SQLALCHEMY_DATABASE_URI = getenv('SQLALCHEMY_DATABASE_URI', 'postgresql://username:password@host/dbname')

# Your Blueprint 
BLUEPRINT_DIRECTORY = 'blueprints'
BLUEPRINTS = [
    'core',
]