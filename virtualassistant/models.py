from virtualassistant import db,app
import datetime
from itsdangerous import JSONWebSignatureSerializer as Serializer



class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120),unique=True,nullable=False)
    email = db.Column(db.String(120),unique=True,nullable=False)
    mobile_no = db.Column(db.String(10),nullable = False)
    department = db.Column(db.String(120), nullable = False)
    
    
    
