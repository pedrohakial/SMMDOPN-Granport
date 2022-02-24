from flask_wtf import FlaskForm
from wtforms import (
    TextField, 
    PasswordField,
    IntegerField, 
    SelectMultipleField, 
    DateTimeField, 
    RadioField,
    SubmitField,
    StringField,
    SelectField,
    SelectMultipleField

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

