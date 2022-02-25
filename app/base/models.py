#
#
#from flask_login import UserMixin, AnonymousUserMixin
#from sqlalchemy import Binary, Column, Integer, String, Boolean, ForeignKey
#from werkzeug.security import generate_password_hash, check_password_hash
#
#from app import db, login_manager
#
#from app.base.util import hash_pass
#
#class User(db.Model, UserMixin):
#
#    __tablename_ = 'User'
#
#    id = Column(Integer, primary_key=True)
#    username = Column(String, unique=True)
#    email = Column(String, unique=True)
#    password_hash = Column(String(128))
#    role_id = Column(Integer, ForeignKey('Role.id')) 
#
#    @property
#    def password(self):
#        raise AttributeError('password is not a readable attribute')
#
#    @password.setter
#    def password(self, password):
#        self.password_hash = generate_password_hash(password)
#
#    def verify_password(self, password):
#        return check_password_hash(self.password_hash, password)
#
#   # def __init__(self, **kwargs):
#   #     super(User, self).__init__(**kwargs)
#   #     if self.role is None:
#   #         if self.email == current_app.config['SMMDOPN_ADMIN']:
#   #             self.role = Role.query.filter_by(name='Administrator').first()
#   #         if self.role is None:
#   #             self.role = Role.query.filter_by(default=True).first()
#    def can(self, perm):
#        return self.role is not None and self.role.has_permission(perm)
#
#    def is_administrator(self):
#        return self.can(Permission.ADMIN)
#
#    def __repr__(self):
#        return str(self.username)
#
#class Role(db.Model):
#    
#    __tablename__='Role'
#
#    id = db.Column(db.Integer, primary_key=True)
#    name = db.Column(db.String(64), unique=True)
#    default = db.Column(db.Boolean, default=False, index=True)
#    permissions = db.Column(db.Integer)
#    users = db.relationship('User', backref='role', lazy='dynamic')
#
#    # establece a função permissão
#    def __init__(self, **kwargs):
#        super(Role, self).__init__(**kwargs)
#        if self.permissions is None:
#            self.permissions = 0
#    # adc permisão a função 
#    def add_permission(self, perm):
#        if not self.has_permission(perm):
#            self.permissions += perm
#    # remove a permissão
#    def remove_permission(self, perm):
#        if self.has_permission(perm):
#            self.permissions -= perm
#    # reseta a permissão
#    def reset_permissions(self):
#        self.permissions = 0
#    # checa se tem o valor x na permissão
#    def has_permission(self, perm):
#        return self.permissions & perm == perm
#
#    @staticmethod
#    def insert_roles():
#        roles = {
#                'Gatista': [Permission.GATE],
#                'Registro': [Permission.REGISTRO],
#                'Conferente': [Permission.DESCARGA],
#                'Transporte': [Permission.TRANSPORTE],
#                'Gestor Transporte': [Permission.GESTÃO_TRANSPORTE],
#                'Logística': [Permission.GATE, Permission.REGISTRO, Permission.LOGÍSTICA, Permission.DESCARGA],
#                'Comercial': [Permission.COMERCIAL],
#                'Executivo Comercial': [Permission.COMERCIAL, Permission.PROPOSTA_COMERCIAL],
#                'Diretoria Comercial': [Permission.COMERCIAL, Permission.PROPOSTA_COMERCIAL, Permission.DIRETORIA_COMERCIAL],
#                'Diretoria Controladoria': [Permission.DIRETORIA_CONTROLADORIA],
#                'Socios': [Permission.GATE, Permission.REGISTRO, Permission.DESCARGA, Permission.TRANSPORTE, Permission.GESTÃO_TRANSPORTE, Permission.LOGÍSTICA, Permission.COMERCIAL, Permission.PROPOSTA_COMERCIAL, Permission.DIRETORIA_COMERCIAL, Permission.DIRETORIA_CONTROLADORIA, Permission.BOOKING, Permission.INSTRUÇÃO, Permission.SOCIOS, Permission.DIROP],
#                'Administrador': [Permission.GATE, Permission.REGISTRO, Permission.DESCARGA, Permission.TRANSPORTE, Permission.GESTÃO_TRANSPORTE, Permission.LOGÍSTICA, Permission.COMERCIAL, Permission.PROPOSTA_COMERCIAL, Permission.DIRETORIA_COMERCIAL, Permission.DIRETORIA_CONTROLADORIA, Permission.BOOKING, Permission.INSTRUÇÃO, Permission.SOCIOS, Permission.DIROP],
#                }
#        default_role = 'User'
#        for r in roles:
#            role = Role.query.filter_by(name=r).first()
#            if role is None:
#                role = Role(name=r)
#            role.reset_permissions()
#            for perm in roles[r]:
#                role.add_permission(perm)
#            role.default = ( role.name == default_role)
#            db.session.add(role)
#        db.session.commit()
#class AnonymousUser(AnonymousUserMixin):
#    def can(self, permissions):
#        return False
#
#    def is_administrator(self):
#        return False
#
#login_manager.anonymous_user = AnonymousUser
#
#
#
#class Permission:
#    GATE = 1
#    REGISTRO = 2
#    SERVIÇO = 4
#    DESCARGA = 8
#    TRANSPORTE = 16
#    GESTÃO_TRANSPORTE = 32
#    LOGÍSTICA = 64
#    COMERCIAL = 124
#    PROPOSTA_COMERCIAL = 264
#    DIRETORIA_COMERCIAL = 512
#    DIRETORIA_CONTROLADORIA = 1024
#    BOOKING = 2048 
#    INSTRUÇÃO = 4096
#    SOCIOS = 8192
#    DIROP = 16384
#    ADMIN = 32768
#
#@login_manager.user_loader
#def user_loader(id):
#    return User.query.filter_by(id=id).first()
#
#@login_manager.request_loader
#def request_loader(request):
#    username = request.form.get('username')
#    user = User.query.filter_by(username=username).first()
#    return user if user else None
