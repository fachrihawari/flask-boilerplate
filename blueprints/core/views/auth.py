from flask import render_template, redirect, render_template, url_for, abort, flash, request
from flask_login import login_user, logout_user, current_user
from datetime import datetime

from .... import db
from .. import core
from ..models.user import User
from ..forms.login import LoginForm

@core.route('/auth/login', methods=['GET', 'POST'])
def login():

    # redirect if authenticated
    if current_user.is_authenticated:
        return redirect(url_for('.admin_index'))

    # Init LoginForm for validation and catch data
    form = LoginForm()
    if form.validate_on_submit():

        # Check user email
        user = User.query.filter(User.email == form.email.data, User.is_confirm == True).first()
        if user is None:
            flash('Your email is not registered!')
            return render_template('auth/login.html', form=form)

        # Check user password
        if not user.check_password(form.password.data):
            flash('Your password is wrong!')
            return render_template('auth/login.html', form=form)

        # Set last login
        user.is_authenticated = True
        user.last_authenticated = datetime.now()
        db.session.commit()

        # login user with flask-login
        login_user(user, remember=form.remember_me.data)

        # Redirect to link
        next = request.args.get('next')
        return redirect(next or url_for('.admin_index'))

    return render_template('auth/login.html', form=form)


@core.route('/auth/logout', methods=['GET'])
def logout():

    # logout user
    user = User.query.get(current_user.id)

    logout_user()

    user.is_authenticated = False
    db.session.commit()
    
    return redirect(url_for('.login'))