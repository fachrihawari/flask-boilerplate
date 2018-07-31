# Load external module
from flask import Blueprint, render_template

# Create blueprint instance
blog = Blueprint('blog', __name__, url_prefix='/', template_folder='templates/')

# Index Admin Page
@blog.route('/admin/blog/')
def admin_page_index():
    return render_template('admin/welcome.html')