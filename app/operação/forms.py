
from flask_wtf import FlaskForm
from wtforms import (
    TextField, 
    IntegerField, 
    SelectMultipleField, 
    DateTimeField, 
    RadioField,
    SubmitField,
    StringField,
    SelectField,
    SelectMultipleField,
    DecimalField

)

from wtforms.validators import InputRequired, Email, DataRequired
class CadastroBookingForm(FlaskForm):                       
    booking_number = TextField('Booking Number', [InputRequired(message='Adicione o Booking Number')])
    armador  = TextField('Armador', [InputRequired(message='Adicione o Armador')])
    navio_viagem = TextField('Navio Viagem', [InputRequired(message='Adicionar Navio Viagem')])
    proposta_modal =TextField('Proposta Modal', [InputRequired(message='Adicionar Proposta Modal')])
    porto_origem = TextField('Porto Origem', [InputRequired(message='Adicionar Porto de Origem')])
    porto_destino =TextField('Porto Destino', [InputRequired(message='Adicionar Porto de Destino')])
    mercadoria = TextField('Tipo Mercadoria', [InputRequired(message='Adicionar Tipo de Mercadoria')])
    quantidade_containers_20 =IntegerField('Quantidade de Containers 20', [InputRequired(message='Adicionar Quantidade de Containers')])
    tipo_containers_20 = SelectMultipleField(
            'Tipo de Container de 20',
            choices = [
                (' HC',' HC'),
                (' Seacell',' Seacell'),
                (' Dry',' Dry'),
                (' Open Top',' Open Top'),
                (' Flat Rack',' Flat Rack'),
                (' Reefer',' Reefer'),
                (' Isotank Vazio e Limpo',' Isotank Vazio e Limpo'),
                (' Carga Geral ',' Carga Geral '),
                ]
            )
    peso_bruto_containers_20=IntegerField('Peso Bruto Containers 20', [InputRequired(message='Adicionar Peso Bruto Containers')])
    quantidade_containers_40 =IntegerField('Quantidade de Containers 40' , [InputRequired(message='Adicionar Quantidade de Containers')])
    tipo_containers_40 = SelectMultipleField(
            'Tipo de Container de 40',
            choices = [
                (' HC',' HC'),
                (' Seacell',' Seacell'),
                (' Dry',' Dry'),
                (' Open Top',' Open Top'),
                (' Flat Rack',' Flat Rack'),
                (' Reefer',' Reefer'),
                (' Isotank Vazio e Limpo',' Isotank Vazio e Limpo'),
                (' Carga Geral ',' Carga Geral '),
                ]
            )
    peso_bruto_containers_40 =IntegerField('Peso Bruto Containers 40', [InputRequired(message='Adicionar Peso Bruto Containers')])
    terminal_vazios =TextField('Terminal dos Vazios', [InputRequired(message='Adicionar Terminal dos Vazios')])
    deadline_documento=  DateTimeField('Data do Deadline Documento'                       ,id='deadline_documento_create'                           ,validators=[DataRequired()])
    deadline_carga =  DateTimeField('Data Deadline da Carga'                       ,id='deadline_carga_create'                           ,validators=[DataRequired()])
    submit = SubmitField("Cadastrar")

class GateRegistroForm(FlaskForm):

    caminhão_placa = TextField('Placa Caminhão', [InputRequired(message='Adicione a placa do caminhão')])
    tipo_caminhão = SelectField(
            'Tipo de Caminhão',
            choices = [
                ('Caminhão 3/4','Caminhão 3/4'),
                ('Carro','Carro'),
                ('Cavalo','Cavalo'),
                ('Desconhecido','Desconhecido'),
                ('Furgão','Furgão'),
                ('L','L'),
                ('LS','LS'),
                ('Médio Aberto','Médio Aberto'),
                ('Médio Baú','Médio Baú'),
                ('Motocicleta','Motocicleta'),
                ('Normal','Normal'),
                ('Pickup Aberto','Pickup Aberto'),
                ('Pickup Baú','Pick Baú'),
                ('Toco aberto','Toco Aberto'),
                ('Toco Baú','Toco Baú'),
                ('Truck Aberto','Truck Aberto'),
                ('Truck Baú','Truck Baú'),
                ('Van','Van'),
                ('VLC','VLC'),
                ('VUC','VUC'),
                ]
            )
    eixos = IntegerField('Quantidade de Eixos', [InputRequired(message='Inserir a quantidade de eixos do caminhão')])
    reboque_placa = TextField('Placa do reboque', [InputRequired(message='Inserir a placa do reboque')])
    tipo_reboque = SelectField('Tipo de Reboque',
            choices = [
                ('Carreta Aberta','Carreta Aberta'),
                ('Carreta Baú','Carreta Baú'),
                ('Cavalo','Cavalo'),
                ('Porta Container 20','Porta Container 20'),
                ('Porta Container 20 Bitrem','Porta Container 20 Bitrem'),
                ('Porta Container 40',' Porta Container 40'),
                ('Porta Container 40 Bitrem','Porta Container 40 Bitrem'),
                ('Plataforma','Plataforma'),
                ('Prancha Rebaixada','Prancha Rebaixada'),
                ('Sider','Sider'),
                ]
            )
    motorista_nome = TextField('Nome do Motorista', [InputRequired(message='Inserir o nome completo do motorista')])
    rg = TextField('RG do Motorista', [InputRequired(message='Inserir o RG do Motorista')])
    cpf = TextField('CPF do Motorista', [InputRequired(message='Inserir o CPF do Motorista')])
    cnh = TextField('CNH do Motorista', [InputRequired(message='Inserir CNH do Motorista')])
    expedição = TextField('Data da Expedição', [InputRequired(message='Inserir a Data de Expedição')])
    órgão_emitente = TextField('Órgão Emitente', [InputRequired(message='Inserir o Órgão que Emitiu')])
    categoria_cnh = TextField('Categoria da CNH', [InputRequired(message='Inserir a Categoria da CNH')])
    validade_cnh = DateTimeField('Validade da CNH', [InputRequired(message='Inserir a Validade da CNH')])
    tel_celular = TextField('Celular Motorista', [InputRequired(message='Telefone Celular do Motorista')])
    origem = TextField('CNPJ Origem', [InputRequired(message='Inserir o CNPJ daonde a carga se originou')])
    destino = TextField('CNPJ Destino', [InputRequired(message='Inserir o CNPJ para onde a carga sera destinada')])
    submit = SubmitField("Cadastrar")

