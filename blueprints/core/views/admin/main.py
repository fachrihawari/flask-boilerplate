from flask import render_template

from .... import required_permission
from ... import core

@core.route('/admin/')
@required_permission('index')
def admin_index():
    return render_template('admin/welcome.html')
