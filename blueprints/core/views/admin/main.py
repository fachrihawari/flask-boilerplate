from flask import render_template

from ... import core

# Index Admin
@core.route('/admin/')
def admin_index():
    return render_template('admin/welcome.html')
