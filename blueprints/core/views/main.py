from flask import render_template

from .. import core

# Index Page
@core.route('/')
def index():
    return '''welcome to flask boilerplate
        <a href="/admin/">Go to admin</a>
    '''

# About Page
@core.route('/about')
def about():
    return '''welcome to flask boilerplate # about page
        <a href="/admin/">Go to admin</a>
    '''

# Contact Page
@core.route('/contact')
def contact():
    return '''welcome to flask boilerplate # contact page
        <a href="/admin/">Go to admin</a>
    '''