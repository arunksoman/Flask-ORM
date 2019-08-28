# models.py

from flask_login import UserMixin
from project import db

class User(UserMixin, db.Model):
    __tablename__ = 'user' 
    id = db.Column(db.Integer, primary_key=True) # primary keys are required by SQLAlchemy
    email = db.Column(db.String(40))
    password = db.Column(db.String(40))
    name = db.Column(db.String(40))

    def __init__(self,email,password,name):
        self.email = email
        self.password = password
        self.name = name
