from flask import render_template, redirect, url_for, request, flash
from flask_login import login_user, login_required, logout_user, current_user

from webapp import webapp, logging


@webapp.route('/', methods=['GET'])
def index_start():
    logging.warning("See this message in Flask Debug Toolbar!")
    return render_template('index.html')
