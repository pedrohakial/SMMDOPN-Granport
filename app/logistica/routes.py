
from app.logistica import blueprint
from flask import render_template, redirect, url_for, request
from flask_login import login_required, current_user
from app import login_manager
from jinja2 import TemplateNotFound
from app.base.forms import (
    LoginForm, 
    CreateAccountForm
)
from app.logistica.forms import (
    CadastroBookingForm 
)

from app.logistica.models import (
        CadastroBooking,
        NavioViagem,
        MovimentaçãoBooking,
        MovimentaçãoNavioViagem

        )

@blueprint.route('/index')
@login_required
def index():

    return render_template('index.html', segment='index')



@blueprint.route('/booking')
@login_required
#inserir nivel de usuário
def booking():
    form = CadastroBookingForm(request.form)
    return render_template('booking.html', form=form)



@blueprint.route('/navio-projeto')
@login_required
#inserir nivel de usuario
def navio_projeto():

    return render_template('navio-projeto.html')

