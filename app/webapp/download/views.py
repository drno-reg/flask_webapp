from flask import Blueprint, render_template, redirect, url_for, request, flash, send_file, send_from_directory


from webapp.views import webapp, logging


# объявление модели
download_blueprint = Blueprint('download_blueprint', __name__)


@download_blueprint.route('/.well-known/pki-validation/<filename>', methods=['GET'])
def return_file(filename):
    return send_from_directory(directory='files', filename='filename', as_attachment=True)
