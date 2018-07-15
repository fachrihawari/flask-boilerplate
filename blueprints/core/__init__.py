# Load external module
from flask import Blueprint

# Load models from this module
from .models import *

# Create blueprint instance
core = Blueprint('core', __name__, url_prefix='/')

# Show core
@core.route('/', defaults={'page': 'index'})
@core.route('/<string:page>')
def show(page):
    return 'ini adalah page: %r' % page