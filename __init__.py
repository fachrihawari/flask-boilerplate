from os import path

from flask import Flask
from flask_login import LoginManager
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

# Init model and migrations
db = SQLAlchemy()
migrate = Migrate()
login_manager = LoginManager()

def create_app():
    '''
    Create an app instance
    '''
    
    # Create and configure the app
    app = Flask(__name__)
    app.config.from_pyfile('config.py')

    # Assign model and migrations to app
    db.init_app(app)
    migrate.init_app(app, db)
    login_manager.init_app(app)

    # Call blueprint autoloader
    autoloader(app)

    # Setup login
    setup_login(login_manager)

    # Setup jinja
    setup_jinja(app)

    return app

def setup_login(login_manager):
    '''
    Setup login
    '''    
    from .blueprints.core.models.user import User

    @login_manager.user_loader
    def user_loader(id):
        return User.query.get(int(id))

def setup_jinja(app):
    '''
    Setup jinja
    '''

    # Get config with filter
    @app.template_filter('config')
    def config(key, default=None):
        print(key, default)
        return app.config.get(key) or default

    # Share data to variable
    @app.context_processor
    def inject_admin_menu():
        '''
        Load admin menu
        '''    
        from .blueprints.core.models.menu import Menu
        menu = Menu.query.filter(Menu.group == 'admin.sidebar', Menu.is_active).order_by(Menu.position).all()
        return dict(admin_sidebar_menu=menu)

    def url_for_other_page(page):
        from flask import request, url_for
        args = request.view_args.copy()
        args['page'] = page
        return url_for(request.endpoint, **args)
        
    app.jinja_env.globals['url_for_other_page'] = url_for_other_page
            
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
    for blueprint_name in app.config['BLUEPRINTS']:

        blueprint_path = __name__ + '.' + app.config['BLUEPRINT_DIRECTORY'] + '.' + blueprint_name + '.' + blueprint_name
        blueprint_instance = import_string(blueprint_path, silent=False)

        # Check if blueprint exists
        if (blueprint_instance is None):
            print('   \u2715 ' + str.capitalize(blueprint_name) + ' failed to load...')
        else:
            app.register_blueprint(blueprint_instance)
            print('   \u2713 ' + str.capitalize(blueprint_name) + ' loaded...')