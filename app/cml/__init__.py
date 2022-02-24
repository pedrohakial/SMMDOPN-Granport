from flask import Blueprint

cml = Blueprint(
        'cml',
    __name__,
    url_prefix='/comercial/',
    template_folder='templates',
    static_folder='static'
)
