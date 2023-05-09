from flask import Blueprint, request, jsonify
from car_inventory.helpers import token_required, random_joke_generator
from car_inventory.models import db, Car, car_schema, cars_schema

api = Blueprint('api', __name__, url_prefix='/api')


@api.route('/cars', methods = ["POST"])
@token_required
def create_car(our_user):
     make = request.json['make']
     model = request.json['model']
     price = request.json['price']
     year = request.json['year']
     vin = request.json['vin']
     random_joke = random_joke_generator()
     user_token = our_user.token
    
     print(f"User Token: {our_user.token}")

     car = Car(make, model, price , year, vin, random_joke, user_token = user_token )

     db.session.add(car)
     db.session.commit()

     response = car_schema.dump(car)

     return jsonify(response)


@api.route('/cars', methods = ['GET'])
@token_required
def get_cars(our_user):
    owner = our_user.token
    cars = Car.query.filter_by(user_token = owner).all()
    response = cars_schema.dump(cars)

    return jsonify(response)


@api.route('/cars/<id>', methods = ['GET'])
@token_required
def get_car(our_user, id):    
    if id:
        car = Car.query.get(id)
        response = car_schema.dump(car)
        return jsonify(response)
    else:
        return jsonify({'message': 'Valid Id equired'}), 401
    

@api.route('/cars/<id>', methods = ["PUT"])
@token_required
def update_car(our_user): 
    car = car.query.get(id)   
    car.make = request.json['make']
    car.model = request.json['model']
    car.price = request.json['price']
    car.year = request.json['year']
    car.vin = request.json['vin']
    car.random_joke = random_joke_generator()
    car.user_token = our_user.token  

    db.session.commit()

    response = car_schema.dump(car)

    return jsonify(response)

@api.route('/cars/<id>', methods = ['DELETE'])
@token_required
def delete_cars(our_user, id):
    car = Car.query.get(id)
    db.session.delete(car)
    db.session.commit()

    response = car_schema.dump(car)
    return jsonify(response)

