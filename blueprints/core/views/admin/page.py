from flask import render_template

from ... import core

# Index Admin Page
@core.route('/admin/page/')
def admin_page_index():
    return render_template('admin/welcome.html')