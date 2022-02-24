from flask import Blueprint

blueprint = Blueprint(
        'cml_blueprint',
    __name__,
    url_prefix='/comercial/',
    template_folder='templates',
    static_folder='static'
)
