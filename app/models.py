from app import db
from app import bcrypt

class User(db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer(), primary_key=True)
    username = db.Column(db.String(length=64), unique=True, nullable=False)
    password_hash = db.Column(db.String(length=64), nullable=False)

    def __repr__(self):
        return f"User {self.username}"

    @property
    def password(self):
        return self.password

    @password.setter
    def password(self, text_password):
        self.password_hash = bcrypt.generate_password_hash(text_password).decode("utf-8")

    def check_password(self, attempd_password):
        return bcrypt.check_password_hash(self.password_hash, attemped_password)
