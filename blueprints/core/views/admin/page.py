from flask import render_template

from .... import required_permission
from ... import core

# Index Admin Page
@core.route('/admin/page/')
@required_permission('page.index')
def admin_page_index():
    return render_template('admin/welcome.html')