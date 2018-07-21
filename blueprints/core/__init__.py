# Load external module
from flask import Blueprint, render_template

# Load models from this module
from .models import *

# Create blueprint instance
core = Blueprint('core', __name__, url_prefix='/', template_folder='templates/')

# Index Page
@core.route('/')
def index():
    return '''welcome to flask boilerplate
        <a href="/admin/">Go to admin</a>
    '''

# Index Admin Page
@core.route('/admin/')
def admin_index():
    return render_template('admin/welcome.html')