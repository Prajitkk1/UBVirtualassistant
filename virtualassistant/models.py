from virtualassistant import db,app
import datetime
from itsdangerous import JSONWebSignatureSerializer as Serializer



class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120),nullable=True)
    email = db.Column(db.String(120),nullable=True)
    mobile_no = db.Column(db.String(15),nullable = True)
    
    
    
