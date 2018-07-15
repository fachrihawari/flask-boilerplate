SECRET_KEY = 'Your secret key'
DEBUG = False

# SQLAlchemy config
SQLALCHEMY_ECHO = False
SQLALCHEMY_TRACK_MODIFICATIONS = True
SQLALCHEMY_DATABASE_URI = 'postgresql://username:password@host/dbname'

# Your Blueprint 
BLUEPRINT_DIRECTORY = 'blueprints'
BLUEPRINTS = [
    'core',
]