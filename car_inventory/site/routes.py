from flask import Blueprint, render_template, request, redirect, url_for
from flask_login import login_required, current_user
from car_inventory.forms import CarForm
from car_inventory.models import Car, db
from car_inventory.helpers import random_joke_generator


site = Blueprint('site', __name__, template_folder='site_templates')



@site.route('/')
def home():
    print("oo")
    return render_template('index.html')


@site.route('/profile', methods = ['GET', 'POST'])
@login_required
def profile():
     my_car = CarForm()
    
     


     try:
        print('I try')
        if request.method == "POST" and my_car.validate_on_submit():
            make = my_car.make.data
            model = my_car.model.data
            price = my_car.price.data
            year = my_car.year.data
            vin = my_car.vin.data 
            if my_car.dad_joke.data:
                random_joke = my_car.dad_joke.data
            else:
                random_joke = random_joke_generator() 
            
                     
            user_token = current_user.token

            car = Car(make, model, price, year, vin, random_joke , user_token)

            db.session.add(car)
            db.session.commit()

            return redirect(url_for('site.profile'))
     except:
        raise Exception("Car not created, please check your form and try again!")
    
     

     cars = Car.query.filter_by(user_token=current_user.token).all()

    
     return render_template('profile.html', form=my_car, cars = cars )
    
    