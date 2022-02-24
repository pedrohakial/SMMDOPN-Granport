# -*- encoding: utf-8 -*-

from flask import Blueprint

blueprint = Blueprint(
    'files_blueprint',
    __name__,
    url_prefix='',
    template_folder='templates',
    static_folder='static'

)