
from flask_login import UserMixin
from sqlalchemy import Binary, Column, Integer, String, DateTime, Float
from datetime import datetime

from ..models import User
from app import db, login_manager

# O Cadastro em si
class CadastroClientes(db.Model):
    
    __tablename__ = 'CadastroClientes'

    id = Column(Integer, primary_key=True)
    user_id = Column(String)
    user_email = Column(String)
    date_created = Column(DateTime, default=datetime.utcnow)
    cnpj = Column(String, unique=True)
    cep = Column(String)
    endereço = Column(String)
    bairro = Column(String)
    complemento = Column(String)
    nome_empresa = Column(String, unique=True)
    razão_social = Column(String, unique=True)
    cidade = Column(String)
    estado = Column(String)
    segmento_mercado = Column(String)
    país = Column(String)
    inscrição_estadual = Column(String, unique=True)
    

    def to_select2(self):
        return {
            'id': self.id,
            'text': self.nome_empresa,
        }
 
    def to_dict(self):
        return {
            'nome_empresa': self.nome_empresa,
            'cnpj': self.cnpj,
            'razao_social': self.razão_social,
            'date_created': self.date_created,
            'segmento_mercado': self.segmento_mercado,
            'cidade': self.cidade,
            'estado': self.estado,
            'endereco': self.endereço
        }
    def __repr__(self):
        return str(self.cnpj)
        return stir(self.nome_empresa)

# Cadastro Operacional -  qual o tipo de operação para a carga em específico
class CadastroOperacional(db.Model):                                        
   
    __tablename__ = 'CadastroOperacional'

    id = Column(Integer, primary_key=True)
    carga = Column(String)
    peso_bruto = Column(Integer)
    peso_liquido = Column(Integer)
    descrição_da_carga = Column(String)
    quantidade_de_cargas = Column(Integer)
    peso_unitário = Column(Integer)
    porto_origem = Column(String) 
    porto_destino = Column(String)
    local_de_entrega = Column(String) 
    endereço_de_entrega = Column(String) 
    cidade_de_origem = Column(String)
    embalagens = Column(String) 
    # RESPONSA DA OPERAÇÃO tipo_de_caminhão = SelectMultipleField('Tipo de Caminhão'               ,validators=[DataRequired()])                      # tipos de caminhão LS, L por ai...
    # não precisa para o comercial quem define é a operação tipo_de_semi_reboque = SelectMultipleField()                  # tipo de semi reboque que a carreta precisa puxar
    apoio_na_coleta = Column(String)
    peso_da_carga = Column(Integer)
    tipo_de_container = Column(String)
    cnpj = Column(String)
    razão_social = Column(String)
    destinatário_remetente = Column(String)
    endereço_rementente = Column(String)
    cnpj_remetente = Column(String)
    nome_razão_social_rementente = Column(String)
    bairro_remetente = Column(String)
    cep_remetente = Column(String)
    uf_remetente = Column(String)
    telefone_remetente = Column(String)
    município_remetente = Column(String)
    inscrição_estadual_remetente = Column(String)
    


    def __repr__(self):
        return str(self.cnpj)
        return str(self.razão_social)
        return str(self.tipo_de_operação)
        
    
