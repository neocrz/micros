from app import db
from app import bcrypt

class Client(db.Model):
    __tablename__ = "clients"
    id = db.Column(db.Integer(), primary_key=True)
    business_name =  db.Column(db.String(length=128), nullable=False, unique=True) # razão social
    trade_name = db.Column(db.String(length=128), nullable=False, unique=True) # nome fantasia
    address = db.Column(db.String(length=128), nullable=True, unique=False) # Endereço
    address_num = db.Column(db.String(length=16), nullable=True, unique=False) # número


class Equip(db.Model):
    __tablename__ = "equipments"

    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(length=128), nullable=False, unique=True)
    model = db.Column(db.String(length=128), nullable=True, unique=False)
    brand = db.Column(db.String(length=128), nullable=True, unique=False)
    sn = db.Column(db.String(length=64), nullable=True, unique=False)
    orders = db.relationship("Order", backref="equip")

    def __repr__(self):
        return f"<Equip {self.name}>"
 
class Order(db.Model):
    __tablename__ = 'orders'
    id = db.Column(db.Integer(), primary_key=True)
    data_os = db.Column(db.String(length=32), nullable=True, unique=False) 
    data_call = db.Column(db.String(length=32), nullable=True, unique=False) # data do chamado
    request_desc = db.Column(db.String(length=512), nullable=True, unique=False) # motivo do chamado
    status = db.Column(db.Integer(), nullable=False, default=1) # 1:'não realizado' 2:'a continuar' 3:'realizado'
    results = db.Column(db.String(length=512), nullable=True, unique=False) # serviço executado
    obs = db.Column(db.String(length=512), nullable=True, unique=False) # obsevações
    cli_signature = db.Column(db.LargeBinary)
    tec_signature = db.Column(db.LargeBinary)
    equip_id = db.Column(db.Integer, db.ForeignKey("equipments.id"))
    client_id = db.Column(db.Integer, db.ForeignKey("clients.id"))

   

class Role(db.Model):
    # roles de usuários do sistema
    __tablename__ = "roles"

    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(length=64), nullable=False, unique=True)
    users = db.relationship("User", backref="role")

    def __repr__(self):
        return f"<Role {self.name}>"

class User(db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer(), primary_key=True)
    username = db.Column(db.String(length=64), unique=True, nullable=False)
    password_hash = db.Column(db.String(length=64), nullable=False)
    role_id = db.Column(db.Integer, db.ForeignKey("roles.id"))
    
    def __repr__(self):
        return f"User '{self.username}'"

    @property
    def password(self):
        return self.password

    @password.setter
    def password(self, text_password):
        self.password_hash = bcrypt.generate_password_hash(text_password).decode("utf-8")

    def check_password(self, attemped_password):
        return bcrypt.check_password_hash(self.password_hash, attemped_password)

