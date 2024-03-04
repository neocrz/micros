from app import db
from app import bcrypt


class Role(db.Model):
    # roles de usuários do sistema
    __tablename__ = 'roles'

    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(length=64), nullable=False, unique=True)
    users = db.relationship('User', backref='role')

    def __repr__(self):
        return f'<Role {self.name}>'

class User(db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer(), primary_key=True)
    username = db.Column(db.String(length=64), unique=True, nullable=False)
    password_hash = db.Column(db.String(length=64), nullable=False)
    role_id = db.Column(db.Integer, db.ForeignKey('roles.id'))
    
    def __repr__(self):
        return f"User '{self.username}'"

    @property
    def password(self):
        return self.password

    @password.setter
    def password(self, text_password):
        self.password_hash = bcrypt.generate_password_hash(text_password).decode("utf-8")

    def check_password(self, attempd_password):
        return bcrypt.check_password_hash(self.password_hash, attemped_password)

