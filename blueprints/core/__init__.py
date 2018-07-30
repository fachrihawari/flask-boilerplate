# Load external module
from flask import Blueprint, render_template, g

# Load models from this module
from .models import *

# Create blueprint instance
core = Blueprint('core', __name__, url_prefix='/', template_folder='templates/')

# Load views from this module
from .views import *