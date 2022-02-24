# The routes file, is the heart of each module of the app
# it calls and aggregates the various files inside its file
# And forms each folder so it is intanciated at the beginning
# If the folder or file is not improted correctly here
# it will be void.



# The application imports the current user, also all the modules required
# This import secures the correct user mngmnt
from flask import jsonify, render_template, redirect, request, url_for
from flask_login import (
    current_user,
    login_required,
    login_user,
    logout_user
)
# This retrieves the modules for the forms
from app import db, login_manager
from app.cml import blueprint
from app.cml.forms import (
   CadastroClientesForm, 
   CadastroContatoClienteForm,
   PropostaComercialForm,
   CadastroFornecedorForm,
   CadastroTermoDeOcorrênciaForm,
   CRMForm,
   EscopoDeServicoForm
)


from app.decorators import admin_required, permission_required

from flask import render_template, redirect, url_for, request, flash
from flask_login import login_required, current_user
from jinja2 import TemplateNotFound

# Here we call from the models each object
# to use the request for 

from app.base.models import User

from app.cml.models import (
        CadastroClientes,
        PropostaComercial,
        CadastroFornecedores,
        CadastroTermoDeOcorrencia,
        CRM,
        EscopoDeServiço

)

from app.base.util import verify_pass



# Data api for clients 
@blueprint.route('/data_ajax', methods=['GET', 'POST'])
def data_ajax():
    return {'data': [cadastroclientes.to_dict() for cadastroclientes  in CadastroClientes.query]}

@blueprint.route('/tabela-clientes.html')
@login_required
def tabela_clientes_ajax():
    return render_template('tabela-clientes.html')

@blueprint.route('/tabela-clientes.html', methods=['GET'])
@login_required
def tabela_clientes():
    cadastro_clientes = CadastroClientes.query

    return render_template('tabela-clientes.html', cadastro_clientes=cadastro_clientes)


