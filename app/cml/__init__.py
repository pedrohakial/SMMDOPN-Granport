from flask import Blueprint

cml = Blueprint(
        'cml',
    __name__,
    template_folder='templates',
    static_folder='static'
)

from . import routes, errors
from ..models import Permission


@cml.app_context_processor
def inject_permissions():
    return dict(Permission=Permission)
