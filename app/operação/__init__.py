from flask import Blueprint

blueprint = Blueprint(
        'operação_blueprint',
    __name__,
    url_prefix='/operação/',
    template_folder='templates',
    static_folder='static'
)
