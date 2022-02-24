from app.operação import blueprint
from flask import render_template, redirect, url_for, request 
from flask_login import login_required, current_user
from app import login_manager
from jinja2 import TemplateNotFound
from app.base.forms import (
    LoginForm, 
    CreateAccountForm
)

from app.operação.forms import (

    GateRegistroForm,
    NotaFiscalForm

    )

from app.operação.models import (
        Motorista,
        Transportadora,
        Reboque,
        Caminhão,
        Container,
        Carga,
        MovimentaçãoMotorista,
        MovimentaçãoReboque,
        MovimentaçãoCaminhão,
        MovimentaçãoContainer,
        MovimentaçãoCarga


        )



@blueprint.route('/index')
@login_required
def index():

    return render_template('index.html', segment='index')



@blueprint.route('/registro', methods=['GET', 'POST'])
@login_required
def registro():

    #query = CadastroClientes.query
    form  = NotaFiscalForm(request.form)
    
    # por enquanto query para os itens dos forms
    # está fora de cogitação pela dificuldade adicional
    # em implementar e possivelmente seja melhor 
    # pq reduz a carga na Base de Dados
    #form.nome_empresa.choices = [(str(nome.id), repr(nome.nome_empresa)) for nome in CadastroClientes.query.all()]
   
   

    if request.method == 'POST':
        
        nome_empresa  = request.form['nome_empresa']
        valor_tarifa_ton = request.form['valor_ton']
        valor_m3 = request.form['valor_m3']
        valor_do_frete_rodo = request.form['frete_rodo']
        validade = request.form['validade']


        user_id = current_user.username 
        user_email = current_user.email


        registro_gate_in = PropostaComercial(
                nome_empresa=nome_empresa,
                valor_tarifa_ton =valor_tarifa_ton,  
                valor_tarifa_m3 =valor_m3,
                valor_do_frete_rodo=valor_do_frete_rodo,
                validade=validade,
                user_id=user_id,
                user_email=user_email
                )

        db.session.add(proposta_nova)
        db.session.commit()
    return render_template('registro.html', form=form)

@blueprint.route('/gate-in', methods=['GET', 'POST'])
@login_required
def gate_in():

    #query = CadastroClientes.query
    form  = GateRegistroForm(request.form)
    
    # por enquanto query para os itens dos forms
    # está fora de cogitação pela dificuldade adicional
    # em implementar e possivelmente seja melhor 
    # pq reduz a carga na Base de Dados
    #form.nome_empresa.choices = [(str(nome.id), repr(nome.nome_empresa)) for nome in CadastroClientes.query.all()]
   
   

    if request.method == 'POST':
        
        nome_empresa  = request.form['nome_empresa']
        valor_tarifa_ton = request.form['valor_ton']
        valor_m3 = request.form['valor_m3']
        valor_do_frete_rodo = request.form['frete_rodo']
        validade = request.form['validade']


        user_id = current_user.username 
        user_email = current_user.email


        registro_gate_in = PropostaComercial(
                nome_empresa=nome_empresa,
                valor_tarifa_ton =valor_tarifa_ton,  
                valor_tarifa_m3 =valor_m3,
                valor_do_frete_rodo=valor_do_frete_rodo,
                validade=validade,
                user_id=user_id,
                user_email=user_email
                )

        db.session.add(proposta_nova)
        db.session.commit()
    return render_template('gate-in.html', form=form)



@blueprint.route('/gate-out')
@login_required
def gate_out():

    return render_template('gate-out.html')


@blueprint.route('/descarga')
@login_required
def descarga():

    return render_template('tela-de-descarga.html')



@blueprint.route('/serviço')
@login_required
def serviço():

    return render_template('tela-de-serviço.html')

