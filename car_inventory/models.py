from flask_sqlalchemy import SQLAlchemy
import uuid
from datetime import datetime

#adding flask security for passwords
from werkzeug.security import generate_password_hash, check_password_hash

#import secrets module (from python) generates a token for each user
import secrets

#import flask login to check for an authenticated user and store current user
from flask_login import UserMixin, LoginManager

#import flask marshmallow to help create our Schemas 
from flask_marshmallow import Marshmallow 

db = SQLAlchemy() 
login_manager = LoginManager()
ma = Marshmallow()

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)

class User(db.Model, UserMixin):
    id = db.Column(db.String, primary_key = True)
    first_name = db.Column(db.String(150), nullable = True, default = '')
    last_name = db.Column(db.String(150), nullable = True, default = '')
    email = db.Column(db.String(150), nullable = False)
    password = db.Column(db.String(150), nullable = True, default = '')
    username = db.Column(db.String(150), nullable = False)
    token = db.Column(db.String, default = '', unique = True)
    date_created = db.Column(db.DateTime, nullable = False, default = datetime.utcnow)
    

    def __init__(self, email, username, first_name = '', last_name = '', password = ''):
        self.id = self.set_id()
        self.first_name = first_name
        self.last_name = last_name
        self.password = self.set_password(password)
        self.email = email
        self.username = username
        self.token = self.set_token(24)

    def set_token(self, length):
        return secrets.token_hex(length)
    
    def set_id(self):
        return str(uuid.uuid4())
    
    def set_password(self, password):
        self.pw_hash = generate_password_hash(password)
        return self.pw_hash
    
    def __repr__(self):
        return f"User {self.email} has been added to the database!"
    

class Car(db.Model):
    id = db.Column(db.String, primary_key = True)
    make= db.Column(db.String(25), nullable=True)
    model = db.Column(db.String(25), nullable=True)
    price = db.Column(db.Numeric(precision=10, scale=2))
    year = db.Column(db.Integer, nullable=True)
    vin = db.Column(db.String(50))
    random_joke = db.Column(db.String, nullable=True)
    user_token = db.Column(db.String, db.ForeignKey('user.token'), nullable=False)
   

    def __init__(self, make, model, price, year, vin, random_joke, user_token):
        self.id = self.set_id()
        self.make = make
        self.model = model
        self.price = price
        self.year = year
        self.vin = vin
        self.random_joke = random_joke
        self.user_token = user_token
       

    def set_id(self):
        return str(uuid.uuid4())

    def __repr__(self):
        return f"Car {self.name} has been added to the database!"



class CarSchema(ma.Schema): 
    class Meta:
        fields = ['id', 'make', 'model', 'price', 'year', 'vin','random_joke']

car_schema = CarSchema()
cars_schema = CarSchema(many = True)