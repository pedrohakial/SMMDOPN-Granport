from flask_login import UserMixin
from sqlalchemy import Binary, Column, Integer, String, DateTime, Numeric
from datetime import datetime

from app.base.models import User
from app import db, login_manager

# #O Cadastro em si
class Motorista(db.Model):
    
    __tablename__ = 'Motorista'

    id = Column(Integer, primary_key=True)
    user_id = Column(String)
    user_email = Column(String)
    date_created = Column(DateTime, default=datetime.utcnow)
    cpf = Column(String)
    nome  = Column(String)
    tel_celular = Column(String)
    transportadora = Column(String)
    expedição = Column(String)
    órgão_emitente = Column(String)
    numero_cnh  = Column(String)
    categoria = Column(String)
    validade = Column(String)
    #transportadora_id = Column(Integer, ForeignKey('Transportadora.id')) 
    #caminhao_id = Column(Integer, ForeignKey('Caminhão.id')) 
    #container_id = Column(Integer, ForeignKey('Container.id')) 
    #booking_id = Column(Integer, ForeignKey('Booking.id'))
    #carga_id = Column(Integer, ForeignKey('Carga.id'))

class MovimentaçãoMotorista(db.Model):

    __tablename__='MovimentaçãoMotorista'
    
    id = Column(Integer, primary_key=True)
    user_id = Column(String)
    user_email = Column(String)
    date_created = Column(DateTime, default=datetime.utcnow)

class Transportadora(db.Model):
    
    __tablename__ = 'Transportadora'

    id = Column(Integer, primary_key=True)
    user_id = Column(String)
    user_email = Column(String)
    date_created = Column(DateTime, default=datetime.utcnow)
    nome_razão_social = Column(String, unique=True)
    cnpj = Column(String, unique=True)
    endereço = Column(String)
    município = Column(String)
    inscrição_estadual = Column(String)

  #  motoristas = db.relationship('Motorista', backref='transportadora', lazy='dynamic')




class Reboque(db.Model):
    
    __tablename__ = 'Reboque'

    id = Column(Integer, primary_key=True)
    user_id = Column(String)
    user_email = Column(String)
    date_created = Column(DateTime, default=datetime.utcnow)
    placa = Column(String, unique=True)
    tipo_reboque = (String)
    eixos = Column(String, nullable=True)
    placa_reboque = Column(String, nullable=True)
    capacidade = Column(Numeric, nullable=True)


class MovimentaçãoReboque(db.Model):

    __tablename__='MovimentaçãoReboque'
    
    id = Column(Integer, primary_key=True)
    user_id = Column(String)
    user_email = Column(String)
    date_created = Column(DateTime, default=datetime.utcnow)

class Caminhão(db.Model):
    
    __tablename__ = 'Caminhão'

    id = Column(Integer, primary_key=True)
    user_id = Column(String)
    user_email = Column(String)
    date_created = Column(DateTime, default=datetime.utcnow)
    placa = Column(String, unique=True)
    tipo_caminhão = (String)
    eixos = Column(String, nullable=True)
    placa_reboque = Column(String, nullable=True)


class MovimentaçãoCaminhão(db.Model):

    __tablename__='MovimentaçãoCaminhão'
    
    id = Column(Integer, primary_key=True)
    user_id = Column(String)
    user_email = Column(String)
    date_created = Column(DateTime, default=datetime.utcnow)


class Container(db.Model):
    
    __tablename__ = 'Container'

    id = Column(Integer, primary_key=True)
    user_id = Column(String)
    user_email = Column(String)
    date_created = Column(DateTime, default=datetime.utcnow)
    nome = Column(String)
    tara = Column(String)
    payload = Column(String)
    mgw = Column(String)
    data_fabricação = Column(String)
    iso = Column(String)
    tipo = Column(String)
    tamanho = Column(String)
    


class MovimentaçãoContainer(db.Model):

    __tablename__='MovimentaçãoContainer'
    
    id = Column(Integer, primary_key=True)
    user_id = Column(String)
    user_email = Column(String)
    date_created = Column(DateTime, default=datetime.utcnow)




class Carga(db.Model):
    
    __tablename__ = 'Carga'


    id = Column(Integer, primary_key=True)
    user_id = Column(String)
    user_email = Column(String)
    date_created = Column(DateTime, default=datetime.utcnow)


class MovimentaçãoCarga(db.Model):

    __tablename__='MovimentaçãoCarga'
    
    id = Column(Integer, primary_key=True)
    user_id = Column(String)
    user_email = Column(String)
    date_created = Column(DateTime, default=datetime.utcnow)
 
class OperadorEmpilhadeira(db.Model):
    
    __tablename__ = 'OperadorEmpilhadeira'

    id = Column(Integer, primary_key=True)
    user_id = Column(String)
    user_email = Column(String)
    date_created = Column(DateTime, default=datetime.utcnow)
    nome = Column(String, unique=True)
    cpf = Column(String, unique=True)
    endereço = Column(String)
    município = Column(String)
    inscrição_estadual = Column(String)


class MovimentaçãoOperadorEmpilhadeira(db.Model):
    
    __tablename__ = 'MovimentaçãoOperadorEmpilhadeira'

    id = Column(Integer, primary_key=True)
    user_id = Column(String)
    user_email = Column(String)
    date_created = Column(DateTime, default=datetime.utcnow)
    nome = Column(String, unique=True)


class Maquinário(db.Model):
    
    __tablename__ = 'Maquinário'

    id = Column(Integer, primary_key=True)
    user_id = Column(String)
    user_email = Column(String)
    date_created = Column(DateTime, default=datetime.utcnow)
    local = Column(String)




class MovimentaçãoMaquinário(db.Model):
    
    __tablename__ = 'MovimentaçãoMaquinário'

    id = Column(Integer, primary_key=True)
    user_id = Column(String)
    user_email = Column(String)
    date_created = Column(DateTime, default=datetime.utcnow)
    nome = Column(String, unique=True)

