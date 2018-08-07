class Pagination(object):

    def __init__(self, page, per_page, total_count):
        self.page = page
        self.per_page = per_page
        self.total_count = total_count

    @property
    def pages(self):
        from math import ceil
        return int(ceil(self.total_count / float(self.per_page)))

    @property
    def has_previous(self):
        return self.page > 1

    @property
    def has_next(self):
        return self.page < self.pages

    def iter_pages(self, left_edge=2, left_current=2, right_current=5, right_edge=2):
        last = 0
        for num in range(1, self.pages + 1):
            if num <= left_edge or \
               (num > self.page - left_current - 1 and \
                num < self.page + right_current) or \
               num > self.pages - right_edge:
                if last + 1 != num:
                    yield None
                yield num
                last = num


def required_permission(permission):
    from functools import wraps
    
    from flask import redirect, url_for, abort, flash, request
    from flask_login import current_user

    def decorator(f):
        @wraps(f)
        def decorated_function(*args, **kwargs):
            if not current_user.is_authenticated:
                flash('Your not logged in!')
                return redirect(url_for('core.login', next=request.url))
            elif not current_user.has_access(permission):
                return abort(403)           
            return f(*args, **kwargs)
        return decorated_function
    return decorator