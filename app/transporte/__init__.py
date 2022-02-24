from flask import Blueprint

blueprint = Blueprint(
        'transporte_blueprint',
    __name__,
    url_prefix='/transporte/',
    template_folder='templates',
    static_folder='static'
)
