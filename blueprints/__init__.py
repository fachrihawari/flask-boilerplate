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