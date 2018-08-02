from flask import render_template
from flask_login import login_required

from ... import core

@core.route('/admin/')
@login_required
def admin_index():
    return render_template('admin/welcome.html')