class EscopoDeServiço(db.Model):
    __tablename__ = 'EscopoDeServiço'

    id = Column(Integer, primary_key=True)
    user_id = Column(String)
    user_email = Column(String)
    date_created = Column(DateTime, default=datetime.utcnow)
    empresa_cliente = Column(String)
    cidade_origem = Column(String)
    estado_origem = Column(String)
    cidade_destino = Column(String)
    estado_destino = Column(String)
    tipo_de_operação = Column(String) 
    porto_origem = Column(String)
    porto_destino = Column(String)
    tipo_embalagem = Column(String, nullable=True)
    tipo_de_carga = Column(String, nullable=True)
    quantidade_volumes =Column(String, nullable=True)
    dimensões_carga_excedente =Column(String, nullable=True)
    valor_mercadoria = Column(String, nullable=True)
    seguro_cliente = Column(String, nullable=True)
    seguro_fornecedor =Column(String, nullable=True)
    seguro_transportador =Column(String, nullable=True)
    armazenagem = Column(String, nullable=True)
    implementos_mov_cargas = Column(String, nullable=True)
    pontos_atenção = Column(String, nullable=True)
    remonte_mercadoria =Column(String, nullable=True)
    max_remonte = Column(String, nullable=True)
    transporte_origem =Column(String, nullable=True)
    tipo_transporte = Column(String, nullable=True)
    tipo_veículo = Column(String, nullable=True)
    material_coleta =Column(String, nullable=True)
    peiação = Column(String, nullable=True)
    dessecantes = Column(String, nullable=True)
    ifyes_dessecantes =Column(String, nullable=True)
    tmp_livre_carregamento =Column(String, nullable=True)
    op_cavalo_atrelado = Column(String, nullable=True)
    tmp_cavalo_atrelado = Column(String, nullable=True)
    ajudantes = Column(String, nullable=True)
    ifyes_ajudantes = Column(String, nullable=True)
    consolidação_origem = Column(String, nullable=True)
    tipo_estufagem =Column(String, nullable=True)
    qnt_ajudantes = Column(String, nullable=True)
    dessecant_cont = Column(String, nullable=True)
    ifyes_dessecant_cont = Column(String, nullable=True)
    material_estufagem = Column(String, nullable=True)
    tipo_de_container = Column(String, nullable=True)
    tamanho_container = Column(String, nullable=True)
    operação_contratada_destino = Column(String, nullable=True)
    transporte_destino = Column(String, nullable=True)
    tipo_coleta_destino = Column(String, nullable=True)
    tipo_veiculo_dest = Column(String, nullable=True)
    período_disposição_dest = Column(String, nullable=True)
    operação_cavalo_dest = Column(String, nullable=True)
    periodo_cavalo_dest = Column(String, nullable=True)
    op_munck = Column(String, nullable=True)
    periodo_op_munck =Column(String, nullable=True)
    ajudantes_dest = Column(String, nullable=True)
    ifyes_ajudantes_dest = Column(String, nullable=True)
    conferentes_dest = Column(String, nullable=True)
    ifyes_conferentes_dest = Column(String, nullable=True)
    desconsolidação_dest = Column(String, nullable=True)
    resp_retirada_mercadoria_dest = Column(String, nullable=True)
    temp_livre_armazenamento_dest = Column(String, nullable=True)
    tipo_desova_dest = Column(String, nullable=True)
    ajudantes_dest_desova = Column(String, nullable=True)

#Aqui as propostas em si, que serão enviadas para os clientes.
class PropostaComercial(db.Model):                             
    __tablename__ = 'PropostaComercial'

    id = Column(Integer, primary_key=True)
    user_id = Column(String)
    user_email = Column(String)
    date_created = Column(DateTime, default=datetime.utcnow)
    nome_empresa = Column(String)
    valor_tarifa_ton = Column(Float)
    valor_tarifa_m3 = Column(Float)
    valor_do_frete_rodo = Column(Integer) 
    validade = Column(DateTime)

# Modelo para o CRM
class CRM(db.Model):                             
    
    __tablename__ = 'CRM'

    id = Column(Integer, primary_key=True)
    user_id = Column(String)
    user_email = Column(String)
    date_created = Column(DateTime, default=datetime.utcnow)
    nome = Column(String, unique=True)
    cep = Column(String, unique=True)
    cargo = Column(String)
    telefone = Column(String, unique=True)
 
    def __repr__(self):
        return str(self.cnpj)
        return stir(self.nome_empresa)

# Cadastro dos fornecedores de serviços
class CadastroFornecedores(db.Model):                              
   

    __tablename__ = 'CadastroFornecedores'

    id = Column(Integer, primary_key=True)
    estado = Column(String)
    tipo = Column(String)
    cnpj = Column(String)
    razão_social =Column(String)
    nome_fantasia = Column(String)
    cep = Column(String)
    endereço = Column(String) 
    complemento = Column(String)
    bairro = Column(String) 
    município = Column(String)
    telefone = Column(String)
    inscrição_estadual = Column(String)
    país = Column(String)
    e_mail = Column(String)
   

