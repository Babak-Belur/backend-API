from app import db 
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash

class Users(db.Model):
    id_user = db.Column(db.BigInteger, primary_key=True, autoincrement=True)
    name = db.Column(db.String(250), nullable=False)
    username = db.Column(db.String(50), index=True, unique=True, nullable=False)
    password = db.Column(db.String(255), nullable=False)
    role = db.Column(db.Enum('Admin', 'User'), nullable=False)

    def __repr__(self):
        return '<Users {}>'.format(self.name)

    def setPassword(self,password):
        self.password = generate_password_hash(password)

    def checkPassword(self,password):
        return check_password_hash(self.password, password)