@cml.route('/cadastro-propostas.html', methods=['GET', 'POST'])
@login_required
@admin_required
def cadastro_propostas():
    query = CadastroClientes.query
    form  = PropostaComercialForm(request.form)

    form.nome_empresa.choices = [(str(nome.id), repr(nome.nome_empresa)) for nome in CadastroClientes.query.all()]
    
    if request.method == 'POST':
        flash(str(form.nome_empresa.data), 'Cadastrado com Sucesso')
        
        nome_empresa  = request.form['nome_empresa']
        valor_tarifa_ton = request.form['valor_ton']
        valor_m3 = request.form['valor_m3']
        valor_do_frete_rodo = request.form['frete_rodo']
        validade = request.form['validade']


        user_id = current_user.username 
        user_email = current_user.email


        proposta_nova = PropostaComercial(
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
    return render_template('cadastro-propostas.html', form=form)


@login_required
def list_html():
    return render_template('list-index.html')



@blueprint.route('/cml-html')
@login_required
def list_html():
    return render_template('list-index.html')


@blueprint.route('/escopo-de-serviços.html', methods=['GET','POST'])
@login_required
def escopo_de_serviços():
    
# chama o form e requisita ele
    query = CadastroClientes.query
    form  = EscopoDeServicoForm(request.form)
    
    form.empresa_cliente.data = None
    form.cidade_origem.data = None
    form.estado_origem.data = None
    form.estado_destino.data = None
    form.cidade_destino.data = None
    form.tipo_de_operação.data = None
    
    # Aqui vem um monte de itens do Perfil

    form.tipo_embalagem.data = None
    form.tipo_de_carga.data = None
    form.quantidade_volumes.data = None
    form.dimensões_carga_excedente.data = None
    form.valor_mercadoria.data = None
    form.seguro_cliente.data = None
    form.seguro_fornecedor.data = None
    form.seguro_transportador.data = None
    form.armazenagem.data = None
    form.maquinário_mov.data = None
    form.pontos_atenção.data = None
    form.remonte_mercadoria.data = None
    form.max_remonte.data = None
    form.transporte_origem.data = None
    form.tipo_transporte.data = None
    form.tipo_veículo.data = None
    form.material_coleta.data = None
    form.peiação.data = None
    form.dessecantes.data = None
    form.ifyes_dessecantes.data = None
    form.tmp_livre_carregamento.data = None
    form.op_cavalo_atrelado.data = None
    form.tmp_cavalo_atrelado.data = None
    form.ajudantes.data = None
    form.ifyes_ajudantes.data = None
    form.consolidação_origem.data = None
    form.tipo_estufagem.data = None
    form.qnt_ajudantes.data = None
    form.dessecant_cont.data = None
    form.ifyes_dessecant_cont.data = None
    form.material_estufagem.data = None
    form.tipo_de_container.data = None
    form.tamanho_container.data = None
    form.operação_contratada_destino.data = None
    form.transporte_destino.data = None
    form.tipo_coleta_destino.data = None
    form.tipo_veículo_dest.data = None
    form.período_disposição_dest.data = None
    form.operação_cavalo_dest.data = None
    form.periodo_cavalo_dest.data = None
    form.op_munck.data = None
    form.periodo_op_munck.data = None
    form.ajudantes_dest.data = None
    form.ifyes_ajudantes_dest.data = None
    form.conferentes_dest.data = None
    form.ifyes_conferentes_dest.data = None
    form.desconsolidação_dest.data = None
    form.resp_retirada_mercadoria_dest.data = None
    form.temp_livre_armazenamento_dest.data = None
    form.tipo_desova_dest.data = None
    form.ajudantes_dest_desova.data = None



    if request.method == "POST":
        empresa_cliente = request.form['empresa_cliente']
        cidade_origem = request.form['cidade_origem']
        estado_origem = request.form['estado_origem']
        cidade_destino = request.form['cidade_destino']
        estado_destino = request.form['estado_destino']
        tipo_de_operação = request.form['tipo_de_operação']
        tipo_embalagem = request.form.getlist('tipo_embalagem')
        tipo_de_carga = request.form.getlist('tipo_de_carga')
        quantidade_volumes = request.form['quantidade_volumes']
        dimensões_carga_excedente = request.form['dimensões_carga_excedente']
        valor_mercadoria = request.form['valor_mercadoria']
        seguro_cliente = request.form['seguro_cliente']
        seguro_fornecedor = request.form['seguro_fornecedor']
        seguro_transportador = request.form['seguro_transportador']
        armazenagem = request.form['armazenagem']
        implementos_mov_carga = request.form.getlist('maquinário_mov')
        pontos_atenção = request.form.getlist('pontos_atenção')
        remonte_mercadoria = request.form['remonte_mercadoria']
        max_remonte = request.form['max_remonte']
        transporte_origem = request.form['transporte_origem']
        tipo_transporte = request.form['tipo_transporte']
        tipo_veículo = request.form['tipo_veículo']
        material_coleta = request.form.getlist('material_coleta')
        peiação = request.form['peiação']
        dessecantes = request.form['dessecantes']
        ifyes_dessecantes = request.form['ifyes_dessecantes']
        tmp_livre_carregamento = request.form['tmp_livre_carregamento']
        op_cavalo_atrelado = request.form['op_cavalo_atrelado']
        tmp_cavalo_atrelado = request.form['tmp_cavalo_atrelado']
        ajudantes = request.form['ajudantes']
        ifyes_ajudantes = request.form['ifyes_ajudantes'] 
        consolidação_origem = request.form['consolidação_origem']
        tipo_estufagem = request.form['tipo_estufagem']
        qnt_ajudantes = request.form['qnt_ajudantes']
        dessecant_cont = request.form['dessecant_cont']
        ifyes_dessecant_cont = request.form['ifyes_dessecant_cont']
        material_estufagem = request.form.getlist('material_estufagem')
        tipo_de_container = request.form.getlist('tipo_de_container')
        tamanho_container = request.form['tamanho_container']
        operação_contratada_destino = request.form['operação_contratada_destino']
        transporte_destino = request.form['transporte_destino']
        tipo_coleta_destino = request.form['tipo_coleta_destino']
        tipo_veículo_dest = request.form['tipo_veículo_dest']
        período_disposição_dest = request.form['período_disposição_dest']
        operação_cavalo_dest = request.form['operação_cavalo_dest']
        periodo_cavalo_dest = request.form['periodo_cavalo_dest']
        op_munck = request.form['op_munck']
        periodo_op_munck = request.form['periodo_op_munck']
        ajudantes_dest = request.form['ajudantes_dest']
        ifyes_ajudantes_dest = request.form['ifyes_ajudantes_dest']
        conferentes_dest = request.form['conferentes_dest']
        ifyes_conferentes_dest = request.form['ifyes_conferentes_dest']
        desconsolidação_dest = request.form['desconsolidação_dest']
        resp_retirada_mercadoria_dest = request.form['resp_retirada_mercadoria_dest']
        temp_livre_armazenamento_dest = request.form['temp_livre_armazenamento_dest']
        tipo_desova_dest = request.form['tipo_desova_dest']
        ajudantes_dest_desova = request.form['ajudantes_dest_desova']
        operação_nova = EscopoDeServiço(
                empresa_cliente=empresa_cliente,
                cidade_origem=cidade_origem,
                estado_origem=estado_origem,
                cidade_destino=cidade_destino,
                estado_destino=estado_destino,
                tipo_de_operação=tipo_de_operação,
                tipo_embalagem = tipo_embalagem, 
                tipo_de_carga =tipo_de_carga,
                quantidade_volumes =quantidade_volumes,
                dimensões_carga_excedente =dimensões_carga_excedente,
                valor_mercadoria =valor_mercadoria,  
                seguro_cliente =seguro_cliente,  
                seguro_fornecedor =seguro_fornecedor,  
                seguro_transportador =seguro_transportador, 
                armazenagem =armazenagem,  
                implementos_mov_cargas =implementos_mov_carga,  
                pontos_atenção =pontos_atenção,  
                remonte_mercadoria =remonte_mercadoria,  
                max_remonte =max_remonte,  
                transporte_origem =transporte_origem,  
                tipo_transporte =tipo_transporte,  
                tipo_veículo =tipo_veículo,  
                material_coleta =material_coleta,  
                peiação =peiação,  
                dessecantes =dessecantes,  
                ifyes_dessecantes =ifyes_dessecantes,  
                tmp_livre_carregamento =tmp_livre_carregamento,  
                op_cavalo_atrelado =op_cavalo_atrelado,  
                tmp_cavalo_atrelado =tmp_cavalo_atrelado,  
                ajudantes =ajudantes,  
                ifyes_ajudantes =ifyes_ajudantes,  
                consolidação_origem =consolidação_origem,  
                tipo_estufagem =tipo_estufagem,  
                qnt_ajudantes =qnt_ajudantes,  
                dessecant_cont =dessecant_cont,  
                ifyes_dessecant_cont =ifyes_dessecant_cont,  
                material_estufagem =material_estufagem,  
                tipo_de_container =tipo_de_container,  
                tamanho_container =tamanho_container,  
                operação_contratada_destino =operação_contratada_destino,  
                transporte_destino =transporte_destino, 
                tipo_coleta_destino =tipo_coleta_destino,  
                tipo_veiculo_dest =tipo_veículo_dest,  
                período_disposição_dest =período_disposição_dest,  
                operação_cavalo_dest =operação_cavalo_dest,  
                periodo_cavalo_dest =periodo_cavalo_dest,  
                op_munck =op_munck,  
                periodo_op_munck =periodo_op_munck,  
                ajudantes_dest =ajudantes_dest,  
                ifyes_ajudantes_dest =ifyes_ajudantes_dest,  
                conferentes_dest =conferentes_dest,  
                ifyes_conferentes_dest =ifyes_conferentes_dest,  
                desconsolidação_dest =desconsolidação_dest,  
                resp_retirada_mercadoria_dest =resp_retirada_mercadoria_dest,  
                temp_livre_armazenamento_dest =temp_livre_armazenamento_dest, 
                tipo_desova_dest =tipo_desova_dest,  
                ajudantes_dest_desova =ajudantes_dest_desova
                )

        db.session.add(operação_nova)
        db.session.commit()
        return render_template('index.html', 
            msg='Operação Cadastrada', 
            success=True)

    else:
        return render_template("escopo-de-serviços.html", form=form)




@blueprint.route('/escopo-de-serviço.html', methods=['GET','POST'])
@login_required
def escopo_de_servicos():
    
# chama o form e requisita ele
    query = CadastroClientes.query
    form  = EscopoDeServicoForm(request.form)
    
    form.empresa_cliente.data = None
    if request.method == "POST":
        empresa_cliente = request.form['empresa_cliente']
    return render_template('escopo-de-serviço.html', form=form)



@blueprint.route('/cadastro-clientes.html', methods=['GET','POST'])
@login_required
def cadastro_clientes():

    # chama o form e requisita ele
    cadastro_clientes_form = CadastroClientesForm(request.form) 

    cadastro_clientes_form.cnpj.data = None
    cadastro_clientes_form.cep.data = None
    cadastro_clientes_form.endereço.data = None
    cadastro_clientes_form.bairro.data = None
    cadastro_clientes_form.complemento.data = None
    cadastro_clientes_form.nome_empresa.data = None
    cadastro_clientes_form.razão_social.data = None
    cadastro_clientes_form.cidade.data = None
    cadastro_clientes_form.estado.data = None
    cadastro_clientes_form.segmento_mercado.data = None
    cadastro_clientes_form.país.data = None
    cadastro_clientes_form.inscrição_estadual.data = None
    
    if request.method =="POST":
        cnpj = request.form['cnpj']
        cep = request.form['cep']
        endereço = request.form['endereço']
        bairro = request.form['bairro']
        complemento = request.form['complemento']
        nome_empresa = request.form['nome_empresa']
        razão_social = request.form['razão_social']
        cidade = request.form['cidade']
        estado = request.form['estado']
        segmento_mercado = request.form['segmento_mercado']
        país = request.form['país']
        inscrição_estadual = request.form['inscrição_estadual']
        user_id = current_user.username 
        user_email = current_user.email

        cadastro_novo = CadastroClientes(
            cnpj=cnpj,
            cep=cep,
            endereço=endereço,
            bairro=bairro,
            complemento=complemento,
            nome_empresa=nome_empresa,
            razão_social=razão_social,
            cidade=cidade,
            estado=estado,
            segmento_mercado=segmento_mercado,
            país=país,
            inscrição_estadual=inscrição_estadual,
            user_id=user_id,
            user_email=user_email
)

        db.session.add(cadastro_novo)
        db.session.commit()

        flash("Cadastro realizado com sucesso")
        return render_template('index.html', 
            msg='Empresa Cadastrada', 
            success=True)

    else:
        return render_template("cadastro-clientes.html", form=cadastro_clientes_form)


@blueprint.route('/comercial-crm.html')
@login_required
def cml_crm():

    crm_form = CRMForm(request.form)

    return render_template('comercial-crm.html', form=crm_form)


@blueprint.route('/cadastro-proposta.html')
@login_required
def cadastro_proposta():
    return render_template('cadastro-proposta.html')

@blueprint.route('/cml-clientes-e-cargas.html')
@login_required
def cml_clientes_e_cargas():
    return render_template('cml-clientes-e-cargas.html')

@blueprint.route('/pipeline.html')
@login_required
def cml_pipeline():
    return render_template('pipeline.html')

@blueprint.route('/cml-cadastro-clientes-2.html', methods=['GET','POST'])
@login_required
def cml_cadastro_clientes_2():
    # chama o form e requisita ele
    cadastro_clientes_form = CadastroClientesForm(request.form) 
    # estabelece os objetos e requisita eles do formulário original 
    cnpj = request.form['cnpj']
    inscrição_estadual = request.form['inscrição_estadual']
    cep = request.form['cep']
    endereço = request.form['endereço']
    bairro = request.form['bairro']
    complemento = request.form['complemento']
    nome_empresa = request.form['nome_empresa']
    razão_social = request.form['razão_social']
    cidade = request.form['cidade']
    estado = request.form['estado']
    país = request.form['país']
    tipo_de_empresa = request.form['tipo_de_empresa']

        # uso o objeto clientes_cadastrados repetidamente, pq o objetivo
        # é checar na base de dados se cada parte do formulário já foi adicionada
        # se foi então retorna uma msg na mesma página dizendo que a empresa já foi cadastrada



    # Procura se existe um cnpj na base
    clientes_cadastrados = CadastroClientes.query.filter_by(cnpj=cnpj).first()
    if clientes_cadastrados:
        return render_template( 'cml-cadastro-clientes.html', 
                                msg='Empresa já cadastrada',
                                success=False,
                                form=cadastro_clientes_form)


    clientes_cadastrados = CadastroClientes(**request.form)
    db.session.add(clientes_cadastrados)
    db.session.commit()
    
    return render_template('cml-cadastro-clientes.html', 
            msg='Empresa Cadastrada', 
            sucess=True, 
            form=cadastro_clientes_form)
    
    return render_template('cml-cadastro-clientes.html',
            form=cadastro_clientes_form )

