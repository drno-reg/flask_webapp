from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_debugtoolbar import DebugToolbarExtension
import logging

webapp = Flask(__name__, static_url_path='')

webapp.config["DEBUG"] = True
webapp.config["DEBUG_TB_INTERCEPT_REDIRECTS"] = False
webapp.config['PROPAGATE_EXCEPTIONS'] = True
# Ensure that debug mode is *on*
# app.debug = True
# Set the secret key to some random bytes. Keep this really secret!
webapp.secret_key = b'_5#y2L"F4Q8z\n\xec]/'
# Enable flask session cookies
webapp.config['SECRET_KEY'] = 'key'

# регистрируем представление для скачивания файлов
from webapp.download.views import download_blueprint
webapp.register_blueprint(download_blueprint)


