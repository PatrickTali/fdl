from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, DecimalField, SubmitField
from wtforms.validators import DataRequired, Email

class UserLoginForm(FlaskForm):
    username = StringField( 'Username', validators=[DataRequired()])
    email = StringField('Email', validators = [DataRequired(), Email()])
    password = PasswordField('Password', validators= [DataRequired()]) 
    submit_button = SubmitField()

class CarForm(FlaskForm):
    make = StringField('make')
    model = StringField('model')
    price = DecimalField('price')
    year = StringField('year')
    vin = StringField('vin')
    dad_joke = StringField('dad joke')
    submit_button =SubmitField()