class NotaFiscalForm(FlaskForm):

    chave_de_acesso = TextField('Chave de Acesso NFe',[InputRequired(message='Inserir a Chave de acesso da NFe')])
    data_emissão = DateTimeField('Data de Emissão',[InputRequired(message='Inserir a data de Emissão da NFe')])
    
    dest_CNPJ = TextField('CNPJ', [InputRequired(message='Inserir o CNPJ do Destinatário')])
    dest_nome = TextField('Nome/Razão Social', [InputRequired(message='Inserir o nome do Destinatário')])
    dest_endereço = TextField('Endereço do Destinatário', [InputRequired(message='Inserir o endereço  do Destinatário')])
    dest_município = TextField('Município', [InputRequired(message='Inserir o município do Destinatário')])
    dest_bairro = TextField('Bairro', [InputRequired(message='Inserir o Bairro do Destinatário')])
    dest_cep = TextField('CEP', [InputRequired(message='Inserir o CEP do Destinatário')])
    dest_uf = TextField('Inserir Estado/UF', [InputRequired(message='Inserir o Estado/UF do Destinatário')])
    dest_insc_estadual = TextField('Inscrição Estadual', [InputRequired(message='Inserir a Inscrição Estadual  do Destinatário')])

    fatura = TextField('Fatura', [InputRequired(message='Inserir o número da Fatura')])
    vencimento = DateTimeField('Vencimento da Fatura', [InputRequired(message='Inserir o Vencimento da Fatura')])
    valor = DecimalField('Valor da Fatura', [InputRequired(message='Inserir o valor da Fatura')])
    
    transportador_nome = TextField('Nome/Razão Social Transportador', [InputRequired(message='Inserir o Nome/Razão Social do Transportador ')])
    resp_frete = TextField('Frete por Conta', [InputRequired(message='Inserir o responsável do frete inicial')])
    código_antt = TextField('Código ANTT', [InputRequired(message='Inserir o Código ANTT do Transportador')])
    placa_veículo = TextField('Placa do Veículo da Transportadora', [InputRequired(message='Inserir a placa do Veículo da Transportadora')])
    trans_uf = TextField('Estado/UF da Transportadora', [InputRequired(message='Inserir o Estado/UF do Transportador')])
    trans_end = TextField('Endereço do Transportador', [InputRequired(message='Inserir o Endereço do Transportador')])
    trans_município = TextField('Município do Transportador', [InputRequired(message='Inserir o Muncípio do Transportador')])
    trans_cnpj = TextField('CNPJ do Transportador', [InputRequired(message='Inserir o CNPJ do Transportador')])
    trans_inscrição_estadual = TextField('Inscrição Estadual do Transportador', [InputRequired(message='Inserir a Inscrição Estadual do Transportador')])
    trans_vol = TextField('Quantidade Volumes Transportados', [InputRequired(message='Inserir a quantidade de Volumes Transportados')])
    trans_espécie = TextField('Espécie de Volume Transporte', [InputRequired(message='Inserir a espécie de Volumes Transportados')])
    
    volume_peso_bruto = TextField('Peso Bruto do Volume', [InputRequired(message='Inserir o Peso Bruto do Volume')])
    volume_peso_líquido = TextField('Peso Líquido do Volume', [InputRequired(message='Inserir o Peso Líquido do Volume')])
    
    dados_adc = TextField('Dados Adicionais', [InputRequired(message='Inserir os dados adicionais')])
    id_usim5  = TextField('Dados da Bobina Numeração do Volume', [InputRequired(message='Inserir a Numeração da Bobina')])
    submit = SubmitField("Cadastrar")
    

    
