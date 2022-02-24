
from flask import Blueprint

blueprint = Blueprint(
        'logistica_blueprint',
    __name__,
    url_prefix='/logistica/',
    template_folder='templates',
    static_folder='static'
)
