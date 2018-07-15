from os import path, getenv

from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

# Init model and migrations
db = SQLAlchemy()
migrate = Migrate()

def create_app():
    '''
    Create an app instance
    '''

    # Get current env
    currentEnv = getenv('FLASK_ENV')
    if currentEnv is None:
        currentEnv = 'production'

    # Generate path
    config_path = path.join(path.abspath(path.dirname(__name__)), 'config', currentEnv + '.py')

    # Create and configure the app
    app = Flask(__name__)
    app.config.from_pyfile(config_path)
    
    # Assign model and migrations to app
    db.init_app(app)
    migrate.init_app(app, db)

    # Call blueprint autoloader
    autoloader(app)

    return app

def autoloader(app):
    '''
    Autoload defined blueprint on BLUEPRINTS from config.py
    '''

    # Core blueprint is required
    if ('core' not in app.config['BLUEPRINTS']):
        print('Missing blueprint core!')
        return
    
    # Log message
    print(' * Blueprints:')
    
    from werkzeug.utils import import_string

    # Load every blueprint
    for blueprint_path in app.config['BLUEPRINTS']:
        # __name__ + '.' +
        real_path = app.config['BLUEPRINT_DIRECTORY'] + '.' + blueprint_path + '.' + blueprint_path
        blueprint = import_string(real_path, silent=True)

        # Check if blueprint exists
        if (blueprint is None):
            print('   \u2715 ' + str.capitalize(blueprint_path) + ' failed to load...')
        else:
            app.register_blueprint(blueprint)
            print('   \u2713 ' + str.capitalize(blueprint_path) + ' loaded...')