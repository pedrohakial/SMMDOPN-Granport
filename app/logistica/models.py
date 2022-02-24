from flask_login import UserMixin
from sqlalchemy import Binary, Column, Integer, String, DateTime, Float
from datetime import datetime

from app.base.models import User
from app import db, login_manager

# O Cadastro em si
class CadastroBooking(db.Model):
    
    __tablename__ = 'Booking'

    id = Column(Integer, primary_key=True)
    user_id = Column(String)
    user_email = Column(String)
    date_created = Column(DateTime, default=datetime.utcnow)
    booking_number = Column(String, unique=True)
    armador  = Column(String)
    navio_viagem = Column(String)
    proposta_modal = Column(String)
    porto_origem = Column(String)
    porto_destino = Column(String)
    mercadoria = Column(String)
    quantidade_containers = Column(String)
    tipo_containers = Column(String)
    peso_bruto_containers = Column(String)
    terminal_vazios = Column(String)
   


class NavioViagem(db.Model):
    
    __tablename__ = 'NavioViagem'

    id = Column(Integer, primary_key=True)
    user_id = Column(String)
    user_email = Column(String)
    date_created = Column(DateTime, default=datetime.utcnow)
    booking_number = Column(String, unique=True)
    armador  = Column(String)
    navio_viagem = Column(String)
    proposta_modal = Column(String)
    porto_origem = Column(String)
    porto_destino = Column(String)
    mercadoria = Column(String)
    quantidade_containers = Column(String)
    tipo_containers = Column(String)
    peso_bruto_containers = Column(String)
    terminal_vazios = Column(String)

class MovimentaçãoBooking(db.Model):

    __tablename__='MovimentaçãoBooking'
    
    id = Column(Integer, primary_key=True)
    user_id = Column(String)
    user_email = Column(String)
    date_created = Column(DateTime, default=datetime.utcnow)


class MovimentaçãoNavioViagem(db.Model):

    __tablename__='MovimentaçãoNavioViagem'
    
    id = Column(Integer, primary_key=True)
    user_id = Column(String)
    user_email = Column(String)
    date_created = Column(DateTime, default=datetime.utcnow)

