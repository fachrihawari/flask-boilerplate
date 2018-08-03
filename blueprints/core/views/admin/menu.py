from flask import render_template

from .... import required_permission
from ... import core
from ...models.menu import Menu

# Index Admin Page
@core.route('/admin/menu/')
@required_permission('menu.index')
def admin_menu_index():
    print(Menu.query.all())
    return render_template('admin/welcome.html')