# Formulário para o Termo de Ocorrência  
class CadastroTermoDeOcorrencia(db.Model):                       

    __tablename__ = 'CadastroTermodeOCorrencia'


    id = Column(Integer, primary_key=True)
    formalização_da_reclamação = Column(String) 
    primeira_vez = Column(String)
    localidade = Column(String)
    data = Column(String)
    cnpj = Column(String)
    nome_empresa = Column(String)
    nota_fiscal = Column(String)
    CTe = Column(String)
    trânsito_da_carga =Column(String) 
    cliente_identificou = Column(String)
    granport_foi_acionada = Column(String)
    manifestou_ocorrência = Column(String)
    posterior_ao_recebimento = Column(String)
    ainda_no_veículo = Column(String)
    ato_descarga = Column(String)
    descrição_relato = Column(String)
    carga = Column(String)
    containers = Column(String)
    embalagem = Column(String)
    veículos = Column(String)
    motorista = Column(String)
    tipo_de_carga = Column(String)
    tipo_de_embalagem = Column(String)
    considerações_finais = Column(String)

# Termos de Proposta Comercial

class ServiçoDeTerminal(db.Model):
    
    __tablename__ = 'ServiçoDeTerminal'


    id = Column(Integer, primary_key=True)
    itens = Column(String) 
    user_id = Column(String)
    user_email = Column(String)
    date_created = Column(DateTime, default=datetime.utcnow)




# tipo de operação
class TipoDeColeta(db.Model):
    
    __tablename__ = 'TipoDeColeta'


    id = Column(Integer, primary_key=True)
    itens = Column(String) 
    user_id = Column(String)
    user_email = Column(String)
    date_created = Column(DateTime, default=datetime.utcnow)



# tipo de operação
class PierPorta(db.Model):
    
    __tablename__ = 'PierPorta'


    id = Column(Integer, primary_key=True)
    itens = Column(String) 
    user_id = Column(String)
    user_email = Column(String)
    date_created = Column(DateTime, default=datetime.utcnow)


# tipo de operação
class PortaPier(db.Model):
    
    __tablename__ = 'PortaPier'


    id = Column(Integer, primary_key=True)
    itens = Column(String) 
    user_id = Column(String)
    user_email = Column(String)
    date_created = Column(DateTime, default=datetime.utcnow)


# tipo de operação
class PierPier(db.Model):
    
    __tablename__ = 'PierPier'


    id = Column(Integer, primary_key=True)
    itens = Column(String) 
    user_id = Column(String)
    user_email = Column(String)
    date_created = Column(DateTime, default=datetime.utcnow)

# tipo de operação
class PortaPorta(db.Model):
    
    __tablename__ = 'PortaPorta'


    id = Column(Integer, primary_key=True)
    itens = Column(String) 
    user_id = Column(String)
    user_email = Column(String)
    date_created = Column(DateTime, default=datetime.utcnow)

# Condições comerciais como free time, demurrage
class CondiçõesComerciais(db.Model):
    
    __tablename__ = 'CondiçõesComerciais'


    id = Column(Integer, primary_key=True)
    itens = Column(String) 
    user_id = Column(String)
    user_email = Column(String)
    date_created = Column(DateTime, default=datetime.utcnow)

# Condições Gerais da venda como prazo de pagamento
class CondiçõesGerais(db.Model):
    
    __tablename__ = 'CondiçõesGerais'


    id = Column(Integer, primary_key=True)
    itens = Column(String) 
    user_id = Column(String)
    user_email = Column(String)
    date_created = Column(DateTime, default=datetime.utcnow)

# São as informações da coleta 
class Coleta(db.Model):
    
    __tablename__ = 'Coleta'


    id = Column(Integer, primary_key=True)
    itens = Column(String) 
    user_id = Column(String)
    user_email = Column(String)
    date_created = Column(DateTime, default=datetime.utcnow)


# São as informações da coleta 

# São as informações da coleta 
class PortoPorta(db.Model):
    
    __tablename__ = 'PortoPorta'


    id = Column(Integer, primary_key=True)
    itens = Column(String) 
    user_id = Column(String)
    user_email = Column(String)
    date_created = Column(DateTime, default=datetime.utcnow)


# São as informações da coleta 
class PortoPorto(db.Model):
    
    __tablename__ = 'PortoPorto'


    id = Column(Integer, primary_key=True)
    itens = Column(String) 
    user_id = Column(String)
    user_email = Column(String)
    date_created = Column(DateTime, default=datetime.utcnow)
# Esta tabela vai ser usada para criar os tags e registrar os valores juntos
# com os tipos de operação e como será medido

class Composição_e_Contabilidade(db.Model):
    
    __tablename__ = 'Composição e Contabilidade'


    id = Column(Integer, primary_key=True)
    itens = Column(String) 
    user_id = Column(String)
    user_email = Column(String)
    date_created = Column(DateTime, default=datetime.utcnow)

















    
