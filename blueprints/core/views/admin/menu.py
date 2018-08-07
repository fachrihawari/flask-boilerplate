from flask import render_template, redirect, url_for, flash, request
from flask_login import current_user

from ..... import db
from .... import required_permission, Pagination
from ... import core
from ...models.menu import Menu
from ...forms.menu import MenuForm

# Index Admin Menu
@core.route('/admin/menu/')
@required_permission('menu.index')
def admin_menu_index():
    page = 1  if request.args.get('page') is None else int(request.args.get('page'))

    menus = Menu.query.order_by(Menu.group.asc(), Menu.position.asc()).paginate(page, 10)
    pagination = Pagination(page, 10, Menu.query.count())
    return render_template('admin/menu/index.html', menus=menus.items, pagination=pagination)

# Create Admin Menu
@core.route('/admin/menu/create', methods=['GET', 'POST'])
@required_permission('menu.create')
def admin_menu_create():
    form = MenuForm()
    form.parent_id.choices = [('', 'Select Parent')] + [(g.id, g.label + ' ('  + g.group + ')') for g in Menu.query.order_by('group')]
    if form.validate_on_submit():
        menu = Menu(
            label=form.label.data, 
            target=form.target.data,
            parent_id= None if form.parent_id.data == '' else form.parent_id.data,
            icon=form.icon.data,
            position=form.position.data,
            group=form.group.data,
            is_active=form.is_active.data,
            user_id=current_user.id
        )

        # add menu to the database
        try:
            db.session.add(menu)
            db.session.commit()
            flash('You have successfully added a new menu.', category='success')
        except Exception as e:
            db.session.rollback()
            flash('Check your data again.', category='danger')   

        # redirect to menu list
        return redirect(url_for('core.admin_menu_index'))

    return render_template('admin/menu/form.html', form=form, type='create')

# Edit Admin Menu
@core.route('/admin/menu/<int:id>/edit', methods=['GET', 'POST'])
@required_permission('menu.edit')
def admin_menu_edit(id):
    menu = Menu.query.get_or_404(id)
    form = MenuForm(obj=menu)
    form.parent_id.choices = [('', 'Select Parent')] + [(g.id, g.label + ' ('  + g.group + ')') for g in Menu.query.order_by('group')]
    if form.validate_on_submit():
        menu.label = form.label.data 
        menu.target = form.target.data
        menu.parent_id = None if form.parent_id.data == '' else form.parent_id.data
        menu.icon = form.icon.data
        menu.position = form.position.data
        menu.group = form.group.data
        menu.is_active = form.is_active.data

        # add menu to the database
        try:
            db.session.commit()
            flash('You have successfully edit menu %s.' % menu.label, category='success')
        except Exception as e:
            db.session.rollback()
            flash('Check your data again.', category='danger')   

        # redirect to menu index
        return redirect(url_for('core.admin_menu_index'))

    return render_template('admin/menu/form.html', form=form, type='edit')


# Toggle Active Admin Menu
@core.route('/admin/menu/<int:id>/toggle_active', methods=['POST'])
@required_permission('menu.edit')
def admin_menu_toggle_active(id):
    menu = Menu.query.get_or_404(id)
    try:
        menu.is_active = not menu.is_active
        db.session.commit()

        message = 'activate' if menu.is_active else 'deactivate'
        flash('You have successfully %s the menu.' % message, category='success')
    except:
        flash('Delete menu failed.', category='danger')

    # redirect to the menu index
    return redirect(url_for('core.admin_menu_index'))

# Delete Admin Menu
@core.route('/admin/menu/<int:id>/delete', methods=['POST'])
@required_permission('menu.delete')
def admin_menu_delete(id):
    menu = Menu.query.get_or_404(id)
    try:
        db.session.delete(menu)
        db.session.commit()
        flash('You have successfully deleted the menu.', category='success')
    except:
        flash('Delete menu failed.', category='danger')

    # redirect to the menu index
    return redirect(url_for('core.admin_menu_index'))
