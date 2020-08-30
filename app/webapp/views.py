from flask import render_template, redirect, url_for, request, flash

from webapp import webapp, logging


@webapp.route('/', methods=['GET'])
def index_start():
    logging.warning("See this message in Flask Debug Toolbar!")
    return render_template('index.html')
