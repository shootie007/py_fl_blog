from flask import request, redirect, url_for, render_template, flash, session
from flask import current_app as app
from flask_login import LoginManager, login_user, login_required
from functools import wraps
from flask import Blueprint
from flask_blog import models

view = Blueprint('view', __name__)
# login_manager = LoginManager()
# login_manager.init_app(app)

def login_required(view):
    @wraps(view)
    def inner(*args, **kwargs):
        if not session.get('logged_in'):
            return redirect(url_for('view.login'))
        return view(*args, **kwargs)
    return inner


@view.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        user = models.User.query.filter_by(username=request.form['username']).first()
        # if user and user.check_password(request.form['password']):
        if user and request.form['password'] == user.password:
            session['logged_in'] = True
            flash('ログインしました')
            return redirect(url_for('entry.show_entries'))
        else:
            flash('ユーザ名またはパスワードが異なります')
    return render_template('login.html')


@view.route('/logout')
def logout():
    session.pop('logged_in', None)
    flash('ログアウトしました')
    return redirect(url_for('entry.show_entries'))

@view.app_errorhandler(404)
def non_existant_route(error):
    return redirect(url_for('view.login'))
